import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pikepdf import Pdf
import sqlite3
import pandas as pd
import frame3
import time
import topframe
import numpy as np
from tkinter import messagebox

#--------------------------------------------------講義選択画面設定------------------------------------------------------------

#*********************指定クラス , ミニカレンダー 
class ClassRegistration():
    def __init__(self, root):

        #選択された単位リスト
        self.selected = []

        ######画面遷移用フレーム
        self.select_move_frame = ttk.Frame(root, relief='solid')   #メインフレーム
        self.select_move_frame.grid(row=0, column=0, sticky="nsew")

        ####学年・学期入力フレーム
        self.class_frame = ttk.Frame(self.select_move_frame, relief='solid', width=1500, height=800)
        self.class_frame.grid(pady=45, padx=500)  # row=0,column=0,
        #見出し
        tk.Label(self.class_frame, text="履修登録を行う年の学年・学期を入力・送信してください").grid(
            row=0, column=0, pady=10, columnspan=4)

        self.check_department = tk.StringVar();self.check_department.set("政治学科")
        self.check_grade = tk.StringVar();self.check_grade.set("１年")
        self.check_semester = tk.StringVar();self.check_semester.set("春学期")
        self.check_foreign = tk.StringVar();self.check_foreign.set("ドイツ語")
  
        def classframe_func(text, lr, lc, clist,var):
            tk.Label(self.class_frame, text=text).grid(row=lr, column=lc)
            for rbindex in range(0, len(clist)):
                rdo1 = tk.Radiobutton(self.class_frame, value=clist[rbindex],
                                      variable=var, text=clist[rbindex])
                rdo1.grid(row=lr+1+rbindex, column=lc)
        classframe_func("学科", 1, 0, ["政治学科", '経済学科', '地域行政学科'], self.check_department)
        classframe_func(
            "学年", 1, 1, ["１年", '２年', '３年', '４年'], self.check_grade)
        classframe_func(
            "学期(春学期/秋学期)", 1, 2, ["春学期", '秋学期'], self.check_semester)
        classframe_func(
            "第二外国語", 1, 3, ["ドイツ語", 'フランス語', '中国語', 'スペイン語', '日本語'], self.check_foreign)

        #[送信]ボタン
        self.submit = tk.Button(self.class_frame, text='送信', width=10,
                                command=lambda: create_display_first_frame())
        self.submit.grid(row=1, column=4)

        #トップ画面に戻る
        findex = self.class_frame
        self.back_button = tk.Button(self.class_frame, text='トップページへ戻る', width=15,
                                     command=lambda : topback_func())
        self.back_button.grid(row=2, column=4)

        


        def create_display_first_frame():
            #送信ボタンを押された時の処理
            self.class_frame.grid_forget()

            ####講義選択画面における親フレーム
            self.display_first_frame = ttk.Frame(self.select_move_frame, relief='solid')    #メインフレーム
            self.display_first_frame.grid(row=0, column=0, padx=100, pady=20)

            self.display_first_frame.tkraise()

            #データフレームの作成
            access_database()

            self.nforeign = self.check_foreign.get()
            self.ndepartment = self.check_department.get()
        
            ##各フレームのリストを作成   外枠とラベルをまず作成する
            first_frame_list = (  # 後が0,0のやつが外枠のフレーム、1,0からは各要素、左から２番目は授業リストのキー番号にする
                # ------基礎科目フレーム-------
                (['<基礎科目群>', 10000, 1, 0],
                ['人文科学科目群', 1, 1, 0],
                ['社会科学科目群', 1, 2, 0],
                ['自然科学科目群', 1, 3, 0],
                ['総合科目群', 1, 4, 0]
                ),
                # ---------------------外国語---------------------
                (['<外国語>', 10000, 1, 1],
                ['英語', 1, 1, 0],
                 [self.nforeign, 1, 2, 0]
                ),
                # ---------------------健康・運動---------------------
                (['<健康運動科目>', 10000, 1, 2],
                ['健康運動１年次必修', 1, 1, 0],
                ['健康運動選択必修２単位', 1, 2, 0]
                ),
                # ---------------------所属学科学科---------------------
                (['<'+self.ndepartment+'>', 10000, 1, 3],
                 ['基本科目_'+self.ndepartment+'関係科目_1年次必修', 1, 1, 0],
                 ['基本科目_'+self.ndepartment+'関係科目_2年次必修', 1, 2, 0],
                 ['基本科目_'+self.ndepartment+'関係科目_12年次配当', 1, 3, 0],
                 ['基本科目_'+self.ndepartment+'関係科目_34年次配当', 1, 4, 0]
                )
            )
            display_func(first_frame_list, self.display_first_frame,
                         create_display_second_frame, '次のページへ')
            #_____________________ミニカレンダー________________________
            ##曜日・時間のラベル作成
            self.mini_calendar = ttk.Frame(
                self.select_move_frame, relief='solid')  # メインフレーム
            self.mini_calendar.grid(row=0, column=1)

            def label_func(text, c, r):
                label = tk.Label(self.mini_calendar, text=text)
                label.grid(column=c, row=r, sticky="nsew")

            self.label_list = (  # text , 列 , 行
                ['Mon', 1, 0], ['Tues', 2, 0], ['Wednes', 3, 0],
                ['Turs', 4, 0], ['Fri', 5, 0], ['Satur', 6, 0],
                ['1', 0, 1], ['2', 0, 2],
                ['3', 0, 3], ['4', 0, 4], ['5', 0, 5]
            )
            for la in self.label_list:
                label_func(la[0], la[1], la[2])

            for c in range(1,7):
                for r in range(1,6):
                    label = tk.Label(self.mini_calendar,
                                     text=" ", background='#ffffff', relief='solid')
                    label.grid(column=c,row=r, sticky="nsew")

        def create_display_second_frame():
            #次へボタンを押された時の処理
            self.display_first_frame.grid_forget()
            ####講義選択画面における親フレーム
            self.display_second_frame = ttk.Frame(
                self.select_move_frame, relief='solid')
            self.display_second_frame.grid(row=0, column=0, padx=100, pady=20)

            #self.display_second_frame.tkraise()
            
            ##各フレームのリストを作成   外枠とラベルをまず作成する
            second_frame_list = (  # 後が0,0のやつが外枠のフレーム、1,0からは各要素、左から２番目は授業リストのキー番号にする
                # ---------------------所属学科---------------------
                (['<応用科目>', 10000, 1, 0],
                 ['応用科目_'+self.ndepartment+'関係科目', 1, 1, 0],
                 ),
                # --------------------その他---------------------
                (['<その他>', 10000, 1, 1],
                 ['学部間共通外国語', 1, 1, 0],
                 ['３学科共通基本科目', 1, 2, 0],
                 ['3学科共通関係科目', 1, 3, 0],
                 ['専門演習科目', 1, 4, 0]
                 ),
                # ---------------------その他---------------------
                (['<その他>', 10000, 1, 2],
                 ['原典研究科目', 1, 1, 0],
                 ['総合講座科目', 1, 2, 0],
                 ['特殊講義科目', 1, 3, 0],
                 ["情報科目", 1, 4, 0]
                 ),
                # ---------------------その他---------------------
                (['<その他>', 10000, 1, 3],
                 ['資格課程科目', 1, 1, 0],
                 ['グローバル全学部共通科目', 1, 2, 0],
                 ["卒業に含めない科目", 1, 3, 0]
                 )
            )
            display_func(second_frame_list, self.display_second_frame,
                         register, '登録して確認する')

        def display_func(frame_list,on_frame,button_command,button_text):
            #ここで、個人用のデータベースを参照し、足りていない必修単位のラベルを赤字に変える
            #個人用データベースを参照するための配列
            self.dbmatch_array = {
                '<基礎科目群>': '◆基礎科目',
                '人文科学科目群': '人文科学科目群',
                '社会科学科目群': '社会科学科目群',
                '自然科学科目群': '自然科学科目群',
                '総合科目群': '総合科目群',
                '<外国語>': '◆外国語科目(共通外国語含む)',
                '<健康運動科目>': '◆健康・運動科学科目',
                '健康運動１年次必修': '必修科目【運動学演習I-1・I-2】',
                '健康運動選択必修２単位': '選択必修科目(2-4年次)',
                '<'+self.ndepartment+'>': '◆経済学関係科目',
                '基本科目_'+self.ndepartment+'関係科目_1年次必修': '必修科目',  # ここ気を付ける
                '基本科目_'+self.ndepartment+'関係科目_2年次必修': '必修科目',
                '基本科目_'+self.ndepartment+'関係科目_34年次配当': '選択必修科目(3・4年次)',
                '原典研究科目': '◆原典研究科目'  # に値が入っている場合は、※コース科目(コース選択者のみ)の判定を飛ばす
            }

            for each_list in frame_list:  # 各フレームのリストを取り出す
                for category_list in each_list:
                    text = category_list[0]
                    var = category_list[1]
                    r = category_list[2]
                    c = category_list[3]

                    if var == 10000:
                        self.each_frame = ttk.Frame(
                            on_frame, relief='solid')
                        self.each_frame.grid(row=r, column=c) #必要であればrowspan
                        #科目ラベル
                        label = tk.Label(
                            self.each_frame, text=text, foreground=not_enough_credits(text)).grid(row=0, column=0)  # 0列 0行
                    else:
                        self.sub_frame = ttk.Frame(
                            self.each_frame, relief='solid')

                        self.sub_label_name = text
                        self.sub_list = extract()  # リストここ＊＊＊＊＊＊＊＊＊＊＊＊＊＊＊
                        self.subject = each_sub_format()
                        self.sub_frame.grid(row=r, column=c)

            # ---------------<Next>ボタン-------------
            self.button_frame = ttk.Frame(
                on_frame, relief='solid')
            self.button_frame.grid(row=0, column=0, pady=10, columnspan=4)

            all_register = tk.Button(
                self.button_frame, command=button_command, text=button_text, height=3)
            all_register.grid(row=0, column=0,rowspan=2)

            #クリアボタン
            clear_button = tk.Button(
                self.button_frame, text='クリア', command=clear,height=3)
            clear_button.grid(row=0, column=1)

            #トップ画面に戻る
            self.back_button1 = tk.Button(self.button_frame, text='Top',
                                          command=lambda: topback_func(), height=3)
            self.back_button1.grid(row=0, column=2)

            #前のページに戻る
            if button_text == '登録して確認する':
                j = 1
                self.back_button2 = tk.Button(self.button_frame, text='Page 1 Back',
                                          command=lambda :one_back_func(j), height=3)
                self.back_button2.grid(row=0, column=3)

            

        ##各科目フレームフォーマット
        def each_sub_format():
            each_sub_frame = ttk.Frame(self.sub_frame)
            #ラベルアンドボタンフレーム
            each_sub_lb_bt_frame = ttk.Frame(each_sub_frame)
            #各科目ラベル
            each_sub_label = tk.Label(
                each_sub_lb_bt_frame, text='{}'.format(self.sub_label_name), foreground=not_enough_credits(self.sub_label_name))
            each_sub_label.grid(row=0, column=0)
    
            #textは、人文科学群など
            #ここでクラス指定
            def select():
                for i in each_listbox.curselection():  #list_boxのindexを返す 上から0,1,2,3
                    sentence = each_listbox.get(i)
                    sentence_list = sentence.split()
                    
                    #Connection_keyの取得
                    co_key = int(sentence_list[len(sentence_list)-1])
                    print("connection_key",co_key)
                    #0以外のconnection_keyが同じ行の取得
                    if co_key != 0:
                        relate_sentence = self.df.loc[self.df.loc[:, "Connection_key"] == co_key, [
                            "Dayofweek", "Time", "Subject", "Classroom", "Teacher", "Connection_key"]]
                        relate_sentence.loc[:, "Connection_key"] = relate_sentence["Connection_key"].astype('str')
                        relate_sentence.loc[:, "Time"] = relate_sentence["Time"].astype('str')

                        for count in range(0, len(relate_sentence)):
                            stext = ""
                            for i in relate_sentence.iloc[count, :]:
                                stext = stext + i + " "
                            if len(self.selected) != 0:
                                # 重複しているとメッセージを出す
                                check_duplication(stext, each_sub_button)
                            else:
                                self.selected.append(stext)
                                take_color(stext)
                    else:
                        if len(self.selected) != 0:
                            #print("check_duplicationの関数")
                            check_duplication(sentence, each_sub_button)
                        else:
                            self.selected.append(sentence)
                            take_color(sentence)
                print(self.selected)

            #各科目登録ボタン
            each_sub_button = tk.Button(
                each_sub_lb_bt_frame, text='登録', command=select)  # , activebackground="purple", activeforeground="blue")
            each_sub_button.grid(row=0, column=1)
            #リストボックスフレーム
            listbox_frame = ttk.Frame(each_sub_frame)
            #各科目スクロールバー
            each_scroll = tk.Scrollbar(listbox_frame)
            #各科目リストボックス
            each_list_value = tk.StringVar()
            each_list_value.set(self.sub_list)   # *******************
            each_listbox = tk.Listbox(listbox_frame, listvariable=each_list_value,
                                      selectmode='multiple', yscrollcommand=each_scroll.set, height=5)
            each_listbox.grid(row=0, column=0)
            each_scroll.grid(row=0, column=1)
            each_scroll["command"] = each_listbox.yview

            each_sub_lb_bt_frame.grid(row=0, column=0)
            listbox_frame.grid(row=1, column=0)
            each_sub_frame.grid(pady=10, padx=10)

        def access_database():
            grade = self.check_grade.get()
            semester = self.check_semester.get()
            jtext = grade + semester

            dbname = ('syllabetai_database.db') 
            conn = sqlite3.connect(dbname, isolation_level=None)
            cursor = conn.cursor()  # カーソルオブジェクトを作成
            if jtext == "１年春学期" or jtext == "２年春学期":
                tbname = "spring12"
            elif jtext == "１年秋学期" or jtext == "２年秋学期":
                tbname = "autumn12"
            elif jtext == "３年春学期" or jtext == "４年春学期":
                tbname = "spring34"
            elif jtext == "３年秋学期" or jtext == "４年秋学期":
                tbname = "autumn34"
            else:
                print("Error")
            sql = 'SELECT * FROM ' + tbname
            self.df = pd.read_sql_query(sql, conn)

            dbname = ('Individual_Database.db')  
            conn = sqlite3.connect(dbname, isolation_level=None)
            cursor = conn.cursor()
            self.person_df = pd.read_sql_query('SELECT * FROM summary', conn)
            self.person_df = self.person_df.replace(np.nan, 0)
            self.person_df.loc[:, "必要単位数"] = self.person_df["必要単位数"].astype('int')
            self.person_df.loc[:, "合計"] = self.person_df["合計"].astype('int')
            cursor.close()  

        #textを引数に入れる
        def extract():
            df1 = self.df.loc[self.df.loc[:, "Category"] == self.sub_label_name, :]
            ex_list = ['Dayofweek', 'Time', 'Subject', 'Classroom', 'Teacher','Connection_key']
            df2 = df1.loc[:, ex_list]
            df2.loc[:, "Time"] = df2.astype("str")
            df2.loc[:, "Connection_key"] = df2.astype("str")
            display_list = []
            for i in range(0, len(df2)):
                colindex = df2.columns
                text = ""
                for k in range(0, len(colindex)):
                    try:
                        text = text + df2.iloc[i, k] + " "
                    except TypeError:
                        text = "None"
                text = text.replace(u"\xa0", "") #ここでテキストの\xaoを排除する
                display_list.append(text)
            return display_list

        def not_enough_credits(sub_label_name):
            if sub_label_name in self.dbmatch_array.keys():
                #キーの項目があれば、valueの項目の１列２列の比較
                datum = self.person_df[self.person_df.loc[:,"単位習得状況"] == self.dbmatch_array[sub_label_name]]
                if int(datum["必要単位数"]) > int(datum["合計"]):
                    print("必要単位数が足りてません")
                    color = "#ff0000"
                else:
                    color = "#000000"
            else:
                color = "#000000"
            return color

        def check_duplication(check_text, each_sub_button):
            split_text = check_text.split()
            print("split_text_____",split_text,"_______")
            judge_var = 0
            for ttt in self.selected:
                tetet = ttt.split()
                if split_text[0] == tetet[0] and split_text[1] == tetet[1]:
                    judge_var = 1
            if judge_var == 1:
                print('エラー;スケジュールが埋まってます')
                return messagebox.showerror('エラー', 'スケジュールが埋まってます')
                
            else:
                print("スケジュールは埋まってない")
                check_text = check_text.replace(u"\xa0", "")
                self.selected.append(check_text)
                take_color(check_text)
                # each_sub_button.config(bg="purple", fg="blue")
                # each_sub_button.config(state=tk.DISABLED)

        def topback_func():
            findex.grid_forget()
            select_subject = topframe.Topframe(root)

        def clear():
            self.selected = []
            print(self.selected)
            for c in range(1, 7):
                for r in range(1, 6):
                    label = tk.Label(self.mini_calendar,
                                     text=" ", background='#ffffff', relief='solid')
                    label.grid(column=c, row=r, sticky="nsew")
        
        def one_back_func(j):
            if j == 1:
                self.display_second_frame.grid_forget()
                self.display_first_frame.grid(
                    row=0, column=0, padx=100, pady=20)
                self.display_first_frame.tkraise()
            else:
                print('ERROR')

        def take_color(tc_text):
            tc_list = tc_text.split()
            llist = self.label_list[0:6]
            for la in llist:
                # la[0], la[1], la[2]
                if tc_list[0] == la[0]:

                    label = tk.Label(self.mini_calendar,
                                     text=" ", background='#ffaacc', relief='solid')
                    label.grid(column=la[1], row=int(tc_list[1]), sticky="nsew")
            # Mon 1 なら 1列0行なので、1列1行になる
            #だから。la[1]列la[2]+1行
        
        ##<登録して確認する>ボタンが押された時の関数
        def register():
            self.display_second_frame.grid_forget()
            #選択された授業名のリストをカレンダーのframeに投げる
            display_calender = frame3.Displaycalender(root,self.selected)
        
