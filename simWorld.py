import cv2
import numpy as np

class SimWorld:
    def __init__(self, size):
        self.size = size
        self.winName = "SimWorld"
        self.baseIm = np.zeros(size, dtype=np.uint8)
        self.maskArr = np.zeros((size[0], size[1]), dtype=np.bool)
        self.things = []

    def loop(self, key=None):
        copIm = self.baseIm.copy()
        for thing in things:
            thing.update()
        cv2.imshow(self.winName, copIm)
