import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pikepdf import Pdf

##[ファイルを選択]ボタン押下時に呼び出し。選択したファイルのパスをテキストボックスに設定する。
def open_file_command(edit_box, file_type_list):
    file_path = filedialog.askopenfilename(filetypes = file_type_list)
    edit_box.delete(0, tk.END)
    edit_box.insert(tk.END, file_path)

##[解除]ボタンを押下時に呼び出し。pdfのロックを解除
def unlock_command(unlock_file,password):
    pass


### ファイル設定エリアのフレームを作成して返却する関数
def set_file_frame(parent_frame, label_text, file_type_list):
    file_frame = ttk.Frame(parent_frame)

    ##AとBがあるフレーム
    file_select_frame = ttk.Frame(file_frame)
    file_select_frame.pack()
    #A:テキストボックスの作成と配置
    tk.Label(file_select_frame, text = label_text).pack(side = tk.TOP)
    file_frame.edit_box = tk.Entry(file_select_frame, width = 50)
    file_frame.edit_box.pack(side = tk.LEFT)
    #B:ボタンの作成と配置
    file_button = tk.Button(file_select_frame, text = 'ファイルを選択', width = 10\
        , command = lambda:open_file_command(file_frame.edit_box, file_type_list))
    file_button.pack(side = tk.LEFT)

    ##CDEがを配置するフレーム
    pasword_frame = ttk.Frame(file_frame)
    pasword_frame.pack()
    #C:パスワード入力画面
    pasword_label = tk.Label(pasword_frame, text = '以下にパスワードを入力してください')
    pasword_label.pack()
    #D:入力エントリー
    pasword_entry = tk.Entry(pasword_frame)
    pasword_entry.pack(side = tk.LEFT)
    #E:入力ボタン
    input_button = tk.Button(pasword_frame, text = 'ロックを解除', command = lambda:unlock_command(file_name,password))
    input_button.pack(side = tk.LEFT)
    
    return file_frame


##[成績を読み込む]ボタン押下時に呼び出し。表示されているPDFを読み込む
def read_file_command(e):
    #pdfファイルの受け渡し
    #講義選択画面への移動
    print('READボタンが押されました')

##ファイル読み込みボタンエリアのフレーム作成、及び[成績を読み込む]ボタンの設置
def read_file_frame(parent_frame):
    read_frame = ttk.Frame(parent_frame)
    ##ボタンの設置
    read_button = tk.Button(read_frame, text = '成績を読み込む', width = 15)
    read_button.bind('<Button-1>',read_file_command)
    read_button.pack()
    return read_frame


##フレームを作成する関数を呼び出して配置
def set_main_frame(root_frame):
    #ファイル選択エリア作成（ファイルの拡張子を指定）
    file_set_frame = set_file_frame(root_frame, "自分の成績表pdfを入れて下さい"
    , [('Chrome HTML Document (.pdf)', '*pdf')])
    file_set_frame.pack(pady = 5)
    file_read_frame = read_file_frame(root_frame)
    file_read_frame.pack()
    
# メイン関数
if __name__ == '__main__':
    root = tk.Tk()
    root.title('成績表読み込み画面')
    #root.geometry("600x400")
    set_main_frame(root)
    root.mainloop()