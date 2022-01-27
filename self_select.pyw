import tkinter as tk
from tkinter import ttk

class self_input_credit():

    def self_input(self,parent_frame):

        common_subject = ttk.Frame(parent_frame)
        human_subject_txt = tk.Label(common_subject, text = '人文科学科目群').grid(row = 0, column = 0, pady = 10)
        human_subject_entry = tk.Entry(common_subject, width =2)
        human_subject_entry.grid(row = 0, column = 1)
        natural_subject_txt = tk.Label(common_subject, text = '自然科学科目群').grid(row = 1, column = 0, pady = 10)
        natural_subject_entry = tk.Entry(common_subject, width =2)
        natural_subject_entry.grid(row = 1, column = 1)
        social_subject_txt = tk.Label(common_subject, text = '社会科学科目').grid(row = 2, column = 0, pady = 10)
        social_subject_entry = tk.Entry(common_subject, width =2)
        social_subject_entry.grid(row = 2, column = 1)
        comprehensive_subject_txt = tk.Label(common_subject, text = '総合科目群').grid(row = 3, column = 0, pady = 10)
        comprehensive_subject_entry = tk.Entry(common_subject, width =2)
        comprehensive_subject_entry.grid(row = 3, column = 1)
        eng_txt = tk.Label(common_subject, text = '英語').grid(row = 4, column = 0, pady = 10)
        eng__entry = tk.Entry(common_subject, width =2)
        eng__entry.grid(row = 4, column = 1)
        forig2_txt = tk.Label(common_subject, text = '第2外国語').grid(row = 5, column = 0, pady = 10)
        forig2_entry = tk.Entry(common_subject, width =2)
        forig2_entry.grid(row = 5, column = 1)
        physical_must_txt = tk.Label(common_subject, text = '健康・運動科目_1年必修').grid(row = 6, column = 0, pady = 10)
        physical_must_entry = tk.Entry(common_subject, width =2)
        physical_must_entry.grid(row = 6, column = 1)
        physical_select_txt = tk.Label(common_subject, text = '健康・運動科目_選択必修').grid(row = 7, column = 0, pady = 10)
        physical_select_entry = tk.Entry(common_subject, width =2)
        physical_select_entry.grid(row = 7, column = 1)
        common_subject.grid(row = 0, column =0)

        department_subject = ttk.Frame(parent_frame)
        basic_must1_txt = tk.Label(department_subject, text = '基本科目_1年次必須').grid(row = 0, column = 0, pady = 10)
        basic_must1_entry = tk.Entry(department_subject, width =2)
        basic_must1_entry.grid(row = 0, column = 1)
        basic_must2_txt = tk.Label(department_subject, text = '基本科目_2年次必須').grid(row = 1, column = 0, pady = 10)
        basic_must2_entry = tk.Entry(department_subject, width =2)
        basic_must2_entry.grid(row = 1, column = 1)
        basic_mselect_txt = tk.Label(department_subject, text = '基本科目_選択必修').grid(row = 2, column = 0, pady = 10)
        basic_mselect_entry = tk.Entry(department_subject, width =2)
        basic_mselect_entry.grid(row = 2, column = 1)
        apply_txt = tk.Label(department_subject, text = '応用科目').grid(row = 3, column = 0, pady = 10)
        apply_entry = tk.Entry(department_subject, width =2)
        apply_entry.grid(row = 3, column = 1)
        dep_common_txt = tk.Label(department_subject, text = '3学科共通関係科目').grid(row = 4, column = 0, pady = 10)
        dep_common_entry = tk.Entry(department_subject, width =2)
        dep_common_entry.grid(row = 4, column = 1)
        department_subject.grid(row = 0, column =1)


        other_subject = ttk.Frame(parent_frame)
        course_txt = tk.Label(other_subject, text = 'コース科目').grid(row = 0, column = 0, pady = 10)
        course_entry = tk.Entry(other_subject, width =2)
        course_entry.grid(row = 0, column = 1)
        special_training_txt = tk.Label(other_subject, text = '専門演習').grid(row = 1, column = 0, pady = 10)
        special_training_entry = tk.Entry(other_subject, width =2)
        special_training_entry.grid(row = 1, column = 1)
        old_reseach_txt = tk.Label(other_subject, text = '原典研究').grid(row = 2, column = 0, pady = 10)
        old_reseach_entry = tk.Entry(other_subject, width =2)
        old_reseach_entry.grid(row = 2, column = 1)
        total_sp_info_txt = tk.Label(other_subject, text = '総合講座・特殊講義・情報科目').grid(row = 3, column = 0, pady = 10)
        total_sp_info_entry = tk.Entry(other_subject, width =2)
        total_sp_info_entry.grid(row = 3, column = 1)
        application_txt = tk.Label(other_subject, text = '資格過程科目').grid(row = 4, column = 0, pady = 10)
        application_entry = tk.Entry(other_subject, width =2)
        application_entry.grid(row = 4, column = 1)
        global_txt = tk.Label(other_subject, text = 'グローバル・全学部共通科目').grid(row = 5, column = 0, pady = 10)
        global_entry = tk.Entry(other_subject, width =2)
        global_entry.grid(row = 5, column = 1)
        not_count_txt = tk.Label(other_subject, text = '卒業単位に含めない科目').grid(row = 4, column = 0, pady = 10)
        not_count_entry = tk.Entry(other_subject, width =2)
        not_count_entry.grid(row = 4, column = 1)
        other_subject.grid(row = 0, column =2)

        parent_frame.grid_columnconfigure(0, weight=1)
        parent_frame.grid_columnconfigure(1, weight=1)
        parent_frame.grid_columnconfigure(2, weight=1)


        def go_input():
            human_subject = human_subject_entry.get()
            natural_subject = natural_subject_entry.get()
            social_subject = social_subject_entry.get()
            comprehensive_subject = comprehensive_subject_entry.get()
            forign = forign__entry.get()
            eng = eng__entry.get()
            forig2 = forig2_entry.get()
            physical_must = physical_must_entry.get()
            physical_select = physical_select_entry.get()
            basic_must1 = basic_must1_entry.get()
            basic_must2 = basic_must2_entry.get()
            basic_mselect = basic_mselect_entry.get()
            dep_common = dep_common_entry.get()
            course =course_entry.get()
            special_training = special_training_entry.get()
            old_reseach = old_reseach_entry.get()
            total_sp_info = total_sp_info_entry.get()
            application = application_entry.get()
            get_global_entry = global_entry.get()
            not_count= not_count_entry.get()

        input_bt = tk.Button(parent_frame, text = '入力する', width = 15, command = go_input)
        input_bt.grid(row = 1, column = 0, columnspan = 3)

        parent_frame.rowconfigure(0, weight = 1)
        parent_frame.rowconfigure(1, weight = 1)


if __name__ == '__main__':
    root = tk.Tk()
    set_display = self_input_credit()
    set_display.self_input(root)
    root.geometry("1000x600")
    root.mainloop()
