import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pikepdf import Pdf

#選択された単位リスト
selected = []

##各科目フレームフォーマット
class each_sub_format():
    def __init__(self, 科目群フレーム, 各科目名, 科目リスト, 変数名):
        self.sub_frame = 科目群フレーム
        self.sub_label_name = 各科目名
        self.sub_list = 科目リスト

    def set_each_sub_frame(self):
        each_sub_frame  = ttk.Frame(self.sub_frame)
            #ラベルアンドボタンフレーム
        each_sub_lb_bt_frame = ttk.Frame(each_sub_frame)
            #各科目ラベル
        each_sub_label = tk.Label(each_sub_lb_bt_frame , text = '{}'.format(self.sub_label_name))
        each_sub_label.grid(row = 0, column = 0)
            #各科目登録ボタン
        def select():
            for i in each_listbox.curselection():
                selected.append(each_listbox.get(i,i)[0])
            print(selected)
        each_sub_label = tk.Button(each_sub_lb_bt_frame , text = '登録', command = select)
        each_sub_label.grid(row = 0, column = 1)
            #リストボックスフレーム
        listbox_frame = ttk.Frame(each_sub_frame)
                #各科目スクロールバー
        each_scroll = tk.Scrollbar(listbox_frame)
                #各科目リストボックス
        each_list_value = tk.StringVar()
        each_list_value.set(self.sub_list)
        each_listbox = tk.Listbox(listbox_frame, listvariable = each_list_value, selectmode = 'multiple',yscrollcommand = each_scroll.set, height = 5)
        each_listbox.grid(row = 0, column = 0)
        each_scroll.grid(row = 0, column = 1)
        each_scroll ["command"]=each_listbox.yview

        each_sub_lb_bt_frame.grid(row = 0, column = 0)
        listbox_frame.grid(row = 1, column = 0)
        each_sub_frame.grid(pady = 10, padx = 5)