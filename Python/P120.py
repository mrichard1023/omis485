def ground_shipping_cost(weight):
  cost = ""
  if weight <= 2:
    cost = (weight*1.5)+20
  elif weight <= 6:
    cost = (weight*3)+20
  elif weight <= 10:
    cost = (weight*4)+20
  else:
    cost = (weight*4.75)+20
  return cost
print(ground_shipping_cost(8.4))

premium_ground_shipping = 125

def drone_shipping_cost(weight):
  drone_cost = ""
  if weight <= 2:
    drone_cost = weight*4.5
  elif weight <= 6:
    drone_cost = weight*9
  elif weight <= 10:
    drone_cost = weight*12
  else:
    drone_cost = weight*14.25
  return drone_cost

print(drone_shipping_cost(1.5))

def best_cost(weight):
  ground = ground_shipping_cost(weight)
  premium = premium_ground_shipping
  drone = drone_shipping_cost(weight)
  
  if ground<premium and ground <drone:
    method = "Standard Ground"  
    cost = ground
  elif premium < ground and premium < drone:
    method = "Premium Ground"
    cost = premium
  else:
    method = "Drone"
    cost = drone
  print("The cheapest price available is $"+ str(cost)+ " using the " + str(method) + " method. ")
  
print(best_cost(4.8))
print (best_cost(41.5))