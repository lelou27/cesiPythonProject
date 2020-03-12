def getDatas():
    try:
        file = open("D:\coty.csv", "r")
        datas = []
        for line in file:
            line =line.rstrip('\n\r')
            fileData = line.split(';')
            if(fileData[0] != '' and fileData[0].isdigit()):
                datas.append(fileData)
            elif(fileData[0] == '' and fileData[1] != ''):
                datas.append(fileData)
        return datas

    except:
        print("Erreur lors de la lecture du fichier")

datas = getDatas()
for data in datas: print(data)
