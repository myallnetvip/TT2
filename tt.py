import pyautogui
import time
import keyboard

def delayed_input(text, delay=0.5):
    """
    模拟延迟输入文字的功能。
    
    :param text: 要输入的文本
    :param delay: 每个字符之间的延迟时间（秒）
    """
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)  # 设置每个字符之间的延迟时间

if __name__ == "__main__":
    # 设置输入文本	
    text_to_input = "I'm just an average player when it comes to playing games."
    
    # 设置延迟时间
    delay_time = 0.1  # 每个字符输入之间的延迟时间（秒）
    
    print("按下 'Ctrl+Shift+I' 启动输入功能...")
    
    # 循环监听快捷键
    while True:
        if keyboard.is_pressed('ctrl+shift+i'):  # 快捷键为 Ctrl+Shift+I
            print("快捷键被触发，开始输入...")
            time.sleep(1)  # 防止快捷键触发时立即执行输入
            # 等待 5 秒，以便你切换到你要输入文字的地方
            print("请在 5 秒后切换到你要输入文字的地方...")
            time.sleep(5)
            
            # 调用延迟输入函数
            delayed_input(text_to_input, delay_time)
            break  # 输入完成后退出程序
