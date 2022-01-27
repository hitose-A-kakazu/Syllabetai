import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pikepdf import Pdf
import tabula
from PIL import Image, ImageTk
from pathlib import Path
from pdf2image import convert_from_path
import os
import PyPDF2
from PyPDF2 import PdfFileReader
import pikepdf
import numpy as np
import pandas as pd
import sqlite3
import frame2
import topframe
import self_select
from tkinter import messagebox

#構造
#file_move_frame
# ---file_frame
# -------file_select_frame  (ファイルパスエリア・[ファイルを選択]ボタンを持つフレーム)
# -------pasword_frame (パスワードのフレーム)
# -------preview (プレビューのフレーム)
# -------read_frame([成績を読み込む]ボタンのフレーム)

#----------------------------------------------ファイル読み込み画面の設定-------------------------------------------------
class Fileread():
    def __init__(self, root):  # ファイル読み込み画面のラベル・エントリー・ボタンの設置
        self.file_move_frame = ttk.Frame(root, relief='sunken')
        self.file_move_frame.grid(row=0, column=0, sticky="nsew")

        ##ファイル読み込み画面における親フレーム
        self.file_frame = ttk.Frame(
            self.file_move_frame, relief='ridge')  # ********#
        self.file_frame.grid(padx=450, pady=10)

        #ファイル読み込みのラベル・テキストボックス・[ファイルを選択]ボタンを持つフレーム
        self.file_select_frame = ttk.Frame(
            self.file_frame, relief='solid')  # ++++++++++++#
        self.file_select_frame.grid(
            row=0, column=0, columnspan=2, pady=10)  # ++++++++++++#
        #ラベル
        tk.Label(self.file_select_frame, text="自分の成績表pdfを入れて下さい").grid(
            row=0, column=0, pady=10)
        #テキストボックス
        self.file_frame.edit_box = tk.Entry(self.file_select_frame, width=50)
        self.file_frame.edit_box.grid(row=1, column=0, pady=10)
        #[ファイルを選択]ボタン
        self.file_button = tk.Button(self.file_select_frame, text='ファイルを選択', width=10,
                                     command=lambda: open_file_command())
        self.file_button.grid(row=1, column=1, pady=10)

        ##パスワード関連のフレーム
        self.pasword_frame = ttk.Frame(
            self.file_frame, relief='solid')  # ++++++++++++#
        self.pasword_frame.grid(row=1, column=0)  # ++++++++++++#
        #パスワード入力を促すラベル
        self.pasword_label = tk.Label(
            self.pasword_frame, text='以下にパスワードを入力してください')
        self.pasword_label.grid(row=0, column=0, columnspan=2, pady=10)
        #パスワードの入力エントリー
        self.pasword_entry = tk.Entry(self.pasword_frame)
        self.pasword_entry.grid(row=1, column=0, pady=10, padx=10)

        ##ブレビュー画面
        self.preview = ttk.Frame(
            self.file_frame, relief='solid')  # ++++++++++++#
        self.preview.grid(row=2, column=0)  # ++++++++++++#
        self.img_canvas = tk.Canvas(
            self.preview,
            width=400,
            height=300,
            scrollregion=(-200, -100, 800, 600)
        )
        self.img_canvas.grid(row=0, column=0)

        ##[成績を読み込む]ボタンの設置
        self.read_frame = ttk.Frame(
            self.file_frame, relief='solid')  # ++++++++++++#
        self.read_frame.grid(row=3, column=0, pady=10)  # ++++++++++++#
        self.read_button = tk.Button(self.read_frame, text='成績を読み込む', width=15,
                                     command=lambda: read_file_command())
        self.read_button.grid(pady=10)

        self.next_button = tk.Button(self.read_frame, text='次のページへ', width=15,
                                     command=lambda: next_func())
        self.next_button.grid(pady=10)

        #トップ画面に戻る
        self.back_button = tk.Button(self.read_frame, text='トップページへ戻る', width=15,
                                     command=lambda: back_func())
        self.back_button.grid(pady=10)

    
        ##[ファイルを選択]ボタン押下時の関数
        def open_file_command():
            print("*************ファイルが選択されました*************")
            file_path = filedialog.askopenfilename()
            self.file_frame.edit_box.delete(0, tk.END)
            self.file_frame.edit_box.insert(tk.END, file_path)

        def file_read():
            # ファイルを開いて読み込んでdataに格納
            print("*************csvファイルに変換中*************")
            try:
                data = tabula.read_pdf(
                self.file_path, stream=True, pages='1')
            except Warning:
                messagebox.showerror('エラー', 'PDFの読み込みに失敗しました。手動での入力をお願いします。')
                selfselect_credits()
            else:
                data = data[0]
                #保存して確認する
                seiseki_path = "seiseki.csv"
                data.to_csv(seiseki_path, index=None)  # pdfからcsvに
                return seiseki_path

        def create_preview():
            print("*************プレビュー作成中*************")
            out_format = 'jpeg'
            image = convert_from_path(pdf_path=str(
                self.file_path), dpi=300, fmt=out_format)
            # 画像ファイルを保存
            for i, page in enumerate(image):
                file_name = "{}_{}{:02d}.{}".format(
                    self.file_path, "output", i+1, out_format)
                page.save(file_name, out_format)
            return file_name

        ##ファイルのパスワード解除関数(パスワード付きPDF→ パスワードなしPDFへ)
        def unlock_command():
            print("*************ファイルのパスワード解除*************")
            with open(self.file_path, mode='rb') as f:
                pdf = PyPDF2.PdfFileReader(f)
                if pdf.isEncrypted:
                    FILE_OUT_PATH = "{}_{}.{}".format(
                        self.file_path, "nonpass", "pdf")
                    pdf2 = pikepdf.open(self.file_path, password=self.password)
                    pdf2.save(FILE_OUT_PATH)
                else:
                    FILE_OUT_PATH = self.file_path
            return FILE_OUT_PATH

        #ここで読み込んだCSVをデータフレームに変える自動化コードをかく
        def cleansing():  # 一回csvで保存してpandasで読み込む必要があると思う
            print("*************データをクレンジング中*************")
            data = pd.read_csv(self.csv_path)
            #まず全てNanの列を削除する
            data = data.dropna(how='all', axis=1)
            #print(data)
            #取得単位数の部分を取り出す  ■合計を認識して列行の位置を特定
            def grade_search(search_word):
                for ncol in data.columns:
                    judge = data.loc[:, ncol].isnull().sum()  # 各列にNaNがいくつあるか
                    if judge == 0:  # 列に全て値が入っている場合(科目)
                        place = data.loc[:, ncol].str.startswith(search_word)
                    elif judge > 0:  # 一つでもNaNがある場合エラーになるのでnaの引数指定 naをfalseにするというもの
                        place = data.loc[:, ncol].str.startswith(
                            search_word, na=False)  # naに反応している
                    else:
                        pass

                    if sum(place) > 0:  # ■合計が判定されたらbreak
                        break
                # place = "■合計"が入っている列の全行がplaceにあるからそこから行番号を取得する
                gyo = 0
                for i in range(0, len(place)):
                    if place.iloc[i, ] == True:
                        gyo = i
                        retu = place.name
                        # gyoは"■合計の行"、"■合計の列"がretu
                return gyo, retu

            total_place = grade_search('■合計')
            #print(total_place)
            #Total credits earned(総修得単位合計)
            TCE_place = grade_search('■●総修得単位合計(■と●の合計単位数)')
            #print(TCE_place)

            ##################取得単位数のデータフレーム整理#######################
            aggregation_df = data.iloc[total_place[0]:TCE_place[0]+1, :]   # これは変えないとダメ
            aggregation_df = aggregation_df.loc[:, total_place[1]:]
            aggregation_df = aggregation_df.dropna(how='all', axis=1)
            aggregation_df = aggregation_df.dropna(how='all')

            # aggregation_dfの３列目の最後のみを入れる
            target_col = len(aggregation_df.columns) - 1
            for row in range(0, len(aggregation_df)):
                # データフレームの３列目の値を１つずつ取り出す
                target = aggregation_df.iloc[row, target_col]
                # NaNのときfloatになるので、Errorになる
                if pd.isna(target):  # NaNのとき
                    pass
                else:
                    space_index = target.rfind(' ')  # 最後のスペースを判定
                    aggregation_df.iloc[row, target_col] = target[space_index+1::]
            aggregation_df.columns = ['単位習得状況', '必要単位数', '合計']
            
            print("*************データをベースを作成中*************")
            #データベース作成
            dbname = ('Individual_Database.db')  # データベース名.db拡張子で設定
            # データベースを作成、自動コミット機能ON
            conn = sqlite3.connect(dbname, isolation_level=None)
            cursor = conn.cursor()  # カーソルオブジェクトを作成
            table_name = "summary"
            aggregation_df.to_sql(table_name, con=conn, index=False)
            cursor.close()  # データベースを閉じる

        ##[成績を読み込む]ボタン押下時の関数
        def read_file_command():
            print('成績を読み込むボタンが押されました')
            self.file_path = self.file_frame.edit_box.get()
            print(self.file_path)

            ####パスワード####
            self.password = self.pasword_entry.get()
            print(self.password)
            print("")

            if len(self.file_path) != 0:
                #パスワードの解除　（新しいファイルパス）
                self.file_path = unlock_command()
                print("パスワード解除済みファイルパス;", self.file_path)

                #ファイルの読み込み
                self.csv_path = file_read()  # csvのファイルパスが返ってくる
                print("pdfからcsvに変換したcsvファイルパス;", self.csv_path)

                #プレビュー
                imgfile_path = create_preview()
                print("プレビュー用の画像ファイルパス;", imgfile_path)

                img = Image.open(imgfile_path)
                img_resize = img.resize((400, 300))
                # 読み込んだ結果を画面に描画
                self.img_canvas.Photo = ImageTk.PhotoImage(img_resize)
                self.img_canvas.create_image(
                    0, 0, image=self.img_canvas.Photo, anchor=tk.NW)
                os.remove(imgfile_path)

                #データクレンジング(個人用のデータベース作成)
                cleansing()

            else:
                print("ファイルを選択してください")
        
        def next_func():
            #time.sleep(5)
            self.file_frame.grid_forget()
            select_subject = frame2.ClassRegistration(root)

        def back_func():
            self.file_frame.grid_forget()
            select_subject = topframe.Topframe(root)

        def selfselect_credits():
            self.file_frame.grid_forget()
            # pdfの読み込みに失敗した場合、自分で入力するフォーに切り替える
            ssc = self_select.self_input_credit(root)
