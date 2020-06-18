from pyGuix.guix import *
from simWorld import *
from signalEmiter import *
from soundProcessor import *
import os

if not os.path.exists("output_files"):
    os.mkdir("output_files")

sp = soundProcessor(60, "blop.wav")

window = Window((270, 480, 3))
slider = Slider([20, 100], 200, limits = [20, 500])
button = Button("Press", [20, 200], [100, 50])

window.addThing(slider)
window.addThing(button)

simWorld = SimWorld((1080, 1920, 3))

se1 = SignalEmiter((270, 180), simWorld, sp, 1, 200)
se2 = SignalEmiter((810, 180), simWorld, sp, 1, 200)
se3 = SignalEmiter((540, 540), simWorld, sp, 1, 50)

def buttonClick():
    se1.createSignals()
    button.color = button.getInverseColor()

button.onClick = buttonClick

while 1:
    key = cv2.waitKey(1)
    window.loop()
    simWorld.loop()
    se1.strength = slider.sliderPos
    if key == ord("q"):
        break

length = len(sp.srcAud)/1000
sp.save(simWorld.frame/60)
sp.combine("output_files/output.avi")
