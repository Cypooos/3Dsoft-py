import sys, random
import pygame

from core.renderer import Renderer

ren = Renderer()

class SceneError(Exception):
  pass
  """When a error in a custom script is made."""

class Scene():

  def __init__(self):
    self.renderer = Renderer
    self.objs = {}
    self.events = {
      "OnDraw":{},
      "OnMouseMove":{},
      "OnKey":{},
      "OnQuit":{}
    }

  def addObj(self,obj,pos,name):
    obj.verts = [(x+pos[0],y+pos[1],z+pos[2]) for x,y,z in obj.verts]
    self.objs[name] = obj
    print(obj.events)
    for key,value in obj.events.items():
      self.addEvent(key,value,"auto-"+key+"-"+obj.__class__.__name__+str(random.randint(100000,999999)))

  def addEvent(self,event,function,name):
    if not event in self.events.keys(): raise SceneError("No events called '"+str(event)+"'")
    self.events[event][name] = function

  def remEvent(self,name):
    for x in self.events.keys():
      del self.events[x][name]

  def play(self):
    pygame.init()
    self.clock = pygame.time.Clock()
    self.renderer = self.renderer()
    while True:
      dt = self.clock.tick()/1000
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          for x in self.events["OnQuit"].values():
            x(dt)
        if event.type==pygame.KEYDOWN:
          if event.key == pygame.K_ESCAPE: break
        if event.type == pygame.MOUSEMOTION:
          for x in self.events["OnMouseMove"].values():
            x(dt,event.rel)
      key = pygame.key.get_pressed()
      for x in self.events["OnKey"].values():
        x(dt,key)

      self.renderer.render(self)