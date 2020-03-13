def isValid(row):
    valid = False

    if (conditionValidationDigit(row[3])) \
            and (conditionValidationDigit(row[4])) \
            and (conditionValidationDigit(row[5])) \
            and (conditionValidationDigit(row[6])) \
            and (conditionValidationDigit(row[7])):
        valid = True

    return valid


def conditionValidationDigit(row):
    valid = False
    if row != None and row.isnumeric() == True:
        valid = True

    return valid


def constructColumn(row):
    dict = {
        "EDP": "Eau de parfum",
        "EAU DE PARFUM": "Eau de parfum",
        "EDT": "Eau de toilette",
        "EAU DE TOILETTE": "Eau de toilette",
        "DEO": "Deodorant",
        "DEODORANT": "Deodorant",
        "BODY LOTION": "Body lotion",
        "SHOWER GEL": "Shower gel",
        "AFTER SHAVE": "After shave"
    }
    type = ""
    for x, y in dict.items():
        if ((row[2].upper()).__contains__(x)): type = y

    column = ''
    column += (row[1], row[0])[row[0] != ''] + ";"
    column += "'" + row[2].strip() + " " + row[3].strip() + " ML" + "';"
    column += row[3].strip() + ";"
    column += row[4].strip() + ";"
    column += row[7].strip() + ";"
    column += row[5].strip() + ";"
    column += row[6].strip() + ";"
    column += "'" + type + "';"
    column += "'" + row[int(len(row))-1].strip() + "';"
    column += "\n"

    return column


class ParseError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = 'Impossible de parser'

    def __str__(self):
        return self.message


def getDatas(tab):
    datas = []
    nbLignes = 0
    for fileData in tab:
        try:
            nbLignes += 1
            if (fileData[0] != '' and fileData[0].isdigit()):
                datas.append(fileData)
            elif (fileData[0] == '' or fileData[0].isdigit() == False):
                if (len(fileData) > 1 and fileData[1] != '' and fileData[1].isdigit()):
                    datas.append(fileData)
        except:
            raise ParseError

    return datas


def getModele():
    file = None
    try:
        file = open("coty.csv", "r")
    except:
        raise FileNotFoundError

    if file == None: raise FileNotFoundError

    temp = []
    for line in file:
        try:
            line = line.rstrip('\n\r')
            fileData = line.split(';')
            temp.append(fileData)
        except:
            raise ParseError
    for i in range(len(temp)):
        if (temp[i][0] != '' and temp[i][0].isdigit() and len(temp[i]) > 1 and i > 5):
            if (temp[i][1] != ''):
                for j in range(i):
                    if (temp[i - j][0] == '' and temp[i - j][1] == '' and temp[i - j][2] != ''):
                        if ((temp[i - j][2]).upper().__contains__("EAU DE")):
                            index = (temp[i - j][2]).find("-")
                            model = (temp[i - j][2])[0: index]
                            temp[i].append(model)
                            break
                        else:
                            temp[i].append((temp[i - j][2]))
                            break
    return temp


try:
    datas = getModele()
    newdatas = getDatas(datas)
    for data in newdatas: print(data)
except FileNotFoundError:
    print("Impossible d'ouvrir le fichier")
except ParseError:
    print('Impossible de parser le fichier')

try:
    f = open('datas.csv', 'w')
    fe = open('error.csv', 'w')
except FileNotFoundError:
    print("Impossible d'ouvrir le fichier")

try:
    for r in newdatas:
        if isValid(r):
            fe.write(constructColumn(r))
        else:
            f.write(constructColumn(r))

except TypeError:
    print('erreur lors de la création de la ligne')
