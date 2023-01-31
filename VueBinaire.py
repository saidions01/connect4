
class VueBinaire():
    VIDE = 0
    JETON_NOIR = 2
    JETON_BLANC = 1
    BLANC_GAGNE = 1
    NOIR_GAGNE = 8

    def __init__(self):
        self.grille = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]
        ]
 
    def renverser_grille(self):
       
        grille_renversée = []
        for row in range(5, -1, -1):
            grille_renversée.append(self.grille[row])
        return grille_renversée

    def Afficher(self):
        print("\n")
        for i in range(len(self.grille)):
            for j in range(len(self.grille[i])):
                print(self.grille[i][j], end=' ')
            print()
        print("\n")