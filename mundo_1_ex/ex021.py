# Player de mp3
import pygame, time
pygame.init()

pygame.mixer.music.load('media/jdilla.mp3')
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():  # wait for music to finish playing
    time.sleep(1)

# from playsound import playsound
# playsound("media/jdilla.mp3")