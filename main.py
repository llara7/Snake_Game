import math
import pygame
import random
import tkinter as tk
from tkinter import messagebox

class snake(object):
  def _init_(self, color, position):
    pass
  
  def move(self, position):
    pass
  
  def reset(self, position):
    pass

  def addCube(self):
    pass

  def draw(self, surface):
    pass


class cube(object):
  rows = 0
  w = 0
  def _init_(self, start, dirnx=1, dirny=0, color=(255,0,0)):
    pass
  def move(self, dirnx, dirny):
    pass
  def draw(self, surface, eyes=False):
    pass


def drawGrid(w, rows, surface):
  sizeBtwn = w // rows
  x = 0
  y = 0
  for 1 in range(rows):
    x = x + sizeBtwn
    y = y + sizeBtwn

    pygame.draw.line(surface,(255,255,255), (x,0), (x,w))
    pygame.draw.line(surface,(255,255,255), (0,y), (w,y))

  pass

def redrawWindow(surface):
  global rows, width
  surface.fill((0,0,0))
  drawGrid(width, rows, surface)
  pygame.display.update()
  pass

def randomSnack(rows, items):
  pass

def main():
  global width, rows 
  width = 500
  height = 500
  rows = 20
  win = pygame.display.set_mode((width, width))
  s = snake((255,0,0),(10,10))
  flag = True
  clock = pygame.time.Clock()
  while flag:
    pygame.time.delay(50)
    clock.tick(10)
    redrawWindow(win)
  pass

rows = 
w =
h =

cube.rows = rows
cube.w = w

main()
