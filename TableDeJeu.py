from VueBinaire import *
class TableDeJeu(VueBinaire):
    def __init__(self):
        super().__init__()

    def obtenir_gagnant_horiz(self):
        
        gagnant = ""
       
        L = 5
      
        arreter = False
    
        while L >= 0 and arreter == False:
            for c in range(4):  
                if self.grille[L][c] * self.grille[L][c + 1] * self.grille[L][c + 2] * \
                        self.grille[L][c + 3] == TableDeJeu.BLANC_GAGNE: 
                    
                    gagnant = "Blanc"
                    print(gagnant)
                    
                    arreter = True
                if self.grille[L][c] + self.grille[L][c + 1] + self.grille[L][c + 2] + \
                        self.grille[L][c + 3] == TableDeJeu.NOIR_GAGNE:  
                    gagnant = "Noir"
                    print(gagnant)
                    arreter = True
           
            L = L - 1
       
        return gagnant

    def obtenir_gagnant_vert(self):
        gagnant = ""
       
        for c in range(7):
            
            for L in range(5, 2, -1):
                if self.grille[L][c] * self.grille[L - 1][c] * self.grille[L - 2][c] * \
                        self.grille[L - 3][c] == TableDeJeu.BLANC_GAGNE:
                    gagnant = "Blanc"
                if self.grille[L][c] + self.grille[L - 1][c] + self.grille[L - 2][c] + \
                        self.grille[L - 3][c] == TableDeJeu.NOIR_GAGNE:
                    gagnant = "Noir"
        return gagnant

    def obtenir_gagnant_diag(self):
        gagnant = ""
      
        for L in range(3):
        
            for c in range(4):
              
                if self.grille[L][c] * self.grille[L + 1][c + 1] * self.grille[L + 2][c + 2] * \
                        self.grille[L + 3][c + 3] == TableDeJeu.BLANC_GAGNE:
                    gagnant = "Blanc"
                if self.grille[L][c] + self.grille[L + 1][c + 1] + self.grille[L + 2][c + 2] + \
                        self.grille[L + 3][c + 3] == TableDeJeu.NOIR_GAGNE:
                    gagnant = "Noir"
  
        for L in range(3):
         
            for c in range(3, 7):
        
                if self.grille[L][c] * self.grille[L + 1][c - 1] * self.grille[L + 2][c - 2] * \
                        self.grille[L + 3][c - 3] == TableDeJeu.BLANC_GAGNE:
                    gagnant = "Blanc"
                if self.grille[L][c] + self.grille[L + 1][c - 1] + self.grille[L + 2][c - 2] + \
                        self.grille[L + 3][c - 3] == TableDeJeu.NOIR_GAGNE:
                    gagnant = "Noir"
        return gagnant
    
    
    
    def obtenir_gagnant(self):
        
        player = self.obtenir_gagnant_horiz()
      
        if player != "":
            return player
        player = self.obtenir_gagnant_vert()
        if player != "":
            return player
        player = self.obtenir_gagnant_diag()
        if player != "":
            return player

    def mettre_jeton(self, c, player):
       
        L = 5  
      
        arreter = False
        while L >= 0 and arreter == False:
            
            if self.grille[L][c] == 0:
                if player == TableDeJeu.JETON_BLANC:
                 
                    self.grille[L][c] = TableDeJeu.JETON_BLANC
                 
                    arreter = True
                else:
                    self.grille[L][c] = TableDeJeu.JETON_NOIR
                    arreter = True
         
            L = L - 1  

