class Liquidificador:
  def __init__(self, cor, potencia, voltagem, preco):
    self.preco = preco
    self.__cor = cor
    self.__potencia = potencia
    self.__voltagem = voltagem
    self.__ligado = False
    self.__velocidade = 0
    self.__velocidade_maxima = 3
    self.__amperagem_atual_no_motor = 0
    
  
  def __str__(self):
    return f""" teste
  {self.__cor }
    {self.__potencia} = potencia
    {self.__voltagem} = voltagem
    {self.__ligado} = False
    {self.__velocidade} = 0
    {self.__velocidade_maxima} = 3
    {self.__amperagem_atual_no_motor} = 0
  """
  
  def ligar(self, velocidade):
    self.__velocidade = velocidade
    self.__amperagem_atual_no_motor = (
      (self.__potencia / self.__voltagem) / self.__velocidade_maxima
      ) * velocidade
    self.__ligado = True
    
    
  def desligar(self):
    self.__velocidade =0
    self.__ligado = False
    
    
  def esta_ligado(self):
    return self.__ligado
          
class Pessoa:
  def __init__(self, nome, saldo_na_conta):
    self.nome = nome
    self.saldo_na_conta = saldo_na_conta
    self.liquidificador = None
    
  def comprar_liquidificador(self, liquidificador: Liquidificador):
    if liquidificador.preco <= self.saldo_na_conta:
      self.saldo_na_conta -= liquidificador.preco
      self.liquidificador = liquidificador

pessoa_cozinheira = Pessoa('Jacquin', 1000)
pessoa_cozinheira.comprar_liquidificador(Liquidificador('preto', 450, 220, 250))

print(pessoa_cozinheira.liquidificador)
