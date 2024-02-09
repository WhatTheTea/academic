import csv

try:
    studCount = int(input("Студентів: "))
    if studCount < 0:
        raise Exception("Число студентів повинно бути більше нуля")
except Exception as e:
    print(e)
    exit()

def checkGrade(grade):
    if grade < 1 or grade > 5:
        raise Exception("Некоректна оцінка")

fileName = "LW6.csv"
# write
with open(fileName, "w", newline='') as file:
    csvWrite = csv.writer(file)
    for i in range(1, studCount + 1):
        try:
            name = input("Уведіть ПІБ: ")
            gradeProgramming = float(input("Оцінка з дисципліни Програмування: "))
            gradeElectronics = float(input("Оцінка з дисципліни Електроніки: "))
        except Exception as e:
            i-=1
            print(e)
            continue
        csvWrite.writerow([i, name, gradeProgramming, gradeElectronics])
# read
with open(fileName, "r") as file:
    studCount = 0
    avgProg = 0
    avgElec = 0
    csvRead = csv.reader(file)
    for row in csvRead:
        print(row)
        studCount += 1
        avgProg += float(row[2])
        avgElec += float(row[3])
    avgProg /= studCount
    avgElec /= studCount
    print("Студентів: ", studCount, "Середній бал з Програмування: ", avgProg, "Середній бал з Електроніки: ", avgElec)
