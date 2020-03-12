def constructColumn(row):
    column = ''
    column += "'" + (row[1],row[0])[row[0] != ''] + "';"
    column += "'" + row[2].strip() + " " + row[3].strip() + " ML" + "';"
    column += "'" + row[3].strip() + "';"
    column += "'" + row[4].strip() + "';"
    column += "'" + row[7].strip() + "';"
    column += "'" + row[5].strip() + "';"
    column += "'" + row[6].strip() + "';"
    column += "'" + '' + "';"
    column += "'" + '' + "';"
    column += "'" + '' + "\n"

    return column

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
    f.write(constructColumn(r))
