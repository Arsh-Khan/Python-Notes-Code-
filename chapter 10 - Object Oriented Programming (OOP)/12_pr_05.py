'''
1 2 3 4 5 6 7 8 9 10

'''
class Train:

    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("*********************")
        print(f"Name of Train is {self.name}")
        print(f"The seats available in the train is {self.seats}")
        print("*********************")

    def getFareInfo(self):
        print(f"The price of the ticket is {self.fare}")

    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked! Your Seat no is {self.seats}")
            self.seats = self.seats-1
        else:
            print("Sorry the train is full! Kindly try for tatkal")

    def cancelTicket(self):
        pass

Intercity = Train("Intercity Express : 14015" , 90 , 2)

Intercity.getStatus()

Intercity.getFareInfo()

Intercity.bookTicket()

Intercity.bookTicket()

Intercity.bookTicket()
