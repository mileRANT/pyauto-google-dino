import pyautogui 
from PIL import Image, ImageGrab 
import time


# basic function for clicking a key
def click(key):
   pyautogui.keyDown(key)
   return


if __name__ == "__main__":
    time.sleep(5)
    click('up')

    while True:  # for infinity loop
       # capture image in black & white format
       image = ImageGrab.grab().convert('L')
       data = image.load()

       # Draw the rectangle for cactus
       for i in range(740, 820):
          for j in range(395, 425):
             data[i, j] = 0

       # Draw the rectangle for birds
       for i in range(740, 770):
          for j in range(365, 390):
             data[i, j] = 171
       image.show()
       break

#
# def isCollision(data):
# # Check colison for birds
#     for i in range(530,560):
#         for j in range(80, 127):
#             if data[i, j] < 171:
#                 click("down")
#                 return
#  # Check colison for cactus
#     for i in range(530, 620):
#         for j in range(130, 160):
#             if data[i, j] < 100:
#                 click("up")
#                 return
#     return