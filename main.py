import pygame
import pyttsx3
from time import sleep

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


sleep(1)
window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play()
sleep(5)
pygame.mixer.music.load('scary.mp3')
pygame.mixer.music.play()
sleep(3)
img = pygame.image.load('scr.jpg')
up = img.get_rect()
window.blit(img, (0, 0))
pygame.display.update()
sleep(5)
