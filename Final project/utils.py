import numpy as np
from collections import deque
import pygame
import pyttsx3

# -------------------------------
# 1. Calculate angle between joints
# -------------------------------
def calculate_angle(a, b, c):
    a = np.array(a)
    b = np.array(b)
    c = np.array(c)

    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - \
              np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)

    if angle > 180.0:
        angle = 360 - angle

    return angle

# -------------------------------
# 2. Rep counter class
# -------------------------------
class RepCounter:
    def __init__(self, up_angle_thresh, down_angle_thresh):
        self.counter = 0
        self.stage = None
        self.up_thresh = up_angle_thresh
        self.down_thresh = down_angle_thresh

    def update(self, angle):
        if angle > self.up_thresh:
            self.stage = "down"
        if angle < self.down_thresh and self.stage == "down":
            self.stage = "up"
            self.counter += 1
        return self.counter, self.stage

# -------------------------------
# 3. Angle smoother
# -------------------------------
class AngleSmoother:
    def __init__(self, max_len=5):
        self.values = deque(maxlen=max_len)

    def smooth(self, angle):
        self.values.append(angle)
        return sum(self.values) / len(self.values)

# -------------------------------
# 4. Voice feedback
# -------------------------------
tts_engine = pyttsx3.init()
tts_engine.setProperty('rate', 140)  # Speed of voice

def speak(text):
    try:
        tts_engine.say(text)
        tts_engine.runAndWait()
    except Exception as e:
        print("Voice error:", e)

# -------------------------------
# 5. Optional beep fallback using pygame
# -------------------------------
def play_beep():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("beep.wav")
        pygame.mixer.music.play()
    except Exception as e:
        print("Beep sound error:", e)
