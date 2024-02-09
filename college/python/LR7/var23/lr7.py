with open("vhid.txt", "r") as file1, open("vyhid.txt", "w") as file2:
    lines = file1.readlines()
    lines.pop(5 - 1)
    file2.writelines(lines)