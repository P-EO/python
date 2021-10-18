userName = input ("Welcome, what is your name? ")
while userName != "Steve Rogers":
 print("You are not Captain America - please try again!")
 userName = input ("Welcome, waht is your name? ")
print("You are Captain America!")
date = input ("When were you born?")
while date !="17th 09 2010":
 print("Today ain't your birthday!")
 date = input ("When were you born?")
print("Happy early Birthday, Captain America!")
passcode = input ("Please type your passcode")
while passcode != "1976543" :
  print("Passcode incorrect please try again")
  passcode = input ("Please type your passcode")
import turtle
import random
pat = turtle.Turtle()
turtle.Screen().bgcolor("cyan")
colours = ["blue"]
pat.penup()
pat.forward(90)
pat.left(45)
pat.pendown()
def branch():
    for i in range(3):
        for i in range(3):
            pat.forward(30)
            pat.backward(30)
            pat.right(45)
        pat.left(90)
        pat.backward(30)
        pat.left(45)
    pat.right(90)
    pat.forward(90)
for i in range(8):
    branch()
    pat.left(45)
#    pat.color(random.choice(colours))
import pygame
from pygame.locals import *
from time import sleep
from random import randrange
pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height))
difference = pygame.image.load('spot_the_diff.png')
difference = pygame.transform.scale(difference, (width, height))
screen.blit(difference, (0, 0))
pygame.display.update()
zombie = pygame.image.load('scary_face.png')
zombie = pygame.transform.scale(zombie, (width, height))
scream = pygame.mixer.Sound('en_images_scream.wav')
sleep(randrange(5, 15))
scream.play()
sleep(0.4)
screen.blit(zombie, (0,0))
pygame.display.update()
sleep(3)
scream.stop()
pygame.quit()
feedback = input ("Please rate us!")
while feedback !="5":
 print("Quit already!")
 feedback = input("Please rate us!")
print("Thank you!")
