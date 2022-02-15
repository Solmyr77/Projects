import pyautogui
from pynput.keyboard import *
import time

keyboard=Controller()
print("Milyen karaktert akarsz ismételni?")
az=input()
print("Milyen legyen a késleltetés? Másodpercben add meg! Ha a másodperc töredékére van szükséged, akkor írd valahogy így: 0.003 ")
delay_p=float(input())
print(delay_p)
#  setting
delay = 1  # sec
resume_key = Key.page_up
pause_key = Key.right
exit_key = Key.page_down

pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// - Beállítások: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Gombok:")
    print("\t page_up = Indít")
    print("\t right = Pause")
    print("\t page_down = Exit")
    print("-----------------------------------------------------")
    print('page_up az indításhoz ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            time.sleep(delay_p)
            keyboard.press(az)
            keyboard.release(az)
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()