with open('Trin2.csv', 'r') as t1, open('Trin1.csv', 'r') as t2:
    fileone = t1.readlines()
    filetwo = t2.readlines()

with open('Trinity.csv', 'w') as outFile:
    for line in filetwo:
        if line not in fileone:
            outFile.write(line)
