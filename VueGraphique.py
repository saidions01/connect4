import os

import pygame

from TableDeJeu import *
from VueBinaire import *



class VueGraphique():

    def __init__(self):
        self.player = 1
        self.tabJeu = TableDeJeu()
        self.pyGame = pygame

     
        pygame.init()
        size = (800, 600)
        screen = pygame.display.set_mode(size)
        
        self.image = pygame.image.load("background image.jpg")

      
        taille_plateau_de_jeu = self.image.get_size()
       
        self.size = (taille_plateau_de_jeu[0] * 1, taille_plateau_de_jeu[1])
        self.background = pygame.image.load("finalbackground.jpg")
        self.background = pygame.transform.scale(self.background,self.size)        
       
        self.screen = pygame.display.set_mode(self.size)
        self.screen.blit(self.image, (0, 0))
        pygame.display.flip()

        
        self.jetonBlanc = pygame.image.load("PionBlanc.png")
    
        self.jetonNoir = pygame.image.load("Pion-noir.png")
      
        self.font = pygame.font.Font("freesansbold.ttf", 15)

    def determiner_colonne(self, x):
     

        c = x - 16
        c = c / 97
        if c in range(0, 7):
            if self.tabJeu.grille[5][int(c)] == 0:
                etat_grille_jeu = False
        return int(c)

    def render(self):
      
        self.screen.fill((0, 0, 0))
        
        self.screen.blit(self.image, (0, 0))

        grille_jeu = self.tabJeu.renverser_grille()

       
        

        for i in range(len(grille_jeu)):
            for j in range(len(grille_jeu[i])):
               
                if grille_jeu[i][j] == TableDeJeu.JETON_BLANC:
                    
                    self.screen.blit(self.jetonBlanc, (16 + 97 * j, 13 - 97.5 * i + 486))
                pygame.display.flip()
            
                if grille_jeu[i][j] == TableDeJeu.JETON_NOIR:
                   
                    self.screen.blit(self.jetonNoir, (16 + 97 * j, 13 - 97.5 * i + 486))
                pygame.display.flip()
    
    def afficher_gagnant(self,gagnant):
        text = pygame.font.SysFont("Small fonts",50).render(f"Le gagnant est le {gagnant}",True,"white")
        rect = text.get_rect(center=(self.size[0]/2,self.size[1]/2))
        run=True
        while run== True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.screen.fill((0,0,0))
            self.screen.blit(self.background,(0,0))
            self.screen.blit(text,rect) 
            pygame.display.flip()       