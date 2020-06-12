import cv2
import numpy as np

class Particle:
    def __init__(self, pos, speed, world):
        self.pos = pos
        self.speed = speed
        self.world = world
        self.world.things.append(self)

    def update(self, frame, im, maskIm):
        self.pos[0] += self.speed[0]
        self.pos[1] += self.speed[1]

        if self.pos[0] < 0 or self.pos[0] >= im.shape[1] or self.pos[1] < 0 or self.pos[1] >= im.shape[0]:
            self.world.things.remove(self)
            return
        self.draw(im, maskIm)

    def draw(self, im, maskIm):
        cv2.circle(im, (int(self.pos[0]), int(self.pos[1])), 1, (255, 255, 255), -1)
        maskIm[int(self.pos[1]), int(self.pos[0])] = True
