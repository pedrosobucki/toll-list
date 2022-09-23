INSERT = 1
REMOVE = 2
SHOW = 3
CASH_OUT = 4
EXIT = 5

ACTIONS = [
  INSERT,
  REMOVE,
  SHOW,
  CASH_OUT,
  EXIT
]

def actionExists(action: int):
  return action in ACTIONS

def chooseAction():
    chosen = False

    while not chosen:
        try:
            action = int(input("1-Incluir, 2-Retirar, 3-Mostrar Filas, 4-Mostrar Lucro, 5-Sair: "))
            if actionExists(action):
              chosen = True
            else:
              print("Insira um valor válido.")
        except:
            print("Insira um valor válido.")
    return action