class Country:
    def __init__(self, name: str, population: int, square: float):
        self.name: str = name
        self.population: int  = population
        self.square: float  = square
    
    def increasePopulation(self, count: int):
        self.population += count
        print('Population increased by {0}'.format(count))

    def multiplySquare(self, amount: float):
        self.square *= amount
        print('Area multiplied by {0}. Capture is inevitable'.format(amount))

    def getInfo(self):
        print('Name: {0}, Population: {1}, Square: {2}'.format(self.name, self.population, self.square))


if __name__ == '__main__':
    australia = Country('Australia', 500, 2000)
    australia.getInfo()
    australia.increasePopulation(25)
    australia.getInfo()
    australia.multiplySquare(2.5)
    australia.getInfo()

    

        