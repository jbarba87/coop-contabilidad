from odoo import models, fields, api
from datetime import datetime
from odoo.exceptions import ValidationError

class coop_factura_cronograma(models.Model):
  _inherit = 'account.invoice'

  #cronograma = fields.One2many('coop_contabilidad.cronograma', 'cronograma_id', string="Cronograma")

  def calcula_cuotas(self):
    #for mes in range(1, self.num_cuotas + 1):
    #  print(" Cuota: " + str(mes) + ", monto:" + str(self.cuota_mensual))
    if self.state == 'paid':
      raise ValidationError('La factura ya ha sido cancelada.')
      return

    if self.num_cuotas == 0 or self.interes < 0.0001:
      raise ValidationError('Por favor establezca interes y numero de cuotas validas.')
      return

    if self.desdoblada == True:
      raise ValidationError('La factura ya ha sido desdoblada en cuotas.')
      return

    n = self.num_cuotas

    mes_actual = datetime.now().month
    anho_actual = datetime.now().year
    dia = 14  # Dia de vencimiento

    # creacion de listas base para mes y año
    meses_cuotas = [ mes_actual + i for i in range(1, n + 1) ]
    anhos_cuotas = [ anho_actual for i in range(1, n + 1) ]

    # Cantidad maxima de años de credito
    # Se usa segun las veces que se le tenga que restar 12 al numero de mes
    max_anhos = 8

    for index, value in enumerate(meses_cuotas):
      for i in range(max_anhos): 
        if value > 12:
          meses_cuotas[index] = meses_cuotas[index] - 12
          anhos_cuotas[index] = anhos_cuotas[index] + 1
          value = value - 12

    fechas = []

    # Creo el string fecha con los datos de los vectores
    for index, mes in enumerate(meses_cuotas):
      fecha = str( anhos_cuotas[index] ) + '-' + str( meses_cuotas[index] ) + '-' + str(dia)
      fechas.append(fecha)
      

    # Creacion de los records en cuotas
    for i in range(n):
      vals = {
        'fecha_venc' : fechas[i],
        'num_cuota' : i + 1,
        'monto_cuota' : self.cuota_mensual,
        'factura_id' : self.id,
        'monto_abonado' : 0,
      }
      self.env['coop_contabilidad.cuota'].create(vals)

      self.desdoblada = True


  @api.onchange('num_cuotas', 'interes', 'amount_total')
  def calc_cuota(self):
    if self.num_cuotas == 0 or self.interes < 0.0001:
      #self.num_cuotas = 12
      #self.interes = 0.05
      self.cuota_mensual = 0

    i = (1 + self.interes/100.0)**(1/12) - 1
    n = self.num_cuotas

    self.cuota_mensual = self.amount_total*( ( i*(i + 1)**n )/( (1 + i)**n - 1 )  )


  num_cuotas = fields.Integer(string="Numero de Cuotas", default=12)
  interes = fields.Float(string="Interes", default=5)
  dia_vencimiento = fields.Integer(string="Dia vencimiento", default=14)
  cuotas = fields.One2many('coop_contabilidad.cuota', 'factura_id', string="Cuotas")

  #desdoblada
  desdoblada = fields.Boolean(default = False)


  # Campos computados
  cuota_mensual = fields.Float(string="Cuota mensual", compute="calc_cuota")