from pyGuix.guix import *
from simWorld import *

window = Window((270, 480, 3))
slider = Slider([20, 100], 200)
window.addThing(slider)

simWorld = SimWorld((480, 720, 3))

while 1:
    key = cv2.waitKey(1)
    window.loop()
    simWorld.loop()
    if key == ord("q"):
        break
