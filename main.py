import math
import pygame
import random
import tkinter as tk
from tkinter import messagebox

class snake(object):
  body = []
  turns = {}
  def __init__(self, color, position):
        self.color = color
        self.head = cube(position)
        self.body.append(self.head)
        self.dirnx = 0
        self.dirny = 1
 
  def move(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
 
            keys = pygame.key.get_pressed()
 
            for key in keys:
                if keys[pygame.K_LEFT]:
                    self.dirnx = -1
                    self.dirny = 0
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_RIGHT]:
                    self.dirnx = 1
                    self.dirny = 0
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_UP]:
                    self.dirnx = 0
                    self.dirny = -1
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]
 
                elif keys[pygame.K_DOWN]:
                    self.dirnx = 0
                    self.dirny = 1
                    self.turns[self.head.position[:]] = [self.dirnx, self.dirny]
 
        for i, c in enumerate(self.body):
            p = c.position[:]
            if p in self.turns:
                turn = self.turns[p]
                c.move(turn[0],turn[1])
                if i == len(self.body)-1:
                    self.turns.pop(p)
            else:
                if c.dirnx == -1 and c.position[0] <= 0: c.position = (c.rows-1, c.position[1])
                elif c.dirnx == 1 and c.position[0] >= c.rows-1: c.position = (0,c.position[1])
                elif c.dirny == 1 and c.position[1] >= c.rows-1: c.position = (c.position[0], 0)
                elif c.dirny == -1 and c.position[1] <= 0: c.position = (c.position[0],c.rows-1)
                else: c.move(c.dirnx,c.dirny)
       
 
  def reset(self, position):
        self.head = cube(position)
        self.body = []
        self.body.append(self.head)
        self.turns = {}
        self.dirnx = 0
        self.dirny = 1
 
 
  def addCube(self):
        tail = self.body[-1]
        dx, dy = tail.dirnx, tail.dirny
 
        if dx == 1 and dy == 0:
            self.body.append(cube((tail.pos[0]-1,tail.position[1])))
        elif dx == -1 and dy == 0:
            self.body.append(cube((tail.pos[0]+1,tail.position[1])))
        elif dx == 0 and dy == 1:
            self.body.append(cube((tail.pos[0],tail.position[1]-1)))
        elif dx == 0 and dy == -1:
            self.body.append(cube((tail.pos[0],tail.position[1]+1)))
 
        self.body[-1].dirnx = dx
        self.body[-1].dirny = dy
       
 
  def draw(self, surface):
        for i, c in enumerate(self.body):
            if i ==0:
                c.draw(surface, True)
            else:
                c.draw(surface)


class cube(object):
  rows = 20
  w = 500
  def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        self.position = start
        self.dirnx = 1
        self.dirny = 0
        self.color = color
 
       
  def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.position = (self.position[0] + self.dirnx, self.position[1] + self.dirny)
 
  def draw(self, surface, eyes=False):
        dis = self.w // self.rows
        i = self.position[0]
        j = self.position[1]
 
        pygame.draw.rect(surface, self.color, (i*dis+1,j*dis+1, dis-2, dis-2))
        if eyes:
            centre = dis//2
            radius = 3
            circleMiddle = (i*dis+centre-radius,j*dis+8)
            circleMiddle2 = (i*dis + dis -radius*2, j*dis+8)
            pygame.draw.circle(surface, (0,0,0), circleMiddle, radius)
            pygame.draw.circle(surface, (0,0,0), circleMiddle2, radius)


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
  global rows, width, s, snack
  surface.fill((0,0,0))
  s.draw(surface)
  snack.draw(surface)
  drawGrid(width,rows, surface)
  pygame.display.update()

def randomSnack(rows, items):
  positions = item.body
 
  while True:
        x = random.randrange(rows)
        y = random.randrange(rows)
        if len(list(filter(lambda z:z.pos == (x,y), positions))) > 0:
            continue
        else:
            break
       
  return (x,y)


def message_box(subject, content):
    root = tk.Tk()
    root.attributes("-topmost", True)
    root.withdraw()
    messagebox.showinfo(subject, content)
    try:
        root.destroy()
    except:
        pass
 

def main():
  global width, rows, s, snack
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
    s.move()
    if s.body[0].position == snack.position:
      s.addCube()
      snack = cube(randomSnack(rows, s), color=(0,255,0))

    for x in range(len(s.body)):
      if s.body[x].position in list((map(lambda z:z.position,s.body[x+1:])):
        print(\'Score: \', len(s.body))
                message_box(\'You Lost!\', \'Play again...\')
                s.reset((10,10))
                break

    redrawWindow(win)
  pass



main()
