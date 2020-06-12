import cv2
import numpy as np

class SimWorld:
    def __init__(self, size):
        self.size = size
        self.winName = "SimWorld"
        self.baseIm = np.zeros(size, dtype=np.uint8)
        self.maskArr = np.zeros((size[0], size[1]), dtype=np.bool)
        self.emiters = []
        self.things = []
        self.frame = 0

    def loop(self, key=None):
        self.frame+=1
        copIm = self.baseIm.copy()
        copMask = self.maskArr.copy()
        for thing in self.things:
            thing.update(self.frame, copIm, copMask)
        for emiter in self.emiters:
            emiter.update(self.frame, copIm, copMask)
        cv2.imshow(self.winName, copIm)
