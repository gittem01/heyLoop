import time

class CalcFps:
    def __init__(self, sync_enabled, fps):
        self.t1 = time.time()
        self.t2 = None
        self.diff = 0
        self.sync_enabled = sync_enabled
        self.fps = fps

    def loopBegin(self):
        self.t1 = time.time()

    def getFps(self):
        rDiff = None
        if self.t2 != None:
            rDiff = 1/(time.time() - self.t2)
        self.t2 = time.time()
        return rDiff

    def loopEnd(self):
        diff0 = time.time() - self.t1
        if self.sync_enabled:
            spf = 1 / (self.fps+self.fps/60)
            if (diff0 < spf):
                time.sleep(spf - diff0)
        self.diff = time.time() - self.t1

    def getDiff(self, type):
        """
        :param type: 0 or 1 if it is zero just returns self.diff otherwise
                returns 1/self.diff
        :return:
        """
        if type == 0:
            return self.diff
        elif type == 1 and self.diff != 0:
            return int(1 / self.diff)
        else: return 60