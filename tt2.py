import pyautogui
import time
import keyboard
import tkinter as tk
from tkinter import scrolledtext, messagebox
import webbrowser

def delayed_input(text, delay=0.5):
    """
    模拟延迟输入文字的功能。
    :param text: 要输入的文本
    :param delay: 每个字符之间的延迟时间（秒）
    """
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)  # 设置每个字符之间的延迟时间

def open_website():
    """ 打开指定网站 """
    webbrowser.open('http://my.allnet.vip')

def start_input_process():
    """ 开始输入过程 """
    text_to_input = text_box.get("1.0", tk.END).strip()  # 获取输入框中的文本
    if text_to_input:
        status_label.config(text="开始输入过程，准备切换窗口...")
        root.update()
        time.sleep(1)  # 防止快捷键触发时立即执行输入
        # 等待 3 秒，以便你切换到你要输入文字的地方
        count = 3
        while count > 0:
            status_label.config(text=f"请在 {count} 秒内切换到目标窗口...")
            root.update()
            time.sleep(1)
            count -= 1
        
        # 调用延迟输入函数
        status_label.config(text="正在输入中...")
        root.update()
        delayed_input(text_to_input, delay=float(delay_var.get()))
        status_label.config(text="输入完成!")

def on_hotkey_pressed():
    """ 当按下快捷键时，触发输入事件 """
    # 尝试将窗口最小化，以便用户可以立即切换到目标窗口
    root.iconify()
    start_input_process()

def set_new_hotkey():
    """ 设置新的快捷键 """
    try:
        new_hotkey = hotkey_entry.get().strip()
        if new_hotkey:
            # 先移除旧的快捷键
            for hotkey in active_hotkeys:
                try:
                    keyboard.remove_hotkey(hotkey)
                except:
                    pass
            
            # 清空活跃快捷键列表
            active_hotkeys.clear()
            
            # 添加新快捷键
            hotkey_id = keyboard.add_hotkey(new_hotkey, on_hotkey_pressed)
            active_hotkeys.append(hotkey_id)
            
            # 更新快捷键显示
            info_label.config(text=f"当前快捷键: {new_hotkey}")
            messagebox.showinfo("成功", f"已设置新快捷键: {new_hotkey}")
    except Exception as e:
        messagebox.showerror("错误", f"无法设置快捷键: {str(e)}")

# 创建一个全局变量来存储活跃的快捷键ID
active_hotkeys = []

# 创建一个简单的GUI
root = tk.Tk()
root.title("自动输入程序")
root.geometry("550x450")

# 创建一个主框架
main_frame = tk.Frame(root, padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# 创建输入框和标签
label = tk.Label(main_frame, text="输入要自动键入的文字:", font=("微软雅黑", 10))
label.pack(pady=5, anchor="w")

# 使用scrolledtext替代Entry，以支持多行输入和滚动
text_box = scrolledtext.ScrolledText(main_frame, width=50, height=10)
text_box.pack(pady=10, fill=tk.BOTH, expand=True)

# 创建延迟时间选择框
delay_frame = tk.Frame(main_frame)
delay_frame.pack(fill=tk.X, pady=5)

delay_label = tk.Label(delay_frame, text="输入延迟(秒):", font=("微软雅黑", 9))
delay_label.pack(side=tk.LEFT, padx=(0,5))

delay_var = tk.StringVar(value="0.5")
delay_options = ["0.1", "0.2", "0.3", "0.5", "0.8", "1.0"]
delay_menu = tk.OptionMenu(delay_frame, delay_var, *delay_options)
delay_menu.pack(side=tk.LEFT)

# 创建手动触发按钮
trigger_button = tk.Button(main_frame, text="开始输入", font=("微软雅黑", 10, "bold"), 
                          command=start_input_process, bg="#4CAF50", fg="white",
                          relief=tk.RAISED, padx=20)
trigger_button.pack(pady=10)

# 创建快捷键设置框
hotkey_frame = tk.Frame(main_frame)
hotkey_frame.pack(fill=tk.X, pady=5)

hotkey_label = tk.Label(hotkey_frame, text="设置快捷键:", font=("微软雅黑", 9))
hotkey_label.pack(side=tk.LEFT, padx=(0,5))

hotkey_entry = tk.Entry(hotkey_frame, width=15)
hotkey_entry.insert(0, "ctrl+alt+v")
hotkey_entry.pack(side=tk.LEFT, padx=(0,5))

hotkey_button = tk.Button(hotkey_frame, text="应用", command=set_new_hotkey)
hotkey_button.pack(side=tk.LEFT)

# 设置一个提示标签
info_label = tk.Label(main_frame, text="当前快捷键: ctrl+alt+v", font=("微软雅黑", 10, "bold"))
info_label.pack(pady=5)

# 设置使用说明
help_text = """
使用说明:
1. 在上方文本框中输入要自动键入的内容
2. 按"开始输入"按钮或使用快捷键触发
3. 在倒计时期间切换到目标窗口
4. 文本将自动输入到目标窗口中
"""
help_label = tk.Label(main_frame, text=help_text, font=("微软雅黑", 9), justify=tk.LEFT)
help_label.pack(pady=5, anchor="w")

# 状态显示标签
status_label = tk.Label(main_frame, text="就绪", font=("微软雅黑", 9), fg="blue")
status_label.pack(pady=5)

# 添加可点击的链接文字
link_label = tk.Label(main_frame, text="来自：琢飞CLDOU", font=("微软雅黑", 9), fg="blue", cursor="hand2")
link_label.pack(pady=5)
link_label.bind("<Button-1>", lambda e: open_website())
link_label.bind("<Enter>", lambda e: link_label.config(fg="red"))
link_label.bind("<Leave>", lambda e: link_label.config(fg="blue"))

# 启动快捷键监听
try:
    # 注册多个常用快捷键组合，增加成功率
    hotkey_id1 = keyboard.add_hotkey('ctrl+alt+v', on_hotkey_pressed)
    hotkey_id2 = keyboard.add_hotkey('ctrl+shift+v', on_hotkey_pressed)
    
    # 将快捷键ID添加到活跃列表
    active_hotkeys.extend([hotkey_id1, hotkey_id2])
except Exception as e:
    messagebox.showwarning("警告", f"快捷键可能无法正常工作: {str(e)}\n请使用按钮代替。")

# 运行GUI的主循环
root.mainloop()

# 确保退出时清理键盘监听器
try:
    keyboard.unhook_all()
except:
    pass 