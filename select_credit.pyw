import tkinter as tk
from tkinter import ttk

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
#選択単位リスト
selected = []

#各科目フレームフォーマット
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
        each_listbox = tk.Listbox(listbox_frame, listvariable = each_list_value, selectmode = 'multiple',yscrollcommand = each_scroll.set, height = 3)
        each_listbox.grid(row = 0, column = 0)
        each_scroll.grid(row = 0, column = 1)
        each_scroll ["command"]=each_listbox.yview

        each_sub_lb_bt_frame.grid(row = 0, column = 0)
        listbox_frame.grid(row = 1, column = 0)
        each_sub_frame.grid()


#選択画面表示の親フレーム
def parent_display_frame(parent_frame):
    ###表示における親フレーム
    display_frame = ttk.Frame(parent_frame)

    ###学科間共通科目フレーム ※以降subはsubjectの略-------------------------------------------------------------------
    common_sub_frame = ttk.Frame(display_frame)
    ##基礎科目フレーム
    basic_sub_frame = ttk.Frame(common_sub_frame)
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

    basic_sub_frame.grid(row = 0, column = 0, pady = 10)

    
    ##外国語
    forign_sub_frame = ttk.Frame(common_sub_frame)
    forign_sub_label = tk.Label(forign_sub_frame, text = '<外国語>').grid(row = 0, column = 0)
    #英語
    eng_sub_parent_frame = ttk.Frame(forign_sub_frame)
    eng_subject = each_sub_format(eng_sub_parent_frame, '英語', 英語, 'eng_sub_')
    eng_subject.set_each_sub_frame()
    eng_sub_parent_frame.grid(row = 1, column = 0)
    #第2外国語
    forign2_sub_parent_frame = ttk.Frame(forign_sub_frame)
    forign2_subject = each_sub_format(forign2_sub_parent_frame, '第2外国語', 第2外国語, 'forign2_sub_')
    forign2_subject.set_each_sub_frame()
    forign2_sub_parent_frame.grid(row = 2, column = 0)

    forign_sub_frame.grid(row = 1, column = 0, pady = 10)

    ##健康・運動
    Phy_sub_frame = ttk.Frame(common_sub_frame)
    Phy_sub_label = tk.Label(Phy_sub_frame, text = '<健康運動科目>').grid(row = 0, column = 0)
    #選択必修科目
    sle_phy_sub_parent_frame = ttk.Frame(Phy_sub_frame)
    sle_phy_subject = each_sub_format(sle_phy_sub_parent_frame, '選択必修科目', 健康運動科目, 'sle_phy_sub_')
    sle_phy_subject.set_each_sub_frame()
    sle_phy_sub_parent_frame.grid(row = 1, column = 0)

    Phy_sub_frame.grid(row = 2, column = 0, pady = 10)    

    common_sub_frame.grid(row = 0, column = 0, padx = 20)

    ##学科関係科目
    department_sub_frame = ttk.Frame(display_frame)
    ##政治学科
    Politics_sub_frame = ttk.Frame(department_sub_frame)
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

    Politics_sub_frame.grid(row = 0, column = 0)
    
    ##経済学科
    Economics_sub_frame = ttk.Frame(department_sub_frame)
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

    Economics_sub_frame.grid(row = 1, column = 0)

    ##地方行政学科
    Local_sub_frame = ttk.Frame(department_sub_frame)
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

    Local_sub_frame.grid(row = 2, column = 0)

    department_sub_frame.grid(row = 0, column = 1, padx = 20, pady = 10)

    ##専門演習
    Seminar_sub_frame = ttk.Frame(display_frame)
    ##ゼミ有
    in_seminar = ttk.Frame(Seminar_sub_frame)
    in_seminar_label = tk.Label(in_seminar, text = '<ゼミ有>').grid(row = 0, column = 0)
    #外国語・古典研究
    classic_reseach_parent_frame = ttk.Frame(in_seminar)
    classic_reseachject = each_sub_format(classic_reseach_parent_frame, '外国語・古典研究', 外国語古典研究, 'classic_reseach_')
    classic_reseachject.set_each_sub_frame()
    classic_reseach_parent_frame.grid(row = 1, column = 0)

    in_seminar.grid(row = 0, column = 0, pady = 30)

    ##ゼミなし
    no_seminar = ttk.Frame(Seminar_sub_frame)
    no_seminar_label = tk.Label(no_seminar, text = '<ゼミ無>').grid(row = 0, column = 0)
    #外国語・古典研究
    classic_subscribe_parent_frame = ttk.Frame(no_seminar)
    classic_subscribeject = each_sub_format(classic_subscribe_parent_frame, '古典講読', 古典講読, 'classic_subscribe_')
    classic_subscribeject.set_each_sub_frame()
    classic_subscribe_parent_frame.grid(row = 1, column = 0)
    #コース科目
    coas_sub_parent_frame = ttk.Frame(no_seminar)
    coas_subject = each_sub_format(coas_sub_parent_frame, 'コース科目', コース科目, 'coas_sub_')
    coas_subject.set_each_sub_frame()
    coas_sub_parent_frame.grid(row = 2, column = 0)

    no_seminar.grid(row = 1, column = 0, pady = 30)

    def register():
        pass

    all_register = tk.Button(Seminar_sub_frame, command = register, text = '登録して確認する')
    all_register.grid(row = 2, column = 0, pady = 30)

    Seminar_sub_frame.grid(row = 0, column = 2, padx =20)

    display_frame.grid()
    return display_frame



#フレームの配置
def set_main_frame(root_frame):
   set_parent_display = parent_display_frame(root_frame)


    
# メイン関数
if __name__ == '__main__':
    root = tk.Tk()
    root.title('選択画面')
    set_main_frame(root)
    root.mainloop()
