import keyboard
import pyautogui
import pydirectinput
import locale
import time
from screeninfo import get_monitors
import tkinter as tk


def is_chinese_language():
    default_language, _ = locale.getdefaultlocale()
    if default_language.startswith('zh'):
        return True
    else:
        return False


is_chinese = is_chinese_language()


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


def alert(content_text):
    # 创建顶层窗口
    window = tk.Toplevel()

    # 设置窗口属性
    window.overrideredirect(True)  # 移除窗口边框
    window.attributes('-alpha', 0.8)  # 设置窗口透明度
    window.attributes("-topmost", True)  # 置顶窗口

    # 获取屏幕尺寸
    tkscreen_width = window.winfo_screenwidth()
    tkscreen_height = window.winfo_screenheight()

    # 设置窗口大小和位置
    window_width = 450
    window_height = 120
    x = (tkscreen_width - window_width) // 2
    y = 75
    window.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # 创建标签
    label = tk.Label(window, text=content_text, fg="white", bg="black", font=("汉仪文黑", 16, 'bold'))
    label.pack(fill=tk.BOTH, expand=True)

    # 设置定时器，3秒后关闭窗口
    window.after(2000, close_window, window)

    # 显示窗口
    window.deiconify()
    window.mainloop()


def close_window(window):
    window.withdraw()  # 隐藏窗口
    window.quit()  # 销毁窗口对象


mainLoop = True


def actively_exit():
    global mainLoop
    mainLoop = False


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
    alert('自动飞天将开始/start fly')
    print("自动飞天开始/start fly")
    time.sleep(0.5)
    pyautogui.press('esc')
    time.sleep(0.75)
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
        alert('对话模式终止/stop talk')
    else:
        alert('对话模式将开始/start talk')
        talking = True
        print('对话模式开始/start talk')


def talk():
    if talking:
        # 获取整个屏幕截图
        screen_image = pyautogui.screenshot()
        # 指定区域并使用截图进行图像匹配
        talk_select_position = pyautogui.locate('./src/talk_select.png', screen_image, confidence=0.8,
                                                region=(int(0.5 * screen_width), int(0.5 * screen_height), screen_width, screen_height))
        close_position = pyautogui.locate('./src/X.png', screen_image, confidence=0.90,
                                          region=(screen_width - 400, 0, screen_width, 200))
        auto_position = pyautogui.locate('./src/auto.png', screen_image, confidence=0.8,
                                         region=(0, 0, 400, 400))
        black = pyautogui.locate('./src/black.png', screen_image, confidence=0.8,
                                 region=(0, int(0.75 * screen_height), screen_width, screen_height))
        location_icon = pyautogui.locate('./src/location_icon.png', screen_image, confidence=0.7,
                                         region=(int(0.7*screen_width), 0, screen_width, 200))
        domain = pyautogui.locate('./src/domain.png', screen_image, confidence=0.7,
                                  region=(int(0.7*screen_width), 0, screen_width, screen_height))

        if talk_select_position is not None:
            talk_select_center = pyautogui.center(talk_select_position)
            pyautogui.click(talk_select_center.x, talk_select_center.y)
        elif close_position is not None and location_icon is None and domain is None:
            close_center = pyautogui.center(close_position)
            pyautogui.click(close_center.x, close_center.y)
        elif auto_position is not None or black is not None:
            pyautogui.click(screen_width/2, screen_height/2)
        else:
            print('未探测到对话/No dialogue detect.')



def rollingneuv():
    i = 0
    pydirectinput.moveRel(0, 200, duration=0.1, relative=True)
    while i < 27:
        pydirectinput.moveRel(1500, 0, duration=0.1, relative=True)
        i = i + 1


Neuvilletteing = False


def neuv_switcher():
    global Neuvilletteing
    if Neuvilletteing:
        Neuvilletteing = False
        print('Neuv自律模式终止/stop auto Neuv')
        alert('Neuv自律模式终止/stop auto Neuv')
    else:
        alert('Neuv自律模式开始/start auto Neuv')
        Neuvilletteing = True
        print('Neuv自律模式将开始/start auto Neuv')


def neuv():
    global Neuvilletteing
    if Neuvilletteing:
        if pyautogui.locateOnScreen('./src/NeuvQ.png', confidence=0.80,
                                    region=(screen_width-490, screen_height-180, screen_width, screen_height)) is not None:
            print('Neuv Q')
            pyautogui.press('q')
            time.sleep(2.8)
        if pyautogui.locateOnScreen('./src/NeuvE.png', confidence=0.80,
                                    region=(screen_width-490, screen_height-180, screen_width, screen_height)) is not None:
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
        pyautogui.keyDown('w')
        time.sleep(0.7)
        pyautogui.keyUp('w')


gathering = False


def gather_switcher():
    global gathering
    if gathering:
        gathering = False
        print('采集模式终止/stop gather')
        alert('采集模式终止/stop gather')
    else:
        alert('采集模式开始/start gather')
        gathering = True
        print('采集模式将开始/start gather')


def gather():
    global gathering
    if gathering:
        while True:
            screen_image = pyautogui.screenshot()
            target3_position = pyautogui.locate('./src/F.png', screen_image, confidence=0.80,
                                                region=(int(0.45*screen_width), int(0.3*screen_height-180), int(0.7*screen_width), int(0.7*screen_height)))
            target1_position = pyautogui.locate('./src/talk.png', screen_image, confidence=0.80,
                                                region=(int(0.45*screen_width), int(0.3*screen_height-180), int(0.7*screen_width), int(0.7*screen_height)))
            target2_position = pyautogui.locate('./src/gear.png', screen_image, confidence=0.80,
                                                region=(int(0.45*screen_width), int(0.3*screen_height-180), int(0.7*screen_width), int(0.7*screen_height)))
            if target1_position is None and target2_position is None and target3_position is not None:
                pyautogui.press('f')
                pyautogui.press('f')
                pyautogui.press('f')
            else:
                break


# 注册按键事件处理函数
keyboard.add_hotkey('f12', actively_exit)

# 注册按键组合 f11 飞
keyboard.add_hotkey('f11', fly)
print('Auto fly...OK')

# 注册按键事件处理函数
keyboard.add_hotkey('f10', talk_switcher)
print('Auto dialogue...OK ')

# 注册按键事件处理函数
keyboard.add_hotkey('ctrl+f9', neuv_switcher)
keyboard.add_hotkey('f9', rollingneuv)
print('Auto & rolling Neuvillette...OK ')

# 注册按键事件处理函数
keyboard.add_hotkey('f8', gather_switcher)
print('Auto gathering...OK ')

print('----说明|Instruction----')
if is_chinese:
    print("主界面中：f11-自动卡飞行bug，f10-自动对话，f9-那维莱特自律，f8-自动采集，f12-退出/重启程序")
else:
    print("Press f11 to fly, f10 for auto dialogue, f9 for auto Neuv, f8 for auto gathering, f12 to exit/restart")

# 循环执行程序
while mainLoop:
    talk()
    neuv()
    gather()
    time.sleep(0.1)
print('exited')