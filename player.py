from vectorClass import Vector, findOrginial
import pygame

class Player:

    def __init__(self,pos,screen,color):
        self.color = color
        self.pos = pos
        self.screen = screen
        self.velocity_vector = Vector(0,0,0)
        self.scaleConstent = 2
        
        # laser variables
        self.posToShoot = 0
        self.counter = 0

        self.W_pressed = 0
        self.A_pressed = 0
        self.S_pressed = 0
        self.D_pressed = 0


    def move(self,keys_pressed):

        if keys_pressed[pygame.K_w] and not self.W_pressed: 
            self.velocity_vector += Vector(0,1,0).scaleVector(self.scaleConstent)
            self.W_pressed = 1
        elif not keys_pressed[pygame.K_w] and self.W_pressed:
            self.velocity_vector -= Vector(0,1,0).scaleVector(self.scaleConstent)
            self.W_pressed = 0
            

        if keys_pressed[pygame.K_a] and not self.A_pressed:
            self.velocity_vector += Vector(-1,0,0).scaleVector(self.scaleConstent)
            self.A_pressed = 1
        elif not keys_pressed[pygame.K_a] and self.A_pressed:
            self.velocity_vector -= Vector(-1,0,0).scaleVector(self.scaleConstent)
            self.A_pressed = 0

        if keys_pressed[pygame.K_s] and not self.S_pressed:
            self.velocity_vector += Vector(0,-1,0).scaleVector(self.scaleConstent)
            self.S_pressed = 1
        elif not keys_pressed[pygame.K_s] and self.S_pressed:
            self.velocity_vector -= Vector(0,-1,0).scaleVector(self.scaleConstent)
            self.S_pressed = 0

        if keys_pressed[pygame.K_d] and not self.D_pressed:
            self.velocity_vector += Vector(1,0,0).scaleVector(self.scaleConstent)
            self.D_pressed = 1
        elif not keys_pressed[pygame.K_d] and self.D_pressed:
            self.velocity_vector -= Vector(1,0,0).scaleVector(self.scaleConstent)
            self.D_pressed = 0

        if not (keys_pressed[pygame.K_d] or keys_pressed[pygame.K_s] or keys_pressed[pygame.K_a] or keys_pressed[pygame.K_w]) :
            self.velocity_vector = Vector(0,0,0)
            self.W_pressed = 0
            self.A_pressed = 0
            self.S_pressed = 0
            self.D_pressed = 0
        
        self.update()


    def laser(self):
        if pygame.mouse.get_pressed()[0] and self.counter  <= 0:
            self.posToShoot = pygame.mouse.get_pos() 
            self.counter = 100
        
        if self.counter > 0:
            self.counter -= 1
            pygame.draw.aaline(self.screen, self.color, self.pos, self.posToShoot)
                
    def update(self):        
        self.pos[0] += self.velocity_vector.x
        self.pos[1] += -self.velocity_vector.y

    def show(self):
        pygame.draw.circle(self.screen, self.color,(int(self.pos[0]),int(self.pos[1])),15)