import csv

separators = ["PRIMERO","SEGUNDO","TERCERO","CUARTO"]
with open('notas.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    tot,ects = 0,0
    for row in csv_reader:
        if row[-1] == "APTO":
            continue
        if row[1] in separators:

            #end of the semester
            mean = tot / ects
            print(separators[separators.index(row[1]) -1]+": " + '%.2f' % (tot/ects))
            ects = 0
            tot = 0
            continue
        ects += float(row[2].replace(",",".")) 
        tot +=  float(row[2].replace(",",".")) * float(row[-1].split("(")[1].split(")")[0].replace(",","."))

    print(separators[-1] + ": " + '%.2f' % (tot/ects))
