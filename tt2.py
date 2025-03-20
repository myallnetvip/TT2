import pyautogui
import time
import keyboard
import tkinter as tk

def delayed_input(text, delay=0.5):
    """
    模拟延迟输入文字的功能。
    :param text: 要输入的文本
    :param delay: 每个字符之间的延迟时间（秒）
    """
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)  # 设置每个字符之间的延迟时间

def on_hotkey_pressed():
    """ 当按下快捷键时，触发输入事件 """
    text_to_input = text_box.get()  # 获取输入框中的文本
    if text_to_input:
        print("快捷键被触发，开始输入...")
        time.sleep(1)  # 防止快捷键触发时立即执行输入
        # 等待 5 秒，以便你切换到你要输入文字的地方
        print("请在 5 秒后切换到你要输入文字的地方...")
        time.sleep(5)
        
        # 调用延迟输入函数
        delayed_input(text_to_input, delay_time=0.5)

# 创建一个简单的GUI
root = tk.Tk()
root.title("延迟输入程序")

# 创建输入框和标签
label = tk.Label(root, text="输入文字:")
label.pack(pady=10)

text_box = tk.Entry(root, width=40)
text_box.pack(pady=10)

# 设置一个提示标签
info_label = tk.Label(root, text="按下 Ctrl+Shift+I 启动输入功能")
info_label.pack(pady=10)

# 启动快捷键监听
keyboard.add_hotkey('ctrl+shift+i', on_hotkey_pressed)

# 运行GUI的主循环
root.mainloop()
