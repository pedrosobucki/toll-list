from vehicle import *

def defineTollPaths():
  validInput = False

  while not validInput:
    try:
      totalPaths = int(input("Insira o número de faixas do pedágio: "))

      if (totalPaths > 0):
        tollPaths = []
        while totalPaths > 0:
          tollPaths.append([])
          totalPaths -= 1

        validInput = True
      else:
        print("Insira um valor numérico válido")
        
    except:
      print("Insira um valor numérico válido")
  
  return tollPaths

def defineTollBank(totalPaths: list):

    tollBank = []
    for i in range(len(totalPaths)):
        tollBank.append(0)

    return tollBank



def tollExists(tollIndex: int, tollPaths: list):
  return tollIndex >= 0 and tollIndex < len(tollPaths)

def chooseToll(tollPaths: list):
    choiceIsValid = False

    while not choiceIsValid:

        try:
            tollIndex = int(input("Em qual fila? "))
            
            if tollExists(tollIndex, tollPaths):
                choiceIsValid = True
            else:
              print("Insira um valor válido.")

        except:
            print("Insira um valor válido.")

    return tollIndex


def showAllTolls(tollPaths: list):
    for i, toll in enumerate(tollPaths):
        showToll(i, toll)
        
def showToll(tollIndex: int, toll: list):
    print("Fila "+str(tollIndex)+": "+str(toll))


def addToToll(toll: list, vehicleType: int):
    toll.append(vehicleType)


def removeFromToll(toll: list, tollIndex: int, tollBank: list):
    if len(toll) > 0:

        vehicleType = toll.pop(0)
        payToll(vehicleType, tollIndex, tollBank)
        print("Veículo de tipo \"" + str(vehicleType) + "\" removido da Fila "+str(tollIndex)+"!")

        return True

    print("A fila está vazia!")
    return False

def payToll(vehicleType:int, tollIndex: int, tollBank: list):
    tollBank[tollIndex] += retrieveVehicleValue(vehicleType)
    return True
  
def showTollBank(tollIndex: int, tollProfit: int):
  formattedProfit = "{:.2f}".format(tollProfit/100)
  print("Fila " + str(tollIndex) + ": R$" + formattedProfit + ".")

def showCompleteTollBank(tollBank: list):
  for i, profit in enumerate(tollBank):
    showTollBank(i, profit)
