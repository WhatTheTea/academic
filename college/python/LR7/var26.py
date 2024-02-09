from random import randint as rint
def task():
    with open("input.txt", "w") as file:
        for i in range(10):
            print(rint(1,1000), 0, rint(1,1000), sep="", file=file)

    with open("input.txt", "r") as fin, open("output.txt", "w") as fout:
        for line in fin:
            isAfterZeroRemoved = False
            for c in range(len(line)):
                if(line[c-1] == "0" and not isAfterZeroRemoved):
                    fout.write("")
                    isAfterZeroRemoved = True
                else:
                    fout.write(line[c])