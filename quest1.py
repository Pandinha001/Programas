class Carteira:
  def __init__(self, moeda: str, saldo: float):
    self.moeda = moeda
    self.saldo = saldo
  
  def converter(self, val_yuan):
    if self.moeda == 'USD':
      return self.saldo*0.14
    elif self.moeda == 'BRL':
      return self.saldo*0.85
    else:
      return val_yuan
  def __add__(self, val_yuan):
    if self.moeda != 'YUAN':
      return self.saldo + self.converter(val_yuan)
    else:
      return self.saldo + val_yuan
  def __sub__(self, val_yuan):
    if self.moeda != 'YUAN':
      return self.saldo - self.converter(val_yuan)
    else:
      return self.saldo - val_yuan

carteira_usd = Carteira("USD", 10.0)
print('Soma de carteira USD + 50 yuan = ', carteira_usd + 50.0)
carteira_brl = Carteira("BRL", 30.0)
print('Soma de carteira BRL + 20 yuan = ', carteira_brl + 20.0)
