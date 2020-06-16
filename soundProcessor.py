from pydub import AudioSegment
import os

class soundProcessor:
    def __init__(self, FPS, sourceAudio, isRealTime=False):
        self.fps = FPS
        self.sound = AudioSegment.silent(duration=FPS*5000)
        self.srcAud = AudioSegment.from_wav(f"./sound_files/{sourceAudio}")
        self.isRealTime = isRealTime # Overlays the sound at the end if True
        self.frames = []
        
    def put(self, frame):
        if self.isRealTime:
            self.sound = self.sound.overlay(self.srcAud, position=(frame/self.fps)*1000)
        else:
            self.frames.append(frame)

    def save(self, size=None):
        for i in range(len(self.frames)):
            self.sound = self.sound.overlay(self.srcAud,
                                            position=(self.frames[i]/self.fps)*1000)
            percentage = int((i/len(self.frames))*100)
            print("%" + str(percentage), end="\r")
        if size == None:
            self.sound.export("output_files/output_sound.wav", format="wav")
        else:
            self.sound = self.sound[:int(size*1000)]
            self.sound.export("output_files/output_sound.wav", format="wav")

    def combine(self, vidPos):
        os.system(f"ffmpeg -i {vidPos} -i output_files/output_sound.wav -c "+
                  "copy output_files/final_output.mkv -y")
