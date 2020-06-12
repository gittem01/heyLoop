from Window import *


window = Window((900, 1600, 3))

bt = Button("buttonX", np.array((200, 200)), np.array((150, 50)))
window.addThing(bt)

sl = Slider((500, 500), 200, 1, (32, -232))
window.addThing(sl)

bt.addConnection(sl)

while 1:
    key = cv2.waitKey(1)
    stat = window.loop(key)
    if (stat == "quit"):
        break
cv2.destroyAllWindows()
exit(1)
