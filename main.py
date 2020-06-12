from pyGuix.guix import *
from simWorld import *
from signalEmiter import *

window = Window((270, 480, 3))
slider = Slider([20, 100], 200, limits = [20, 500])
button = Button("Press", [20, 200], [100, 50])

window.addThing(slider)
window.addThing(button)

simWorld = SimWorld((720, 1080, 3))

se1 = SignalEmiter((270, 180), simWorld, 1, 50)
se2 = SignalEmiter((810, 180), simWorld, 1, 50)
se3 = SignalEmiter((540, 540), simWorld, 1, 50)


button.onClick = se1.createSignals

while 1:
    key = cv2.waitKey(1)
    window.loop()
    simWorld.loop()
    se1.strength = slider.sliderPos
    if key == ord("q"):
        break
