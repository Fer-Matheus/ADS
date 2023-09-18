from tools.calcs import Calcs

redeASimulation = []
redeBSimulation = []

with open("data/Q2_c.txt") as data:
    dataLines = data.readlines()

    for line in dataLines:
        source = line.split(" ")
        xi, fiA, fiB = float(source[0]), float(source[1]), float(source[2])
        redeASimulation.append((xi, fiA))
        redeBSimulation.append((xi, fiB))
        
calc = Calcs()

print(f"########## RedeA: ")
print(f"ArithmeticAverage: {calc.ArithmeticAverage(redeASimulation, True)}\n")
print(f"GeometricAverage: {calc.GeometricAverage(redeASimulation, True)}\n")
print(f"HarmonicAverage: {calc.HarmonicAverage(redeASimulation, True)}\n")
print(f"Variance: {calc.Variance(redeASimulation, True)}\n")
print(f"StandardDerivation: {calc.StandardDerivation(redeASimulation, True)}\n")

print(f"########## RedeB: ")
print(f"ArithmeticAverage: {calc.ArithmeticAverage(redeBSimulation, True)}\n")
print(f"GeometricAverage: {calc.GeometricAverage(redeBSimulation, True)}\n")
print(f"HarmonicAverage: {calc.HarmonicAverage(redeBSimulation, True)}\n")
print(f"Variance: {calc.Variance(redeBSimulation, True)}\n")
print(f"StandardDerivation: {calc.StandardDerivation(redeBSimulation, True)}\n")

print(redeASimulation)
print(redeBSimulation)
