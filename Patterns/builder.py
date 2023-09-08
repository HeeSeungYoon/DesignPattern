class AbstractBuilder:
    def buildDay(self, date):
        pass

    def addHotel(self, date, hotel):
        pass

    def addReservation(self):
        pass

    def addSpecialEvent(self):
        pass

    def addTickets(self, ticket):
        pass

    def getVacationPlanner(self):
        pass

class VacationBuilder(AbstractBuilder):
    def __init__(self) -> None:
        self.vacation = {}

    def getVacationPlanner(self):
        return self.vacation

def constructPlanner(builder, date):
    builder.buildDay(date)
    builder.addHotel(date, "Grand Facadian")
    builder.addTickets("Patterns on Ice")

    myPlanner = builder.getVacationPlanner()

# Client
if __name__ == '__main__':
    builder = VacationBuilder()
    constructPlanner(builder, '2023-09-08')
    
