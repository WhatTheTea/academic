import csv

try:
    studCount = int(input("Студентів: "))
    if studCount < 0:
        raise Exception("Число студентів повинно бути більше нуля")
except Exception as e:
    print(e)
    exit()

fileName = "6.1.csv"
# write
with open(fileName, "w") as file:
    for i in range(1, studCount + 1):
        try:
            name = input("Уведіть ПІБ: ")
            grade = float(input("Оцінка з курсу Інформатики: "))
            if grade < 1 or grade > 12:
                raise Exception("Некоректна оцінка")
        except Exception as e:
            i-=1
            print(e)
            continue
        file.write("%i\t %s\t %.2f\n" % (i, name, grade))
# read
with open(fileName, "r") as file:
    studCount = 0
    avg = 0
    csvRead = csv.reader(file, delimiter="\t")
    for row in csvRead:
        print(row)
        studCount += 1
        avg += float(row[2])
    print("Студентів: ", studCount, "Середній бал з Інформатики: ", avg)
