import pyautogui
import time

print("Ctrl-c for stop")
try:
    while True:
        x, y = pyautogui.position()
        position_str = f"X: {x}. Y: {y}"
        print(position_str, end="")
        print("\b" * len(position_str), end="", flush=True)
        pyautogui.move(60, 0, duration=0.01)
        time.sleep(5)
        x, y = pyautogui.position()
        position_str = f"X: {x}. Y: {y}"
        print(position_str, end="")
        print("\b" * len(position_str), end="", flush=True)
        pyautogui.moveTo(0, 60, duration=0.01)
        time.sleep(5)

except KeyboardInterrupt:
            print("\nDone.")


