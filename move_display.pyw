import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from pikepdf import Pdf
from select_display_format import each_sub_format
from calendar import calender_frame

#リスト集
#学科間共通科目
人文科学科目群 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
社会科学科目群 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
自然科学科目群 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
総合科目群 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']

英語 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
第2外国語 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']

健康運動科目 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']

#学科別関係科目
政治基本科目A = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
政治基本科目B = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
政治応用科目 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']

経済基本科目A = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
経済基本科目B = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
経済応用科目 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']

地方行政基本科目A = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
地方行政応用科目 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']

#専門演習
外国語古典研究 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']

古典講読 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']
コース科目 = ['哲学概論', '哲学史', '基礎論理学', '論理学概論', '歴史学']


#学年
year = ['1年', '2年', '3年', '4年']
period = ['春学期', '秋学期']
selected_year = []
selected_period = []

#----------------------------------------------ファイル読み込み画面の設定-------------------------------------------------
##[ファイルを選択]ボタン押下時の関数
def open_file_command(edit_box, file_type_list):
    file_path = filedialog.askopenfilename(filetypes = file_type_list)
    edit_box.delete(0, tk.END)
    edit_box.insert(tk.END, file_path)

##[解除]ボタンを押下時の関数
def unlock_command(unlock_file,password):
    #pdfの解除
    pass

##[成績を読み込む]ボタン押下時の関数
def read_file_command(e):
    #pdfファイルの受け渡し
    select_credit.tkraise()
    print('READボタンが押されました')

## ファイル読み込み画面のラベル・エントリー・ボタンの設置
def set_file_frame(parent_frame, label_text, file_type_list):
    ##画面遷移用フレーム
    file_move_frame = ttk.Frame(parent_frame)
    file_move_frame.grid(row = 0, column = 0, sticky="nsew")
    ##ファイル読み込み画面における親フレーム
    file_frame = ttk.Frame(file_move_frame)
    file_frame.grid(padx = 350, pady = 100)
        #ファイル読み込みのラベル・テキストボックス・[ファイルを選択]ボタンを持つフレーム
    file_select_frame = ttk.Frame(file_frame)
    file_select_frame.grid(row = 0, column = 0, columnspan = 2, pady = 10)
        #ラベル
    tk.Label(file_select_frame, text = label_text).grid(row = 0, column = 0, pady = 10)
        #テキストボックス
    file_frame.edit_box = tk.Entry(file_select_frame, width = 50)
    file_frame.edit_box.grid(row = 1, column = 0, pady = 10)
        #[ファイルを選択]ボタン
    file_button = tk.Button(file_select_frame, text = 'ファイルを選択', width = 10\
        , command = lambda:open_file_command(file_frame.edit_box, file_type_list))
    file_button.grid(row = 2, column = 0, pady = 10)

    ##学年・学期選択
    select_year_period = ttk.Frame(file_frame)
    select_year_period.grid(row = 1, column = 0, padx = 5)
    ##学年コンボボックス関数
    def select_year(e):
        selected_year.append(year_cb.current()+1)
        print(selected_year)

    def select_period(e):
        selected_period.append(period_cb.current())
        print(selected_period)

        #学年・学期選択ラベル
    year_period_label = tk.Label(select_year_period, text = '学年と学期を選択してください')
    year_period_label.grid(row = 0, column = 0, columnspan = 2, pady = 10)
        #学年ラベル
    year_label = tk.Label(select_year_period, text = '<学年>').grid(row = 1, column = 0)
        #学年選択コンボボックス
    y = tk.StringVar()
    year_cb = ttk.Combobox(select_year_period, textvariable = y, values = year)
    year_cb.bind('<<ComboboxSelected>>', select_year)
    year_cb.grid(row=2, column=0)
        #学期ラベル
    period_label = tk.Label(select_year_period, text = '<学期>').grid(row = 1, column = 1)
        #学期選択
    p = tk.StringVar()
    period_cb = ttk.Combobox(select_year_period, textvariable = p, values = period)
    period_cb.bind('<<ComboboxSelected>>', select_period)
    period_cb.grid(row=2, column=1)    
    ##パスワード関連のフレーム
    pasword_frame = ttk.Frame(file_frame)
    pasword_frame.grid(row = 2, column = 0, padx = 5)
        #パスワード入力を促すラベル
    pasword_label = tk.Label(pasword_frame, text = '以下にパスワードを入力してください')
    pasword_label.grid(row = 0, column = 0, columnspan = 2, pady = 10)
        #パスワードの入力エントリー
    pasword_entry = tk.Entry(pasword_frame)
    pasword_entry.grid(row = 1, column = 0, pady = 10, padx = 10)
        #[ロックを解除]ボタン
    input_button = tk.Button(pasword_frame, text = 'ロックを解除', command = lambda:unlock_command(file_name,password))
    input_button.grid(row = 1, column = 1, pady = 10, padx = 10)

    ##[成績を読み込む]ボタンの設置
    read_frame = ttk.Frame(file_frame)
    read_frame.grid(row = 3, column = 0, pady = 10)
    read_button = tk.Button(read_frame, text = '成績を読み込む', width = 15)
    read_button.bind('<Button-1>',read_file_command)
    read_button.grid()
    
    return file_move_frame

#--------------------------------------------------講義選択画面設定------------------------------------------------------------
##<登録して確認する>ボタンが押された時の関数
def register():
    look_calendar.tkraise()

#選択画面表示の親フレーム
def set_select_display(parent_frame):
    ##画面遷移用フレーム
    select_move_frame = ttk.Frame(parent_frame)
    select_move_frame.grid(row = 0, column = 0, sticky="nsew")
    ##講義選択画面における親フレーム
    display_frame = ttk.Frame(select_move_frame)
    display_frame.grid(padx = 5)
        ##基礎科目フレーム
    basic_sub_frame = ttk.Frame(display_frame)
    basic_sub_frame.grid(row = 0, column = 0, pady = 10)
            #<基礎科目>ラベル
    basic_sub_label = tk.Label(basic_sub_frame, text = '<基礎科目群>').grid(row = 0, column = 0)
            #人文科学科目
    human_sub_parent_frame = ttk.Frame(basic_sub_frame)
    human_subject = each_sub_format(human_sub_parent_frame, '人文科学科目群', 人文科学科目群, 'human_sub_')
    human_subject.set_each_sub_frame()
    human_sub_parent_frame.grid(row = 1, column = 0)
            #社会科学科目
    social_sub_parent_frame = ttk.Frame(basic_sub_frame)
    social_subject = each_sub_format(social_sub_parent_frame, '社会科学科目群', 社会科学科目群, 'social_sub_')
    social_subject.set_each_sub_frame()
    social_sub_parent_frame.grid(row = 2, column = 0)
            #自然科学科目
    natural_sub_parent_frame = ttk.Frame(basic_sub_frame)
    natural_subject = each_sub_format(natural_sub_parent_frame, '自然科学科目群', 自然科学科目群, 'natural_sub_')
    natural_subject.set_each_sub_frame()
    natural_sub_parent_frame.grid(row = 3, column = 0)
            #総合科目
    comprehensivw_sub_parent_frame = ttk.Frame(basic_sub_frame)
    comprehensivw_subject = each_sub_format(comprehensivw_sub_parent_frame, '総科科目群', 総合科目群, 'comprehensivw_sub_')
    comprehensivw_subject.set_each_sub_frame()
    comprehensivw_sub_parent_frame.grid(row = 4, column = 0)

        ##外国語+健康
    forign_health_frame = ttk.Frame(display_frame)
    forign_health_frame.grid(row = 0, column = 1, pady = 10)
            #<外国語>ラベル
    forign_sub_label = tk.Label(forign_health_frame, text = '<外国語>').grid(row = 0, column = 0)
            #英語
    eng_sub_parent_frame = ttk.Frame(forign_health_frame)
    eng_subject = each_sub_format(eng_sub_parent_frame, '英語', 英語, 'eng_sub_')
    eng_subject.set_each_sub_frame()
    eng_sub_parent_frame.grid(row = 1, column = 0)
            #第2外国語
    forign2_sub_parent_frame = ttk.Frame(forign_health_frame)
    forign2_subject = each_sub_format(forign2_sub_parent_frame, '第2外国語', 第2外国語, 'forign2_sub_')
    forign2_subject.set_each_sub_frame()
    forign2_sub_parent_frame.grid(row = 2, column = 0)
            #<健康運動科目>ラベル
    Phy_sub_label = tk.Label(forign_health_frame, text = '<健康運動科目>').grid(row = 3, column = 0)
            #選択必修科目
    sle_phy_sub_parent_frame = ttk.Frame(forign_health_frame)
    sle_phy_subject = each_sub_format(sle_phy_sub_parent_frame, '選択必修科目', 健康運動科目, 'sle_phy_sub_')
    sle_phy_subject.set_each_sub_frame()
    sle_phy_sub_parent_frame.grid(row = 4, column = 0)

        ##政治学科
    Politics_sub_frame = ttk.Frame(display_frame)
    Politics_sub_frame.grid(row = 0, column = 3)
            #<政治学科>ラベル
    Politics_sub_label = tk.Label(Politics_sub_frame, text = '<政治学科>').grid(row = 0, column = 0)
            #1・2年取得可能基本科目
    PbasicA_sub_parent_frame = ttk.Frame(Politics_sub_frame)
    PbasicA_subject = each_sub_format(PbasicA_sub_parent_frame, '1・2年取得可能基本科目', 政治基本科目A, 'PbasicA_sub_')
    PbasicA_subject.set_each_sub_frame()
    PbasicA_sub_parent_frame.grid(row = 1, column = 0)
            #3・4年取得可能基本科目
    PbasicB_sub_parent_frame = ttk.Frame(Politics_sub_frame)
    PbasicB_subject = each_sub_format(PbasicB_sub_parent_frame, '3・4年取得可能基本科目', 政治基本科目B, 'PbasicB_sub_')
    PbasicB_subject.set_each_sub_frame()
    PbasicB_sub_parent_frame.grid(row = 2, column = 0)
            #3・4年取得可能基本科目
    Papply_sub_parent_frame = ttk.Frame(Politics_sub_frame)
    Papply_subject = each_sub_format(Papply_sub_parent_frame, '3・4年取得可能応用科目', 政治応用科目, 'Papply_sub_')
    Papply_subject.set_each_sub_frame()
    Papply_sub_parent_frame.grid(row = 3, column = 0)

        ##経済学科
    Economics_sub_frame = ttk.Frame(display_frame)
    Economics_sub_frame.grid(row = 0, column = 4)
            #<経済学科>ラベル
    Economics_sub_label = tk.Label(Economics_sub_frame, text = '<経済学科>').grid(row = 0, column = 0)
            #1・2年取得可能基本科目
    EbasicA_sub_parent_frame = ttk.Frame(Economics_sub_frame)
    EbasicA_subject = each_sub_format(EbasicA_sub_parent_frame, '1・2年取得可能基本科目', 経済基本科目A, 'EbasicA_sub_')
    EbasicA_subject.set_each_sub_frame()
    EbasicA_sub_parent_frame.grid(row = 1, column = 0)
            #3・4年取得可能基本科目
    EbasicB_sub_parent_frame = ttk.Frame(Economics_sub_frame)
    EbasicB_subject = each_sub_format(EbasicB_sub_parent_frame, '3・4年取得可能基本科目', 経済基本科目B, 'EbasicB_sub_')
    EbasicB_subject.set_each_sub_frame()
    EbasicB_sub_parent_frame.grid(row = 2, column = 0)
            #3・4年取得可能基本科目
    Eapply_sub_parent_frame = ttk.Frame(Economics_sub_frame)
    Eapply_subject = each_sub_format(Eapply_sub_parent_frame, '3・4年取得可能応用科目', 経済応用科目, 'Eapply_sub_')
    Eapply_subject.set_each_sub_frame()
    Eapply_sub_parent_frame.grid(row = 3, column = 0)

        ##地方行政学科
    Local_sub_frame = ttk.Frame(display_frame)
    Local_sub_frame.grid(row = 0, column = 5)
            #<地域行政学科>ラベル
    Local_sub_label = tk.Label(Local_sub_frame, text = '<地方行政学科>').grid(row = 0, column = 0)
            #1・2年取得可能基本科目
    LbasicA_sub_parent_frame = ttk.Frame(Local_sub_frame)
    LbasicA_subject = each_sub_format(LbasicA_sub_parent_frame, '1・2年取得可能基本科目', 地方行政基本科目A, 'LbasicA_sub_')
    LbasicA_subject.set_each_sub_frame()
    LbasicA_sub_parent_frame.grid(row = 1, column = 0)
            #3・4年取得可能基本科目
    Lapply_sub_parent_frame = ttk.Frame(Local_sub_frame)
    Lapply_subject = each_sub_format(Lapply_sub_parent_frame, '3・4年取得可能応用科目', 地方行政応用科目, 'Lapply_sub_')
    Lapply_subject.set_each_sub_frame()
    Lapply_sub_parent_frame.grid(row = 2, column = 0)

        ##ゼミ有
    seminar = ttk.Frame(display_frame)
    seminar.grid(row = 0, column = 6, pady = 30)
            #<ゼミ有>ラベル
    in_seminar_label = tk.Label(seminar, text = '<ゼミ有>').grid(row = 0, column = 0)
            #外国語・古典研究
    classic_reseach_parent_frame = ttk.Frame(seminar)
    classic_reseachject = each_sub_format(classic_reseach_parent_frame, '外国語・古典研究', 外国語古典研究, 'classic_reseach_')
    classic_reseachject.set_each_sub_frame()
    classic_reseach_parent_frame.grid(row = 1, column = 0)
            #<ゼミ無>ラベル
    no_seminar_label = tk.Label(seminar, text = '<ゼミ無>').grid(row = 2, column = 0)
            #外国語・古典研究
    classic_subscribe_parent_frame = ttk.Frame(seminar)
    classic_subscribeject = each_sub_format(classic_subscribe_parent_frame, '古典講読', 古典講読, 'classic_subscribe_')
    classic_subscribeject.set_each_sub_frame()
    classic_subscribe_parent_frame.grid(row = 3, column = 0)
            #コース科目
    coas_sub_parent_frame = ttk.Frame(seminar)
    coas_subject = each_sub_format(coas_sub_parent_frame, 'コース科目', コース科目, 'coas_sub_')
    coas_subject.set_each_sub_frame()
    coas_sub_parent_frame.grid(row = 4, column = 0)
            #<登録して確認する>ボタン
    all_register = tk.Button(seminar, command = register, text = '登録して確認する', height = 5)
    all_register.grid(row = 5, column = 0, pady = 30)

    return select_move_frame


# メイン関数
if __name__ == '__main__':
    root = tk.Tk()
    root.title('syllabetai')
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.geometry("1000x600")
    set_file = set_file_frame(root, "自分の成績表pdfを入れて下さい", [('Chrome HTML Document (.pdf)', '*pdf')])
    select_credit = set_select_display(root)
    look_calendar = calender_frame(root)
    set_file.tkraise()
    root.mainloop()
