import sys
import time

from VueGraphique import *


class Jeu:
    NBR_Jetons = 42

    def __init__(self):
        self.joueur = 1
        self.jetons_joués = 0
        self.gagnantpossib = False
        self.VueJeu = VueGraphique()

    def obt_player(self):
        
        if self.jetons_joués % 2 == 0:
            id_player = 1
        else:
            id_player = 2
        return id_player

    def Afficher_gagnant(self):
        if self.player == "" or self.player is None:
            return "personne n'a gagne"
        else:
            return self.player + " a gagne"

    def Jouer(self):
        self.VueJeu.tabJeu.Afficher()
        while self.gagnantpossib != "Blanc" \
                and self.gagnantpossib != "Noir" \
                and self.jetons_joués < Jeu.NBR_Jetons:
            

           
                    
            for event in self.VueJeu.pyGame.event.get():

                


                if event.type == self.VueJeu.pyGame.MOUSEBUTTONUP:
                    x, y = self.VueJeu.pyGame.mouse.get_pos()
                    player = self.obt_player()
                    c = self.VueJeu.determiner_colonne(x)
                    
                    self.VueJeu.tabJeu.mettre_jeton(c, player)
                    self.VueJeu.tabJeu.Afficher()
                    self.jetons_joués = self.jetons_joués + 1
                    self.gagnantpossib = self.VueJeu.tabJeu.obtenir_gagnant()
                    if self.gagnantpossib != None:
                       print("GAGNANT ? : " + str(self.gagnantpossib))
                       self.VueJeu.afficher_gagnant(self.gagnantpossib)
                    self.VueJeu.render()
                    self.VueJeu.pyGame.display.flip()

                if event.type == self.VueJeu.pyGame.QUIT:
                    sys.exit(0)