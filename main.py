import pyautogui 
from PIL import Image, ImageGrab 
import time
import webbrowser


# basic function for clicking a key
def click(key):
   pyautogui.keyDown(key)
   return


def isCollision(data):
# # Check colison for birds
   for i in range(760, 790):
      for j in range(365, 390):
            if data[i, j] < 171:
                click("down")
                return
   # Check colison for cactus
   for i in range(760, 840):
      for j in range(395, 425):
            if data[i, j] < 100:
                click("up")
                return
   return

# this code was to show us the hit boxes. upon confirming the hitboxes are in the correct area,
# we set it up in the iscollision method
#    while True:  # for infinity loop
#       # capture image in black & white format
#       image = ImageGrab.grab().convert('L')
#       data = image.load()
#
#       # Draw the rectangle for cactus
#       for i in range(770, 850):
#          for j in range(395, 425):
#             data[i, j] = 0
#
#       # Draw the rectangle for birds
#       for i in range(770, 800):
#          for j in range(365, 390):
#             data[i, j] = 171
#       image.show()
#       break

if __name__ == "__main__":
   chrome_path = "C:\Program Files\Google\Chrome\Application\chrome.exe"

   # open a public URL, in this case, the webbrowser docs
   url = "https://elgoog.im/t-rex/"
   webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
   webbrowser.get('chrome').open_new_tab(url)

   time.sleep(5)
   click('up')

   while True:
     image = ImageGrab.grab().convert('L')
     data = image.load()
     isCollision(data)



