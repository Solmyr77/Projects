import pyautogui
from pynput.keyboard import *
import time
import ctypes
import dict as d
import os


SendInput = ctypes.windll.user32.SendInput
PUL = ctypes.POINTER(ctypes.c_ulong)


class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

def clear():
    os.system('CLS')

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))


def menu():
    print(f"Használható gombok:\n{d.char_dict}")


char = input("Gomb: ")
char = d.char_dict[char.upper()]
char = int(char)
time_delay=float(input('Delay: '))


resume_key = Key.page_up
pause_key = Key.right
exit_key = Key.page_down


pause = True
running = True


def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Start]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// - Settings: ")
    print(f"\t delay = {time_delay}")
    print("// - Controls:")
    print("\t page_up = Start")
    print("\t right = Pause")
    print("\t page_down = Exit")
    print("-----------------------------------------------------")
    print('Press page_up to start ...')


def main():
    menu()
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            PressKey(char)
            time.sleep(time_delay/2)
            ReleaseKey(char)
            time.sleep(time_delay/2)
            pyautogui.PAUSE = 1
    lis.stop()

if __name__ == "__main__":
    clear()
    main()
