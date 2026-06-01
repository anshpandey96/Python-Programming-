from random import randint

class Train:
    def __init__(slf, trainNo):
        slf.trainNo = trainNo

    def book(self , fro, to):
        print(f"Ticket is booked from {fro} to {to} on train no {self.trainNo}")

    def getStatus(self):
        print(f"Train no {self.trainNo} is on time")

    def getFare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,5555)}")


t = Train(12399)

t.book("Rampur", "Mumbai")
t.getStatus() 
t.getFare("Rampur", "Mumbai")

