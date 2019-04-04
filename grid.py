class Grid:
    grille = []
    longueur = 20
    largeur = 20
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.grille = [["| |".format(x,y) for x in range(self.longueur)] for y in range(self.largeur)] 
        # for lon in range(longueur):
        #     for lar in range(largeur):
        #         # ■
        #         self.grille.insert([lon][lar], "X")

    def showGrid(self):
        tab = ""
        for lon in range(self.longueur+1):
            for lar in range(self.largeur+1):
                #tab += "[{}, {}]".format(lon, lar)
                # ■
                if(lon==0):
                    tab += "|"+str(lar)+"|"
                elif(lar==0):
                    tab += "|"+str(lon)+"|"
                else:
                    tab += str(self.grille[lon-1][lar-1])
            tab += "\n"
        return tab

    def updateGrid(self, newPoint):
        # print(len(self.grille))
        # print(len(self.grille[0]))
        if(self.grille[int(newPoint[0][0])][int(newPoint[1][0])]!="|■|"):
            self.grille[int(newPoint[0][0])-1][int(newPoint[1][0])-1]="|■|"
        else:
            print ("\n ------------------------ \n ERREUR : Cette case est déjà remplie \n ------------------------ \n")
        
        # self.grille[4][4]="|■|"

    def startPosition(self):
        numCarre = 1
        inputText = True
        while inputText:
            posLigne = input("\n Saisissez la ligne du carré N°{} / Saisir \"STOP\" pour arrêter \n".format(numCarre))
            posColonne = input("\n Saisissez la colonne du carré N°{} / Saisir \"STOP\" pour arrêter \n".format(numCarre))
            if(posColonne != "STOP" and posLigne != "STOP"):
                #test = [[posLigne],[posColonne]]
                #print (test)
                self.updateGrid([[posLigne],[posColonne]])
                print(self.showGrid())
                numCarre += 1
            else:
                return

    def countDemons(self, point):
        voisins=""
        try:
            voisins += self.grille[int(point[0][0])-1][int(point[1][0])-1]
        except:
            pass
        try:
            voisins += self.grille[int(point[0][0])-1][int(point[1][0])]
        except:
            pass
        try:
            voisins += self.grille[int(point[0][0])-1][int(point[1][0])+1]
        except:
            pass
        try:
            voisins += self.grille[int(point[0][0])][int(point[1][0])-1]
        except:
            pass
        try:
            voisins += self.grille[int(point[0][0])][int(point[1][0])]
        except:
            pass
        try:
            voisins += self.grille[int(point[0][0])][int(point[1][0])+1]
        except:
            pass
        try:
            voisins += self.grille[int(point[0][0])+1][int(point[1][0])-1]
        except:
            pass
        try:
            voisins += self.grille[int(point[0][0])+1][int(point[1][0])]
        except:
            pass
        try:
            voisins += self.grille[int(point[0][0])+1][int(point[1][0])+1]
        except:
            pass
        # print(voisins)
        if(len(voisins)==2 or len(voisins)==3):
            self.grille[int(point[0][0])-1][int(point[1][0])-1]="|■|"
        else:
            self.grille[int(point[0][0])-1][int(point[1][0])-1]="| |"

            
    def launchGame(self):
        while True:
            for lon in range(self.longueur):
                for lar in range(self.largeur):
                    self.countDemons([[lon],[lar]])
            print(self.showGrid())
            
            

                    




