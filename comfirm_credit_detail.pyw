import tkinter as tk
from tkinter import ttk

#基礎科目群
basic_variable_name = ['h_sience_subject', 's_sience_subject','n_sience_subject','comp_subject','rest_basic_subject','basic_total']
basic_subject_text = ['人文科学科目','社会科学科目','自然科学科目','総合科目','以上4科目から残り','合計']
basic_subject_must = ['/4','/4','/4','/4','/12','/28']
basic_subject_can_sum = 0
basic_subject_can = [0,0,0,0,0,basic_subject_can_sum]

#外国語科目群
lang_variable_name = ['eng_subject', 'sec_lang_subject','rest_lang_subjct','lang_total']
lang_subject_text = ['英語','第二外国語','以上に2科目から残り','合計']
lang_subject_must = ['/6','/8','/2','/16']
lang_subject_can_sum = 0
lang_subject_can = [0,0,0,lang_subject_can_sum]

#運動・健康科目群
physical_variable_name = ['spe_phy_subject', 'sel_physical_subject','physical_total']
physical_subject_text = ['指定必須単位','選択必須単位','合計']
physical_subject_must = ['/2','/2','/4']
physical_subject_can_sum = 0
physical_subject_can = [0,0,physical_subject_can_sum]

#政治学科科目群
plo_relative_variable_name = ['1_pol', '2_pol','3_4_pol','rest_pol_relative','pol_rerative_total']
plo_relative_text = ['一年次指定必須単位','二年次指定必須単位','三・四年次選択必須単位','基本科目・応用科目より','合計']
plo_relative_must = ['/10','/4','/12','/16','/42']
plo_relative_can_sum = 0
plo_relative_can = [0,0,0,0,plo_relative_can_sum]

#経済学科科目群
eco_relative_variable_name = ['1_eco','3_4_eco','rest_eco_relative','eco_rerative_total']
eco_relative_text = ['一年次指定必須単位','三・四年次選択必須単位','基本科目・応用科目より','合計']
eco_relative_must = ['/14','/12','/16','/42']
eco_relative_can_sum = 0
eco_relative_can = [0,0,0,eco_relative_can_sum]

#地域行政学科科目群
local_relative_variable_name = ['1_local','2_local','rest_local_relative','local_rerative_total']
local_relative_text = ['一年次指定必須単位','二年次指定必須単位','基本科目・応用科目より','合計']
local_relative_must = ['/12','/18','/12','/42']
local_relative_can_sum = 0
local_relative_can = [0,0,0,eco_relative_can_sum]

#専門演習履修者
special_exercise_variable_name = ['forign_clasic','graduation_thesis']
special_exercise_text = ['専門演習(外国書・原典研究)','専門演習(卒業論文)']
special_exercise_must = ['/4','/8']
special_exercise_can = [0,0]

#専門演習不履修者
n_special_variable_name = ['forign_clasic','graduation_thesis']
n_special_text = ['原典講読','選択コース科目']
n_special_must = ['/4','/20']
n_special_can = [0,0]

#全単位合計
credit_total = 0


###表示フレーム
def display_set_frame(parent_frame):
    display_frame = ttk.Frame(parent_frame)
    display_frame.pack()


    ##科目群表示フォーマット
    def subject_group_format(group_name,variable_name,subject_text, can_get_credit, must_get_credit,subject_outline):
        #項目をまとめるフレーム
        group_frame = ttk.Frame(subject_outline)
        group_frame.pack(pady = 10 , padx = 10)
        group_name_text = '<{}>'.format(group_name)
        group_label = tk.Label(group_frame, text = group_name_text, font=(10)).pack(side = tk.TOP, pady = 3)
        #項目ごとのフレーム・ラベル・エントリー配置
        for i in range(len(variable_name)):
            variable_name[i] = ttk.Frame(group_frame)
            variable_name[i].pack(pady = 3)
            tk.Label(variable_name[i], text = subject_text[i]).pack(side = tk.LEFT)
            get_credit_num = tk.Entry(variable_name[i], width = 2)
            get_credit_num.insert(0,can_get_credit[i])
            get_credit_num.pack(side = tk.LEFT)
            tk.Label(variable_name[i], text = must_get_credit[i]).pack(side = tk.LEFT)
            
        return group_name



##共通科目フレーム
    common_subject = ttk.Frame(display_frame)
    common_subject.pack(side = tk.LEFT,padx = 7)
    #基礎科目群表示
    subject_group_format('基礎科目群',basic_variable_name,basic_subject_text,basic_subject_can,basic_subject_must,common_subject)
    #外国語科目群表示
    subject_group_format('外国語科目群',lang_variable_name,lang_subject_text,lang_subject_can,lang_subject_must,common_subject)
    #健康・運動科目表示
    subject_group_format('健康・運動科目群',physical_variable_name,physical_subject_text,physical_subject_can,physical_subject_must,common_subject)



##学科別科目フレーム
    department_subject = ttk.Frame(display_frame)
    department_subject.pack(side = tk.LEFT,padx = 7)
    #政治学科関係科目
    subject_group_format('政治学科関係科目',plo_relative_variable_name,plo_relative_text,plo_relative_can,plo_relative_must,department_subject)
    #経済学科関係科目
    subject_group_format('経済学科関係科目',eco_relative_variable_name,eco_relative_text,eco_relative_can,eco_relative_must,department_subject)
    #地域行政学科関係科目
    subject_group_format('地域行政学科関係科目',local_relative_variable_name,local_relative_text,local_relative_can,local_relative_must,department_subject)



##専門演習・コース科目フレーム
    SpecialAndCourse_subject = ttk.Frame(display_frame)
    SpecialAndCourse_subject.pack(side = tk.TOP,padx = 7)

    #専門演習履修パターン
    subject_group_format('専門演習履修者',special_exercise_variable_name,special_exercise_text,special_exercise_can,special_exercise_must,SpecialAndCourse_subject)
    #専門演習不履修パターン
    subject_group_format('専門演習不履修者',n_special_variable_name,n_special_text,n_special_can,n_special_must,SpecialAndCourse_subject)

##政治経済学部必須単位合計及び取得単位合計数
    total_frame = ttk.Frame(display_frame)
    total_frame.pack(pady = 10 , padx = 10, side = tk.BOTTOM)

    tk.Label(total_frame, text = '◎合計取得単位数', font=(8)).pack(side = tk.TOP, pady = 3)
    total_entry = tk.Entry(total_frame, width = 3)
    tk.Label(total_frame, text = '/124').pack(side = tk.RIGHT)
    total_entry.insert(0, credit_total)
    total_entry.pack(side = tk.RIGHT)


    return display_frame



##フレームを作成する関数を呼び出して配置
def set_main_frame(root_frame):
    explain_label = tk.Label(root_frame, text = '※①既得の単位と②選択した授業で取れる単位を足した単位数を確認できます。')
    explain_label.pack()
    set_display_frame = display_set_frame(root_frame)
    set_display_frame.pack()



###メイン関数
if __name__ == '__main__':
    root = tk.Tk()
    root.title('選択画面')
    #root.geometry("600x400")
    set_main_frame(root)
    root.mainloop()