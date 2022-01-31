

def hotelCost(amountNights, roomCost):
   totalCostH = (amountNights * roomCost)
   return totalCostH
   

def planeCost(city):
   
   if city == "paris":
      flightCost = 1500
   elif city == "new york":
      flightCost = 2000
   elif city == "barcelona":
      flightCost = 1000
   elif city == "london":
      flightCost = 1500
   elif city == "istanbul":
      flightCost = 1000
   return flightCost
   

def carRental(amountDays):
   totalCostC = (amountDays * 100)
   return totalCostC
   

def holidayCost(city,amountDays,amountNights,roomCost):
   holidayCost = (hotelCost(amountNights, roomCost)+planeCost(city)+carRental(amountDays))
   return("A holiday to " + city + " will cost you : $" + str(holidayCost))


userInput= input("Would you like to go on holiday ?\nYes or No : ")



if userInput == "yes" :

   city = input("Please enter a City you would like to travel to :\nparis\nnew york\nbarcelona\nlondon\nistanbul : ")
   
   carOption = input("would you like to rent a car ?: ")
   
   if carOption == "yes" :
      amountDays = int(input("Please enter how many days you would like to rent the car for : "))
      
   
   roomOption = input("There are 3 room choices :\nGold = 1000 a night\nSilver = 750 a night\nBronze = 500 a night\nPlease enter either 'Gold', 'Silver' or 'Bronze' : ")
   
   if roomOption == "gold" :
      roomCost = 1000
   elif roomOption == "silver" :
      roomCost = 750
   elif roomOption == "bronze" :
      roomCost = 500
   else :
     print("No valid room option was choosen")
     
   amountNights = int(input("Please enter the amount of nights you would like to stay : "))
     
   print( holidayCost(city,amountDays,amountNights,roomCost))