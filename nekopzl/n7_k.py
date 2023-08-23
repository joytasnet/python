import tkinter as tk
import random

cursor_x=cursor_y=0
mouse_x=mouse_y=mouse_c=0

def mouse_move(e):
    global mouse_x,mouse_y
    mouse_x,mouse_y=e.x,e.y

def mouse_press(e):
    global mouse_c
    mouse_c=1


neko = []
check = []
for i in range(10):
    neko.append([0]*8)
    check.append([0]*8)

def draw_neko():
    for y in range(10):
        for x in range(8):
            if neko[y][x] == 0:continue
            cvs.create_image(x*72+60,y*72+60,image=img_neko[neko[y][x]],tag="NEKO")

def check_neko():
    for y in range(10):
        for x in range(8):
            check[y][x] = neko[y][x]
    #縦の判定
    for y in range(1,9):
        for x in range(8):
            if check[y][x] == 0:continue
            if check[y-1][x] == check[y][x] == check[y+1][x]:
                neko[y-1][x]=neko[y][x]=neko[y+1][x]=7

    #横の判定
    for y in range(10):
        for x in range(1,7):
            if check[y][x] == 0:continue
            if check[y][x-1] == check[y][x] == check[y][x+1]:
                neko[y][x-1] = neko[y][x] = neko[y][x+1]=7
    #斜めの判定
    for y in range(1,9):
        for x in range(1,7):
            if check[y][x] == 0:continue
            if check[y-1][x-1] == check[y][x] == check[y+1][x+1]:
                neko[y-1][x-1]=neko[y][x]=neko[y+1][x+1]=7
            if check[y+1][x-1] == check[y][x] == check[y-1][x+1]:
                neko[y+1][x-1]=neko[y][x]=neko[y-1][x+1]=7



def drop_neko():
    for y in range(8,-1,-1):
        for x in range(8):
            if neko[y][x] != 0 and neko[y+1][x] == 0:
                neko[y+1][x] = neko[y][x]
                neko[y][x]=0
def game_main():
    global cursor_x,cursor_y,mouse_c
    if 660 <=mouse_x <840 and 100 <= mouse_y < 160 and mouse_c == 1:
        mouse_c=0
        check_neko()

    if 24 <= mouse_x < 24+72*8 and 24 <=mouse_y < 24+72*10:
        cursor_x=int((mouse_x-24)/72)
        cursor_y=int((mouse_y-24)/72)
        if mouse_c==1:
            mouse_c=0
            neko[cursor_y][cursor_x]=random.randint(1,2)
    cvs.delete("CURSOR")
    cvs.create_image(cursor_x*72+60,cursor_y*72+60,image=cursor,tag='CURSOR')
    cvs.delete("NEKO")
    draw_neko()
    root.after(100,game_main)

root=tk.Tk()
root.title("二次元リストでマスを管理する")
root.resizable(False,False)
root.bind('<Motion>',mouse_move)
root.bind('<ButtonPress>',mouse_press)
cvs=tk.Canvas(root,width=912,height=768)
cvs.pack()

bg=tk.PhotoImage(file='neko_bg.png')
cursor=tk.PhotoImage(file='neko_cursor.png')
img_neko=[
        None,
        tk.PhotoImage(file='neko1.png'),
        tk.PhotoImage(file='neko2.png'),
        tk.PhotoImage(file='neko3.png'),
        tk.PhotoImage(file='neko4.png'),
        tk.PhotoImage(file='neko5.png'),
        tk.PhotoImage(file='neko6.png'),
        tk.PhotoImage(file='neko_niku.png'),
        ]
cvs.create_image(456,384,image=bg)
cvs.create_rectangle(660,100,840,160,fill='white')
cvs.create_text(750,130,text='テスト',fill='red',font=('Times New Roman',30))
game_main()
root.mainloop()

