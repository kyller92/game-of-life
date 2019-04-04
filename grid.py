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
        for lon in range(self.longueur):
            for lar in range(self.largeur):
                #tab += "[{}, {}]".format(lon, lar)
                # ■
                
                tab += str(self.grille[lon][lar])
            tab += "\n"
        return tab

    def updateGrid(self, newPoint):
        print(len(self.grille))
        print(len(self.grille[0]))
        self.grille[int(newPoint[0][0])][int(newPoint[1][0])]="|■|"
        # self.grille[4][4]="|■|"

    def startPosition(self):
        numCarre = 1
        inputText = True
        while inputText:
            posLigne = input("\n Saisissez la ligne du carré N°{} / Saisir \"STOP \" pour arrêter \n\n".format(numCarre))
            posColonne = input("\n Saisissez la colonne du carré N°{} / Saisir \"STOP \" pour arrêter \n\n".format(numCarre))
            if(posColonne != "STOP" and posLigne != "STOP"):
                #test = [[posLigne],[posColonne]]
                #print (test)
                self.updateGrid([[posLigne],[posColonne]])
                print(self.showGrid())
                return
            else:
                return
            
                




