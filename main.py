from toll import *
from actions import *

keepLoop = True
tollPaths = defineTollPaths()
tollBank = defineTollBank(tollPaths)

while keepLoop:
    action = chooseAction()

    if action == INSERT:
        tollIndex = chooseToll(tollPaths)
        vehicleType = chooseVehicleType()
        addToToll(tollPaths[tollIndex], vehicleType)
    elif action == REMOVE:
        tollIndex = chooseToll(tollPaths)
        removeFromToll(tollPaths[tollIndex], tollIndex, tollBank)
    elif action == SHOW:
        tollIndex = chooseToll(tollPaths)
        showToll(tollIndex, tollPaths[tollIndex])
    elif action == CASH_OUT:
        tollIndex = chooseToll(tollPaths)
        showTollBank(tollIndex, tollBank[tollIndex])
    elif action == EXIT:
        showAllTolls(tollPaths)
        showCompleteTollBank(tollBank)
        keepLoop = False
    else:
        print("Escolha uma opção válida")