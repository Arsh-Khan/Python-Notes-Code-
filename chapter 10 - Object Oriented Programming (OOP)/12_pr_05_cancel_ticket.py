'''
1 2 3 4 5 6 7 8 9 10

'''
class Train:

    def __init__(self,name,fare,l1,seats):
        self.name = name
        self.fare = fare
        self.seats = seats
        self.l1 = l1

    def getStatus(self):
        print("*********************")
        print(f"Name of Train is {self.name}")
        print(f"The seats available in the train is {self.seats}")
        print("*********************")

    def getFareInfo(self):
        print(f"The price of the ticket is {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your Seat no is {(self.l1).pop(-1)}")
            self.seats=self.seats-1
        else:
            print("Sorry the train is full! Kindly try for tatkal")

    def cancelTicket(self,SeatNo):
      print("Your Seat has been Cancelled!")
      self.seats = self.seats + 1
      l1.append(SeatNo)  


l1=[]
for i in range(1,301):
    l1.append(i)
Intercity = Train("Intercity Express : 14015" , 90 , l1 ,300)

Intercity.getStatus()

Intercity.getFareInfo()

Intercity.bookTicket()

Intercity.bookTicket()

Intercity.bookTicket()


Intercity.cancelTicket(300)

Intercity.bookTicket()

Intercity.bookTicket()



































