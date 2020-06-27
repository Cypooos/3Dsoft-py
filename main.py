"""import pygame,math,sys
movement_speed = 10
sensitive = 200
color = (255,0,0),(255,128,0),(255,255,0),(255,255,255),(0,0,255),(0,255,0)

def rotate2d(pos,rad): x,y = pos;  s,c = math.sin(rad),math.cos(rad); return x*c-y*s,y*c+x*s

class Cam():

    def __init__(self,pos=(0,0,0),rot=(0,0)):
        self.pos = list(pos)
        self.rot = list(rot)

    def events(self,event):
        if event.type == pygame.MOUSEMOTION:
            x,y = event.rel; x/=sensitive; y/=sensitive
            self.rot[0]+=y;self.rot[1]+=x

    def update(self,dt,key):
        s=dt*movement_speed
        if key[pygame.K_q]: self.pos[1] -=s
        if key[pygame.K_e]: self.pos[1] +=s

        x,y = s*math.sin(self.rot[1]),s*math.cos(self.rot[1])

        if key[pygame.K_w]: self.pos[0] +=x;self.pos[2] +=y;
        if key[pygame.K_s]: self.pos[0] -=x;self.pos[2] -=y;
        if key[pygame.K_a]: self.pos[0] -=y;self.pos[2] +=x;
        if key[pygame.K_d]: self.pos[0] +=y;self.pos[2] -=x;
pygame.init()
w,h = 400,400; cx,cy = w//2,h//2
screen = pygame.display.set_mode((w,h))
clock = pygame.time.Clock()

verts = (-1,-1,-1),(1,-1,-1),(1,1,-1),(-1,1,-1),(-1,-1,1),(1,-1,1),(1,1,1),(-1,1,1)
#edges = (0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),(0,4),(1,5),(2,6),(3,7)
faces = (0,1,2,3),(4,5,6,7),(0,1,5,4),(2,3,7,6),(0,3,7,4),(1,2,6,5)
cam = Cam((0,0,-5))

pygame.event.get(); pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygaqame.event.set_grab(1)

while True:

    dt = clock.tick()/1000
    print(dt)

    for event in pygame.event.get():
        if event.type==pygame.QUIT: pygame.quit(); sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()
        cam.events(event)

    screen.fill((100,10,255))

    vert_list = []; screen_coords = []

    for x,y,z in verts:
        x -=cam.pos[0];y -=cam.pos[1];z -=cam.pos[2]
        x,z = rotate2d((x,z),cam.rot[1]);y,z = rotate2d((y,z),cam.rot[0])
        vert_list += [(x,y,z)]
        f=200/z
        x,y = x*f,y*f
        screen_coords.append((cx+int(x),cy+int(y)))
        pygame.draw.circle(screen,(0,0,0),(cx+int(x),cy+int(y)),5)
    face_list = [];face_color = [];depth = []

    for f in range(len(faces)):
        face = faces[f]
        on_screen = False
        for i in face:
            if vert_list[i][2]>0:
                on_screen=True; break
        if on_screen:
            coords = [screen_coords[i] for i in face]
            face_list += [coords]
            face_color += [color[f]]
            depth += [sum(sum(vert_list[j][i] for j in face)**2 for i in range(3))]

    order = sorted(range(len(face_list)),key = lambda i:depth[i],reverse=True)

    for i in order:
        pygame.draw.polygon(screen,face_color[i],face_list[i])






    pygame.display.flip()

    key = pygame.key.get_pressed()
    cam.update(dt,key)"""

import pygame,math,sys
from core.sceneManagement import Scene
from core.objects.cube import Cube 
from core.objects.camera import Camera

pygame.event.get(); pygame.mouse.get_rel()
pygame.mouse.set_visible(0); pygame.event.set_grab(1)

scene = Scene()

cam = Camera()
cube = Cube()

scene.addObj(cam,(0,0,0),"CAMERA")
scene.addObj(cube,(0,0,0),"cube1")
scene.addObj(cube,(0,3,0),"cube1")


scene.play()