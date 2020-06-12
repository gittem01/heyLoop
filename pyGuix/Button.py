import cv2

class Button:
    def __init__(self, title, pos: """np array(x, y)""",
                             size: """np array(w, h)"""):

        self.title = title
        self.pos = pos
        self.size = size
        self.connections = [] # Sliders, tick boxes, text boxes etc
        self.color = (255, 0, 0)
        self.mp = [-999, -999]

    def set(self, uid, mp):
        self.uId = uid
        self.mp = mp

    def addConnection(self, c):
        self.connections.append(c)

    def setOnClickFunc(self, func):
        self.onClick = func

    def onClick(self):
        self.color = self.getInverseColor()
        for obj in self.connections:
            print(obj.sliderPos)

    def onRelease(self):
        self.color = self.getInverseColor()

    def update(self, im, thingMap):
        self.draw(im, thingMap)

    def getInverseColor(self):
        return 255 - self.color[0], 255 - self.color[1], 255 - self.color[2]

    def draw(self, im, thingMap):
        im[self.pos[1]: self.pos[1]+self.size[1],
            self.pos[0]: self.pos[0]+self.size[0]] = self.color

        thingMap[self.pos[1]: self.pos[1]+self.size[1],
                  self.pos[0]: self.pos[0]+self.size[0]] = self.uId

        scale = cv2.getFontScaleFromHeight(cv2.FONT_HERSHEY_SIMPLEX, int(self.size[1]/2), 1)
        cv2.putText(im, self.title, (self.pos[0], self.pos[1]+int(self.size[1]*0.75)),
            cv2.FONT_HERSHEY_SIMPLEX, scale, self.getInverseColor(), 1, lineType=cv2.LINE_AA)
