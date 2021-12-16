# Faça um programa em python que abra e reproduza o áudio de um arquivo mp3

import time
import pygame
pygame.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
time.sleep(60)