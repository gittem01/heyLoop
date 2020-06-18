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
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        fps = 60
        self.writer = cv2.VideoWriter('output_files/output.avi',fourcc, fps, (size[1], size[0]))


    def loop(self, key=None):
        self.frame+=1
        copIm = self.baseIm.copy()
        copMask = self.maskArr.copy()
        willRemoved = []
        for i in range(len(self.things)):
            if self.things[i].update(self.frame, copIm, copMask):
                willRemoved.append(i)
        val = 0
        for i in willRemoved:
            self.things.pop(i-val)
            val += 1

        for emiter in self.emiters:
            emiter.update(self.frame, copIm, copMask)
        cv2.imshow(self.winName, copIm)
        self.writer.write(copIm)
