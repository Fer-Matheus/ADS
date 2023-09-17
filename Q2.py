from tools.calcs import Calcs

redeA = []
redeB = []

with open("data/Q2.txt") as data:
    dataLines = data.readlines()

    for line in dataLines:
        source = line.split(" ")
        xi, fiA, fiB = float(source[0]), float(source[1]), float(source[2])
        redeA.append((xi, fiA))
        redeB.append((xi, fiB))

calc = Calcs()

print(f"########## RedeA: ")
print(f"ArithmeticAverage: {calc.ArithmeticAverage(redeA, True)}\n")
print(f"GeometricAverage: {calc.GeometricAverage(redeA, True)}\n")
print(f"HarmonicAverage: {calc.HarmonicAverage(redeA, True)}\n")
print(f"Variance: {calc.Variance(redeA, True)}\n")
print(f"StandardDerivation: {calc.StandardDerivation(redeA, True)}\n")

print(f"########## RedeB: ")
print(f"ArithmeticAverage: {calc.ArithmeticAverage(redeB, True)}\n")
print(f"GeometricAverage: {calc.GeometricAverage(redeB, True)}\n")
print(f"HarmonicAverage: {calc.HarmonicAverage(redeB, True)}\n")
print(f"Variance: {calc.Variance(redeB, True)}\n")
print(f"StandardDerivation: {calc.StandardDerivation(redeB, True)}\n")

print(redeA)
print(redeB)
