import pygame
from vectorClass import Vector
import numpy as np

rotationMatrix = lambda angle: np.array([[np.cos(angle), -np.sin(angle)],
                                         [np.sin(angle),  np.cos(angle)]])

class Polygon:

    def __init__(self, screen, cords):
        self.screen = screen
        self.mass = 2
        self.velocityVector = Vector(0,0,0)
        self.cords = cords
        self.center = self.findCenter(cords)
        self.originCords = self.findOriginCords(self.cords)

    def findCenter(self, cords):
        center = [0,0]

        for i in cords:
            center[0] += i[0]
            center[1] += i[1]

        center[0] = center[0]/len(cords)
        center[1] = center[1]/len(cords)

        return center

    def findOriginCords(self, transCords):
        # Vs will hold the vectors for the given coordinates and get the original Polygon points where it is centred around the origin
        # and store them in Xs
        Vs = []
        Xs = []
        centerVector = Vector(self.center[0],self.center[1],0)
        for i in transCords:
            Vs.append(Vector(i[0],i[1],0))

        for i in range(len(transCords)):
            Xs.append(Vs[i]-centerVector)

        for i in range(len(Xs)):
            Xs[i] = Xs[i].arr2d()
        
        return Xs

    def rotate(self, angularVeolcity):
        # rotate around the origin
        toRotate = rotationMatrix(angularVeolcity)
        for i in range(len(self.originCords)):
            newCord = toRotate.dot(self.originCords[i])
            self.originCords[i][0], self.originCords[i][1] = newCord[0], newCord[1]

        # translate it back to the center
        self.center = self.findCenter(self.cords)
        centerVector = Vector(self.center[0],self.center[1],0)
        Xs = []
        Vs = []
        for i in self.originCords:
            Xs.append(Vector(i[0],i[1],0))
        
        for i in range(len(self.cords)):
            Vs.append((Xs[i]+centerVector).arr2d())

        self.cords = Vs

    def applyForces(self, forces):
        # Apply the forces in the Forces array passed as [x-comp of force, y-comp of force]
        for i in forces:
            self.velocityVector.x += i[0]/self.mass
            self.velocityVector.y += i[1]/self.mass
        
        self.center[0] += self.velocityVector.x
        self.center[1] += -self.velocityVector.y
            
        for i in range(len(self.cords)):
            self.cords[i][0] += self.velocityVector.x
            self.cords[i][1] += -self.velocityVector.y
        
    def show(self):
        self.applyForces([[0.001,-0.01]])
        pygame.draw.polygon(self.screen, (228, 235, 27), self.cords)


        # pygame.draw.polygon(self.screen, (228, 235, 27), self.originCords)
        # pygame.draw.aaline(self.screen, (228, 160, 27), [0,0], self.center)
