from pydub import AudioSegment
import os

class soundProcessor:
    def __init__(self, FPS, sourceAudio):
        self.fps = FPS
        self.sound = AudioSegment.silent(duration=FPS*5000)
        self.srcAud = AudioSegment.from_wav(f"./sound_files/{sourceAudio}")
        
    def put(self, frame):
        self.sound =  self.sound.overlay(self.srcAud, position=(frame/self.fps)*1000)

    def save(self, size=None):
        if size == None:
            self.sound.export("output_files/output_sound.wav", format="wav")
        else:
            self.sound = self.sound[:int(size*1000)]
            self.sound.export("output_files/output_sound.wav", format="wav")

    def combine(self, vidPos):
        os.system(f"ffmpeg -i {vidPos} -i output_files/output_sound.wav -c "+
                  "copy output_files/final_output.mkv -y")
