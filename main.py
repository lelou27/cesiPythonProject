def colonne1(row):
    return (row[1],row[0])[row[0] != '']

def colonne2(row):
    return row[2].strip() + " " + row[3].strip() + " ML"

def colonne3(row):
    return row[3].strip()

def colonne4(row):
    return row[4].strip()

def colonne5(row):
    return row[7].strip()

def colonne6(row):
    return row[5].strip()

def colonne7(row):
    return row[6].strip()

def colonne8(row):
    return ''

def colonne9(row):
    return ''

def colonne10(row):
    return ''

class ParseError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = 'Impossible de parser'

    def __str__(self):
        return self.message

def getDatas():
    file=None
    try:
        file = open("coty.csv", "r")
    except:
        raise FileNotFoundError

    if file == None : raise FileNotFoundError

    datas = []
    for line in file:
        try:
            line = line.rstrip('\n\r')
            fileData = line.split(';')
            if (fileData[0] != '' and fileData[0].isdigit()):
                datas.append(fileData)
            elif(fileData[0] == '' or fileData[0].isdigit() == False):
                if(len(fileData) > 1):
                    if(fileData[1] != '' and fileData[1].isdigit()):
                        datas.append(fileData)
        except:
            raise ParseError

    return datas


try:
    datas = getDatas()
    for data in datas: print(data)
except FileNotFoundError:
    print("Impossible d'ouvrir le fichier")
except ParseError:
    print('Impossible de parser le fichier')


f = open('datas.csv', 'w')
for r in datas:
    f.write("'" + colonne1(r) + "',")
    f.write("'" + colonne2(r) + "',")
    f.write("'" + colonne3(r) + "',")
    f.write("'" + colonne4(r) + "',")
    f.write("'" + colonne5(r) + "',")
    f.write("'" + colonne6(r) + "',")
    f.write("'" + colonne7(r) + "',")
    f.write("'" + colonne8(r) + "',")
    f.write("'" + colonne9(r) + "',")
    f.write("'" + colonne10(r) + "'\n")
