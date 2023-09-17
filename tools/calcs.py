class Calcs:

    def __init__(self, dataBase):
        self.dataBase = dataBase
        self.dataSize = len(self.dataBase)

    def __init__(self):
        None

    def ArithmeticAverage(self):
        summation = 0
        for i in self.dataBase:
            summation += i
        return summation/self.dataSize

    def GeometricAverage(self):
        product = 1
        for i in self.dataBase:
            product *= i
        return round(product**(1/self.dataSize), 2)

    def HarmonicAverage(self):
        summation = 0
        for i in self.dataBase:
            summation += 1/i
        return round((self.dataSize/summation), 2)

    def Median(self):
        self.dataBase.sort()
        if (self.dataSize % 2) == 0:
            med = self.dataSize // 2
            return round((self.dataBase[med]+self.dataBase[med+1]), 2)
        else:
            med = (self.dataSize+1) // 2
            return self.dataBase[med-1]

    def Variance(self):
        average = self.ArithmeticAverage()
        summation = 0
        for i in self.dataBase:
            summation += (i - average)**2
        return summation / (self.dataSize-1)

    def StandardDerivation(self):
        return self.Variance()**(1/2)

    def ArithmeticAverage(self, dataBase=list, classes=False):
        summation = 0
        if classes:
            summationFi = 0
            for xi, fi in dataBase:
                summation += xi*fi
                summationFi += fi
            return round(summation/summationFi, 2)
        for i in dataBase:
            summation += i
        return round(summation/len(dataBase), 2)

    def GeometricAverage(self, dataBase=list, classes=False):
        product = 1
        if classes:
            summationFi = 0
            for xi, fi in dataBase:
                product *= xi**fi
                summationFi += fi
            return round(product**(1/summationFi), 2)
        for i in dataBase:
            product *= i
        return round(product**(1/len(dataBase)), 2)

    def HarmonicAverage(self, dataBase=list, classes=False):
        summation = 0
        if classes:
            summationFi = 0
            for xi, fi in dataBase:
                summation += (1/xi)*fi
                summationFi += fi
            return round((summationFi/summation), 2)
        for i in dataBase:
            summation += 1/i
        return round((len(dataBase)/summation), 2)

    def Median(self, dataBase=list):
        dataBase.sort()
        if (len(dataBase) % 2) == 0:
            med = len(dataBase) // 2
            return round((dataBase[med]+dataBase[med+1]), 2)
        else:
            med = (len(dataBase)+1) // 2
            return dataBase[med-1]

    def Variance(self, dataBase=list, classes=False):
        average = self.ArithmeticAverage(dataBase, classes)
        summation = 0
        summationFi = 0
        if classes:
            for xi, fi in dataBase:
                summation += ((xi - average)**2)*fi
                summationFi += fi
            return round(summation / summationFi)
        for i in dataBase:
            summation += (i - average)**2
        return round(summation / (len(dataBase)-1))

    def StandardDerivation(self, dataBase=list, classes=False):
        if classes:
            return round(self.Variance(dataBase, classes)**(1/2), 2)
        return round(self.Variance(dataBase)**(1/2), 2)
