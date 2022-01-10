import tkinter as tk
from tkinter import ttk

#授業の情報を受け取るリスト
accept_data = {'m1':['統計学','永原'], 'm2':['統計学','永原'], 'm3':['統計学','永原'], 'm4':['統計学','永原'], 'm5':['統計学','永原'],
'tu1':['統計学','永原'], 'tu2':['',''], 'tu3':['統計学','永原'], 'tu4':['統計学','永原'], 'tu5':['統計学','永原'],
'w1':['統計学','永原'], 'w2':['統計学','永原'], 'w3':['統計学','永原'], 'w4':['統計学','永原'], 'w5':['統計学','永原'],
'th1':['統計学','永原'], 'th2':['統計学','永原'], 'th3':['統計学','永原'], 'th4':['統計学','永原'], 'th5':['統計学','永原'],
'f1':['統計学','永原'], 'f2':['統計学','永原'], 'f3':['統計学','永原'], 'f4':['統計学','永原'], 'f5':['統計学','永原'],
's1':['統計学','永原'], 's2':['統計学','永原'], 's3':['統計学','永原'], 's4':['統計学','永原'], 's5':['統計学','永原'], }

#月~土・1~5限の計36のリスト
week = ['m','tu','w','th','f','s']
DefLabel = []
for w in week:
  for t in range(1,6):
    name = str(w)+str(t)
    DefLabel.append([name, week.index(w)+1, t, accept_data[name]])

#カレンダーの作成関数
def calender_frame(parent_frame):
  #カレンダー表示フレーム
  calender_top_frame = ttk.Frame(parent_frame)
  calender_top_frame.pack(padx = 30 , pady = 30)
  #行・列名の作成
  w_m = tk.Label(calender_top_frame, text = '月')
  w_m.grid(column = 1, row = 0, sticky = tk.N +tk.E + tk.S + tk.W)
  w_tu = tk.Label(calender_top_frame, text = '火')
  w_tu.grid(column = 2, row = 0, sticky = tk.N +tk.E + tk.S + tk.W)
  w_w = tk.Label(calender_top_frame, text = '水')
  w_w.grid(column = 3, row = 0, sticky = tk.N +tk.E + tk.S + tk.W)
  w_th = tk.Label(calender_top_frame, text = '木')
  w_th.grid(column = 4, row = 0, sticky = tk.N +tk.E + tk.S + tk.W)
  w_f = tk.Label(calender_top_frame, text = '金')
  w_f.grid(column = 5, row = 0, sticky = tk.N +tk.E + tk.S + tk.W)
  w_st = tk.Label(calender_top_frame, text = '土')
  w_st.grid(column = 6, row = 0, sticky = tk.N +tk.E + tk.S + tk.W)
  t_1 = tk.Label(calender_top_frame, text = '1限目')
  t_1.grid(column = 0, row = 1, sticky = tk.N +tk.E + tk.S + tk.W)
  t_2 = tk.Label(calender_top_frame, text = '2限目')
  t_2.grid(column = 0, row = 2, sticky = tk.N +tk.E + tk.S + tk.W)
  t_3 = tk.Label(calender_top_frame, text = '3限目')
  t_3.grid(column = 0, row = 3, sticky = tk.N +tk.E + tk.S + tk.W)
  t_4 = tk.Label(calender_top_frame, text = '4限目')
  t_4.grid(column = 0, row = 4, sticky = tk.N +tk.E + tk.S + tk.W)
  t_5 = tk.Label(calender_top_frame, text = '5限目')
  t_5.grid(column = 0, row = 5, sticky = tk.N +tk.E + tk.S + tk.W)
  #リストの配置
  for name, c, r, l in DefLabel:
    name = ttk.Frame(calender_top_frame)
    name.grid(column = c, row = r, sticky = tk.N +tk.E + tk.S + tk.W, padx = 5, pady = 5)
    lecture_name = tk.Entry(name, font = 'MSゴシック 9')
    lecture_name.insert(0, l[0])
    lecture_name.pack()
    teacher_name = tk.Entry(name, font = 'MSゴシック 8')
    teacher_name.insert(0,l[1])
    teacher_name.pack()
  return calender_top_frame
  




def set_main_frame(root_frame):
  calender_frame(root_frame)

# メイン関数
if __name__ == '__main__':
    root = tk.Tk()
    root.title('時間割')
    #root.geometry("500x250")
    root.option_add('*Label.font', 'ＭＳゴシック 15')
    set_main_frame(root)
    root.mainloop()




