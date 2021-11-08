import pyautogui
from pynput.keyboard import *
import time

keyburd=Controller()
print("// Auto Key Presser készítve IMPERATOR666888 által, a kód iSayChris Autoclickeréből származik és az lett módosítva a célom elérése érdekében...")
print("// https://github.com/isaychris/python-autoclicker <==== Ez a kis program lett átalakítva.")
print("Milyen karaktert akarsz ismételni?")
az=input()
print("Milyen legyen a késleltetés? Másodpercben add meg! Ha a másodperc töredékére van szükséged, akkor írd valahogy így: 0.003 ")
seksz=float(input())
print(seksz)
#  ======== settings ========
delay = 1  # in seconds
resume_key = Key.page_up
pause_key = Key.right
exit_key = Key.page_down
#  ==========================

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
    print("// - Settings: ")
    print("\t delay = " + str(delay) + ' sec' + '\n')
    print("// - Controls:")
    print("\t page_up = Resume")
    print("\t right = Pause")
    print("\t page_down = Exit")
    print("-----------------------------------------------------")
    print('Press page_up to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            time.sleep(seksz)
            keyburd.press(az)
            keyburd.release(az)
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()