import random
import turtle
#亀配列
ts = ['blue','red','yellow','brown','green']

def setup():
    global ts
    #画面生成
    screen=turtle.Screen()
    #画面サイズ設定
    screen.setup(1290,720)
    #背景画像設定
    screen.bgpic('pavement.gif')
    #スタートのx座標の値
    startline=-620

    for i in range(len(ts)):
        t=turtle.Turtle()
        t.shape('turtle')
        t.color(ts[i])
        t.penup()
        t.setpos(startline,(len(ts)//2)*-40+40*i)
        t.pendown()
        ts[i]=t
def race():
    global ts
    finishline=540

    while True:
        for current_t in ts:
            move=random.randint(0,20)
            current_t.forward(move)

            x=current_t.xcor()
            #ゴールしたかの判定
            if x >= finishline:
                winner_color=current_t.color()
                current_t.write('Win!'+winner_color[0],font=('Arial',16,'bold'))
                return
setup()
race()
turtle.mainloop()
