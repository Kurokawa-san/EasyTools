from pynput.keyboard import Key, Controller
keyboard = Controller()
import time

import webbrowser
webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', new=2)

f = open('RICKROLLED.txt', 'w')
f.write("YOU GOT RICKROLLED!!!!! \n-ALDRICH JUSTIN LOTAS \ni put alot of effort to rick roll you all \np.s don't tell the others :)")
f.close

time.sleep(5)
time.sleep(0.1)
keyboard.press(Key.cmd)
keyboard.release(Key.cmd)

time.sleep(0.1)
for char in "RICKROLLE":
    keyboard.press(char)
    keyboard.release(char)
    time.sleep(0.5)
time.sleep(0.3)
keyboard.press('D')
keyboard.release('D')

time.sleep(1)
keyboard.press(Key.enter)
keyboard.release(Key.enter)

