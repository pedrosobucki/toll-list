CAR = 1
TRUCK = 2

VEHICLE_TYPES = [ CAR, TRUCK ]
VEHICLE_TYPE_VALUES = [ 300, 450 ]

def chooseVehicleType():
  choiceIsValid = False

  while not choiceIsValid:

      try:
          vehicleType = int(input("Qual tipo de veículo entrará na fila? (1 ou 2)"))
          
          if vehicleTypeExists(vehicleType):
              choiceIsValid = True
          else:
            print("Insira um valor válido.")

      except:
          print("Insira um valor válido.")

  return vehicleType

def retrieveVehicleValue(vehicleType: int):

  if vehicleTypeExists(vehicleType):
    return VEHICLE_TYPE_VALUES[vehicleType-1]

def vehicleTypeExists(vehicleType: int):
  return vehicleType in VEHICLE_TYPES