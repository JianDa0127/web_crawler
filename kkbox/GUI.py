import tkinter as tk

# 視窗初始化
main_window = tk.Tk()
main_window.title("kkbox")
# 視窗高度和寬度
main_window_h = 400
main_window_w = 300
# 取得螢幕高度和寬度
screen_h = main_window.winfo_screenheight()
screen_w = main_window.winfo_screenwidth()
x = (screen_h - main_window_h) / 2
y = (screen_w - main_window_w) / 2

main_window.geometry("%dx%d+%d+%d" % (main_window_h, main_window_w, x, y))

main_window.mainloop()