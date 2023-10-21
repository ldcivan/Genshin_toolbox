import keyboard
import pyautogui
import pydirectinput
import locale
import time
from screeninfo import get_monitors


def is_chinese_language():
    default_language, _ = locale.getdefaultlocale()
    if default_language.startswith('zh'):
        return True
    else:
        return False


is_chinese = is_chinese_language()

if is_chinese:
    print("主界面中：f11-自动卡飞行bug，f10-自动对话，f12-退出程序")
else:
    print("Press f11 to fly, f10 for auto dialogue, f12 to exit")


def click_pic(icon_path):
    # 点击特定图标
    icon_position = pyautogui.locateOnScreen(icon_path, confidence=0.80)
    if icon_position is not None:
        icon_center = pyautogui.center(icon_position)
        pyautogui.click(icon_center.x, icon_center.y)
    else:
        if is_chinese:
            print("无法找到以下图片，请尝试自行替换为自己截取的图片：", icon_path)
        else:
            print("Can not find position of the img:", icon_path)


# 获取屏幕分辨率大小
def get_screen_resolution():
    monitors = get_monitors()
    if monitors:
        monitor = monitors[0]  # 假设只有一个显示器
        width = monitor.width
        height = monitor.height
        return width, height
    else:
        return None


# 调用函数获取屏幕分辨率
resolution = get_screen_resolution()
if resolution:
    screen_width, screen_height = resolution
    print(f"屏幕分辨率/Resolution：{screen_width}x{screen_height}")
else:
    screen_width = 100
    screen_height = 100
    print("无法获取屏幕分辨率/Can not get resolution")


def fly():
    print("自动飞天开始/start fly")
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

    if is_chinese:
        print('自动飞天结束，f11来再次运行，f10使用自动对话，f12退出程序')
    else:
        print('Auto fly end. Press f11 for a new turn, f12 to exit.')


talking = False


def talk_switcher():
    global talking
    if talking:
        talking = False
        print('对话模式终止/stop talk')
    else:
        talking = True
        print('对话模式开始/start talk')


def talk():
    if talking:
        talk_select_position = pyautogui.locateOnScreen('./src/talk_select.png', confidence=0.8)
        close_position = pyautogui.locateOnScreen('./src/X.png', confidence=0.8)
        auto_position = pyautogui.locateOnScreen('./src/auto.png', confidence=0.8)
        if talk_select_position is not None and auto_position is not None:
            talk_select_center = pyautogui.center(talk_select_position)
            pyautogui.click(talk_select_center.x, talk_select_center.y)
        elif close_position is not None:
            close_center = pyautogui.center(close_position)
            pyautogui.click(close_center.x, close_center.y)
        elif auto_position is not None:
            pyautogui.click(screen_width/2, screen_height/2)
        else:
            print('未探测到对话/No dialogue detect.')


Neuvilletteing = False

def Neuvillette_switcher():
    global Neuvilletteing
    if Neuvilletteing:
        Neuvilletteing = False
        print('Neuv模式终止/stop Neuv')
    else:
        Neuvilletteing = True
        print('Neuv模式开始/start Neuv')


def Neuvillette():
    global Neuvilletteing
    if Neuvilletteing:
        if pyautogui.locateOnScreen('./src/NeuvQ.png', confidence=0.80) is not None:
            print('Neuv Q')
            pyautogui.press('q')
            time.sleep(2.8)
        if pyautogui.locateOnScreen('./src/NeuvE.png', confidence=0.80) is not None:
            print('Neuv E')
            pyautogui.press('e')
            time.sleep(0.7)
        print('Neuv A')
        pyautogui.mouseDown(button='left')
        i = 0
        while i < 10 and Neuvilletteing:
            target1_position = pyautogui.locateOnScreen('./src/Neuv.png', confidence=0.55)
            target2_position = pyautogui.locateOnScreen('./src/Neuv2.png', confidence=0.55)
            if target1_position is not None or target2_position is not None:
                break
            else:
                pyautogui.keyDown('s')
                time.sleep(0.1)
                pyautogui.keyUp('s')
                i = i + 1
        i = 0
        pydirectinput.moveRel(0, 200, duration=0.1, relative=True)
        while i < 27 and Neuvilletteing:
            pydirectinput.moveRel(1500, 0, duration=0.1, relative=True)
            i = i + 1

        pyautogui.mouseUp(button='left')


# 注册按键组合 f11 飞
keyboard.add_hotkey('f11', fly)
print('Auto fly...OK')

# 注册按键事件处理函数
keyboard.add_hotkey('f10', talk_switcher)
print('Auto dialogue...OK ')

# 注册按键事件处理函数
keyboard.add_hotkey('f9', Neuvillette_switcher)
print('Neuvillette rolling...OK ')

# 循环执行程序
while True:
    talk()
    Neuvillette()
    time.sleep(1)

# 监听按键事件
keyboard.wait('f12')





