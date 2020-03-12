try :
    file = open("coty.csv", "r")

    for line in file:
        line =line.rstrip('\n\r')
        fileData = line.split(';')
        print(fileData)
except:
    print("Erreur lors de la lecture du fichier")

