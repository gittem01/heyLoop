import numpy as np
import cv2
import math
import random

from signalEmiter import *
from particle import *

class SignalEmiter:
    def __init__(self, pos, world, soundProcessor, freq=1, strength=100):
        self.pos = pos
        self.freq = freq
        self.strength = strength
        self.world = world
        self.sp = soundProcessor
        world.emiters.append(self)
        self.r = 10

        arr = np.zeros((self.r*2, self.r*2), dtype=np.uint8)
        cv2.circle(arr, (int(self.r), int(self.r)), self.r, 1, -1)
        self.mask = np.where(arr==1)
        self.done = False

    def update(self, frame, im, maskIm):
        chck = self.check(maskIm)
        if chck == True and self.done == False:
            self.createSignals()
        if chck:
            self.done = True
        else:
            self.done = False
        if frame % int(self.freq*60) == float("inf"):
            self.createSignals()
        self.draw(im, maskIm)

    def check(self, maskIm):
        m0 = self.mask[0]+self.pos[0]-self.r
        m1 = self.mask[1]+self.pos[1]-self.r
        values = maskIm[m1, m0]
        if np.any(values):
            return True
        return False

    def draw(self, im, maskIm):
        m0 = self.mask[0]+self.pos[0]-self.r
        m1 = self.mask[1]+self.pos[1]-self.r
        im[m1, m0] = (255, 255, 3)

    def createSignals(self):
        self.sp.put(self.world.frame)
        baseAngle  = random.random()*math.pi
        for i in range(int(self.strength)):
            angle = (i/self.strength)*2*math.pi + baseAngle
            speed = (math.cos(angle)*20, math.sin(angle)*20)
            pos = [self.pos[0]+speed[0]*self.r*1.5, self.pos[1]+speed[1]*self.r*1.5]
            particle = Particle(pos, speed, self.world)
