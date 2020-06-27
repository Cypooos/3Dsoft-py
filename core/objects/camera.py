import pygame
import math



class Camera():
  
  verts = []
  faces = []
  colors = []

  def __init__(self):
    self.pos = [0,0,0]
    self.rot = [0,0]
    self.fov = 200
    self.movement_speed = 3
    self.sensitive = 30
    self.events = {"OnKey":self.onKey,"OnMouseMove":self.onMove}

  def onKey(self,dt,key):
    s=dt*self.movement_speed
    if key[pygame.K_q]: self.pos[1] -=s
    if key[pygame.K_e]: self.pos[1] +=s

    x,y = s*math.sin(self.rot[1]),s*math.cos(self.rot[1])

    if key[pygame.K_w]: self.pos[0] +=x;self.pos[2] +=y;
    if key[pygame.K_s]: self.pos[0] -=x;self.pos[2] -=y;
    if key[pygame.K_a]: self.pos[0] -=y;self.pos[2] +=x;
    if key[pygame.K_d]: self.pos[0] +=y;self.pos[2] -=x;

  def onMove(self,dt,move):
    x,y = move
    x/=self.sensitive; y/=self.sensitive
    self.rot[0]+=y;self.rot[1]+=x