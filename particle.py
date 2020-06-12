import cv2
import numpy as np

class Particle:
    def __init__(self, pos, speed):
        self.pos = pos
        self.speed = speed

    def update(self, frame, im, maskIm):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]
        self.draw(im, maskIm)
        
    def draw(self, im, maskIm):
        cv2.circle(im, (int(pos[0]), int(pos[1])), 2, (255, 255, 255), -1)
        maskIm[int(pos[1]), int(pos[0])] = True
