import tkinter as tk
from tkinter import ttk
import sys
import os
import numpy as np
import pandas as pd
import sqlite3
import topframe

class Displaycalender():
    def __init__(self, root, selected):
        ##講義選択画面から受け取ったリストをカレンダー用リストに変換

        #\xaoの削除(frame2で行うべき、frame2で表示されているか確認する)
        DefLabel = []
        for i in range(0, len(selected)):
            #selected[i] = selected[i].replace(u"\xa0", "")
            DefLabel.append(selected[i].split())
        print(DefLabel)

        ##カレンダー表示の親フレーム
        calender_top_frame = ttk.Frame(root)
        calender_top_frame.grid(row=0, column=0, sticky="nsew")

        ##曜日・時間のラベル作成
        def label_func(text, c, r):
            label = tk.Label(calender_top_frame, text=text)
            label.grid(column=c, row=r, sticky="nsew")

        label_list = (  # text , 列 , 行
            ['月', 1, 0], ['火', 2, 0], ['水', 3, 0], [
                '木', 4, 0], ['金', 5, 0], ['土', 6, 0],
            ['1限目', 0, 1], ['2限目', 0, 2], [
                '3限目', 0, 3], ['4限目', 0, 4], ['5限目', 0, 5]
        )
        for la in label_list:
            label_func(la[0], la[1], la[2])

        # #最初にデータフレームに格納して、中身を抜き出し出力する
        temp_value = [[""], [""], [""], [""], [""]]
        temp_value = np.repeat(temp_value, 6, 1)
        day_list = ["Mon", "Tues", "Wednes", "Turs", "Fri", "Satur"]
        df = pd.DataFrame(temp_value, columns=day_list,
                          index=["1", "2", "3", "4", "5"])
        for fday, ftime, fsubject, fclassroom, fteacher,connection_key in DefLabel:
            df.loc[ftime, fday] = fsubject + " " + fclassroom + " " + fteacher

        #エントリーの作成
        for col in range(1, 7):  # 1,2,3,4,5,6   曜日
            for row in range(1, 6):  # 1,2,3,4,5　時限
                lframe = ttk.Frame(calender_top_frame)
                lframe.grid(column=col, row=row,
                            sticky="nsew", padx=2, pady=10)
                lecture_name = tk.Entry(lframe, font='MSゴシック 12')
                lecture_name.insert(0, df.iloc[row-1, col-1])
                lecture_name.pack(ipadx=25, ipady=10)

        #csvへ出力するボタン作成
        self.to_csv_button = tk.Button(calender_top_frame, text='csvへ出力', width=15,
                                       command=lambda: to_csv_func())
        self.to_csv_button.grid(row=6, column=0, pady=10, columnspan=5)

        #トップ画面に戻る
        self.back_button = tk.Button(calender_top_frame, text='トップページへ戻る', width=15,
                                     command=lambda: back_func())
        self.back_button.grid(row=6, column=1)

        def to_csv_func():
            #csvに出力するコード
            df.to_csv("Syllabetai_RegisteClasses.csv")
            #個人用のデータベースを削除
            os.remove("Individual_Database.db")
            sys.exit()

        def back_func():
            #calender_top_frame.grid_forget()
            select_subject = topframe.Topframe(root)
