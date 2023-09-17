
from tools.calcs import Calcs


systems = {}
programs = {}

with open("data/Q1.txt", "+r") as data:
    dataLines = data.readlines()

    for line in dataLines:
        data = line.split(" ")
        dataInt = []
        for i in data[1:]:
            dataInt.append(int(i))
        programs[data[0]] = dataInt

    for line in dataLines:
        data = line.split(" ")
        for i in range(1, len(data)):
            systems.update({str(i): []})

    for line in dataLines:
        data = line.split(" ")
        j = 1
        for i in data[1:]:
            systems[str(j)].append(int(i))
            j += 1

calc = Calcs()

i = 1
for program in programs.keys():
    print(f"########## Program ({i}): ")
    print(f"ArithmeticAverage: {calc.ArithmeticAverage(programs[program])}\n")
    print(f"GeometricAverage: {calc.GeometricAverage(programs[program])}\n")
    print(f"HarmonicAverage: {calc.HarmonicAverage(programs[program])}\n")
    print(f"Median: {calc.Median(programs[program])}\n")
    print(f"Variance: {calc.Variance(programs[program])}\n")
    print(
        f"StandardDerivation: {calc.StandardDerivation(programs[program])}\n")
    i += 1

i = 1
for system in systems.keys():
    print(f"########## System ({i}): ")
    print(f"ArithmeticAverage: {calc.ArithmeticAverage(systems[system])}\n")
    print(f"GeometricAverage: {calc.GeometricAverage(systems[system])}\n")
    print(f"HarmonicAverage: {calc.HarmonicAverage(systems[system])}\n")
    print(f"Median: {calc.Median(systems[system])}\n")
    print(f"Variance: {calc.Variance(systems[system])}\n")
    print(
        f"StandardDerivation: {calc.StandardDerivation(systems[system])}\n")
    i += 1
