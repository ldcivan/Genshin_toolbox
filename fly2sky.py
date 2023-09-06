import keyboard
import pyautogui
import time


def click_pic(icon_path):
    # 点击特定图标
    icon_position = pyautogui.locateOnScreen(icon_path, confidence=0.8)
    if icon_position is not None:
        icon_center = pyautogui.center(icon_position)
        pyautogui.click(icon_center.x, icon_center.y)
    else:
        print("Can not find position of the img:", icon_path)


def activate_program():
    print("Running...")
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.7)
    click_pic('./src/photo.png')

    time.sleep(0.5)
    pyautogui.press('f2')
    time.sleep(0.6)
    click_pic('./src/pose_think.png')
    pyautogui.press('esc')
    pyautogui.press('esc')
    pyautogui.press('space')
    pyautogui.press('esc')
    time.sleep(0.7)
    click_pic('./src/photo.png')

    time.sleep(0.5)
    pyautogui.press('f2')
    time.sleep(0.25)
    click_pic('./src/pose_think.png')

    print('End. Press f11 for a new turn.')

print("Press f11 to run a new turn, and press f12 to stop script")

# 注册按键组合 f11
keyboard.add_hotkey('f11', activate_program)

# 监听按键事件
keyboard.wait('f12')

