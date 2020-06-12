import numpy as np
import cv2
from signalEmiter import *
from particle import *

class SignalEmiter:
    def __init__(self, pos, world, freq=1, strength=100):
        self.pos = pos
        self.freq = freq
        self.strength = strength
        self.world = world
        self.r = 5

        arr = np.zeros((self.r*2, self.r*2), dtype=np.uint8)
        cv2.circle(arr, (int(self.r), int(self.r)), self.r, 1, -1)
        print(np.where(arr==1))

    def update(self, frame, im):
        if frame % 60 == 0:
            self.createSignals()

    def draw(self, im):
        pass

    def createSignals(self):
        for i in range(self.strength):
            angle = (i/self.strength)*2*np.pi
            speed = (np.sin(angle), np.cos(angle))
            pos = [self.pos[0]+speed[0]*3, self.pos[1]+speed[1]*3]
            particle = Particle(pos, speed)
            self.world.things.append(particle)
