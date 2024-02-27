from PIL import Image, ImageGrab
import time
import pyautogui

def countdown(r:int):
    for i in reversed(range(r)):
        print(i)
        time.sleep(1)

# One tile up from Harp's click (see sample.png)
HARP_BOX = (835, 452, 1084, 485)

# [ScanPos, Color]
BOARD_POSITIONS = [
    [(17, 8), "de90a5"],
    [(52, 8), "aea32b"],
    [(88, 8), "45b23a"],
    [(124, 8), "394c1d"],
    [(160, 8), "8849c2"],
    [(197, 8), "323d9f"],
    [(233, 8), "4b66b8"]
]

countdown(5)

while True:
    img = ImageGrab.grab(HARP_BOX)
    detectedAbsPos = []
    for pos, color in BOARD_POSITIONS:
        rgb = img.getpixel(pos)
        if rgb == tuple((int(color[i:i+2], 16) for i in range(0, len(color), 2))):
            print(f"matched! color: #{color}/{pos}")
            print("moving cursor")
            pyautogui.moveTo(HARP_BOX[0]+pos[0], HARP_BOX[1]+51, 0.05)
            print("try to click")
            pyautogui.click()
    time.sleep(0.02)