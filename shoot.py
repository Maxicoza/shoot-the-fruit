import pgzrun
from random import randint
import pygame
import sys
import os


startgame = False
game_over = False
apple = Actor("apple")
orange = Actor("orange")
score = 0


def draw():
    screen.fill("black")
    apple.draw()
    orange.draw()
    screen.draw.text("Score : " + str(score), color="green", topleft=(10, 10))

    if game_over:
        screen.fill("green")
        screen.draw.text("Final Score: " + str(score), topleft=(10, 10), fontsize=60)

        
def time_up():
    global game_over
    game_over = True
        
def place_orange():
    orange.x = randint(10, 800)
    orange.y = randint(10, 600)
       
            
def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)
                   
def on_mouse_down(pos):
    if apple.collidepoint(pos):
        global score
        print("Good shot!")
        score = score + 1
        screen.clear()
        place_apple()
        print("Your score is: ",score)
    elif orange.collidepoint(pos):
        print("Good shot!")
        score = score + 2
        screen.clear()
        place_orange()
        print("Your score is: ",score)
    else:
        score = score - 2
        print("You missed! Your score is now ",score)


clock.schedule(time_up, 15.0)
place_apple()
place_orange()
