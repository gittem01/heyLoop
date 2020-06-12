import cv2

class Slider:
    def __init__(self, pos, size, rotation=0, limits=(0, 100)):
        self.pos = pos
        self.size = size
        self.rotation = rotation # 0 for horizontal 1 for vertical
        self.limits = limits
        self.sliderPos = limits[0]
        self.color = (0, 255, 255)
        self.limitSize = abs(limits[1] - limits[0])
        self.mp = [0, 0]
        self.startPos = [0, 0]
        self.status = False
        if limits[1] < limits[0]: self.direction = -1
        else: self.direction = 1

    def set(self, uid, mp):
        self.uId = uid
        self.mp = mp

    def checkSliderPos(self):
        if self.sliderPos < min(self.limits):
            self.sliderPos = min(self.limits)
        elif self.sliderPos > max(self.limits):
            self.sliderPos = max(self.limits)

    def move(self, pb, pn):
        diff = [0, 0]
        diff[0] = pn[0] - pb[0]
        diff[1] = pn[1] - pb[1]
        val0 = diff[0] * (1 - self.rotation)
        val0 += diff[1] * self.rotation
        mult = self.size/self.limitSize
        self.sliderPos+=val0/mult
        self.checkSliderPos()

    def followMouse(self):
        relativePos = [self.mp[0]-self.pos[0], self.mp[1]-self.pos[1]]
        mult = self.size / self.limitSize * self.direction
        val = relativePos[0]*(1-self.rotation)
        val += relativePos[1]*self.rotation
        self.sliderPos = (val/mult + self.limits[0])
        self.checkSliderPos()

    def onClick(self):
        self.color = (255, 255, 255)
        self.status = True
        self.startPos = self.mp.copy()

    def onRelease(self):
        self.color = (0, 255, 255)
        self.status = False

    def update(self, im, thingMap):
        if self.status:
            self.followMouse()
            #self.move(self.startPos, self.mp)
            #self.startPos = self.mp.copy()

        self.draw(im, thingMap)

    def draw(self, im, thingMap):
        im[ self.pos[1]:self.pos[1]+self.size*self.rotation+1,
            self.pos[0]:self.pos[0]+self.size*(1-self.rotation)+1] = (255, 255, 255)
        floatPos = (self.sliderPos - self.limits[0])/self.limitSize*self.direction
        cv2.circle(im, (int(self.pos[0]+self.size*(1-self.rotation)*floatPos),
                        int(self.pos[1]+self.size*self.rotation*floatPos)),
                   int(self.size/20), self.color, -1, lineType=cv2.LINE_AA)
        cv2.circle(thingMap, (int(self.pos[0] + self.size * (1 - self.rotation) * floatPos),
                        int(self.pos[1] + self.size * self.rotation * floatPos)),
                   int(self.size / 20), self.uId, -1)