import tkinter as tk
from tkinter import ttk
import tkinter.font as f
import frame1    #ファイル読み込み画面のコードファイル

def main():
    root = tk.Tk()
    root.title('syllabetai')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.geometry("1500x800")
    style = ttk.Style()
    style.theme_use('classic')
    style.configure('MyWidget.TButton', background='#ffffcc')
    set_mainframe = Topframe(root)
    root.mainloop()
    
class Topframe():
    def __init__(self,root):
        self.file_move_frame = ttk.Frame(root, relief='sunken')
        self.file_move_frame.grid(row=0, column=0, sticky="nsew")

        title = tk.Label(self.file_move_frame, text="Syllabetai",
                         font=("MSゴシック", "200", "bold"))
        title.grid(padx=280,pady=100)

        font1 = f.Font(family="Lucida Console",
                       weight="bold", size=20, slant="italic")
        copy_label = tk.Label(self.file_move_frame, justify="center",
                            text="Copyright(C) 2022 Hitose Kakazu , Kenya Morishita. \nAll rights reserved.")
        copy_label["font"] = font1
        copy_label.grid(padx=280, pady=20)

        button = tk.Button(self.file_move_frame, text="OK",
                            command=lambda: to_frame1(), height=3,width=7)
        button.grid(padx=280, pady=30)

        def to_frame1():
            self.file_move_frame.grid_forget()
            to_register = frame1.Fileread(root)
        
#---------------------------------------------------------------------------------------------------------------------
# メイン関数
if __name__ == '__main__':
    main()
