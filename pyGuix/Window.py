import cv2
import numpy as np
import random
from .CalcFps import *
from .Button import *
from .Slider import *

class Window:
    def __init__(self, size, winName="Window"):
        self.size = size
        self.idCounter = 1
        self.winName = winName
        self.fpsThing = CalcFps(True, 90)
        self.call = False
        self.stat = [0, 0]
        self.lastMp = [0, 0]
        self.things = []
        self.im = arr = np.zeros(size, dtype=np.uint8)
        self.map = np.zeros((size[0], size[1]), dtype=np.uint8)
        self.clickedObject = None
        self.loopCounter = 0
        cv2.namedWindow(winName)
        cv2.setMouseCallback(winName, self.mouseCallbackFunction)
        cv2.imshow(self.winName, self.im)

    def addThing(self, thing):
        self.things.append(thing)
        thing.set(self.idCounter, self.lastMp)
        self.idCounter += 1

    def mouseCallbackFunction(self, type, x, y, u2, u3):
        self.call = True
        self.stat = [type, u2]
        self.lastMp[0] = x; self.lastMp[1] = y
        if type == cv2.EVENT_LBUTTONDOWN and self.map[y, x] > 0:
            self.clickedObject = self.things[self.map[y, x]-1]
            self.clickedObject.onClick()
        elif type == cv2.EVENT_LBUTTONUP and self.clickedObject != None:
            self.clickedObject.onRelease()
            self.drawF()
            self.clickedObject = None
        elif type == cv2.EVENT_MBUTTONDOWN:
            btn = Button("Title", np.array((x, y)), np.array((400, 200)))
            self.addThing(btn)

    def showFps(self, arrC):
        scale = cv2.getFontScaleFromHeight(cv2.FONT_HERSHEY_SIMPLEX, 100, 1)
        cv2.putText(arrC, str(self.fpsThing.getDiff(1)), (0, 100), cv2.FONT_HERSHEY_SIMPLEX,
                    scale, (0, 255, 255), 2, lineType=cv2.LINE_AA)

    def drawF(self):
        self.call = False
        arrC = self.im.copy()
        self.map = np.zeros_like(self.map)
        for thing in self.things:
            thing.update(arrC, self.map)
        cv2.imshow(self.winName, arrC)

    def loop(self, key=None):
        self.loopCounter += 1

        if key == ord("q"):
            return "quit"

        if (not self.stat.__eq__([0, 0]) and self.call) or self.loopCounter == 1:
            self.drawF()
