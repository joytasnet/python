import tkinter as tk
root=tk.Tk()
root.title('My Window') #タイトルを設定
canvas = tk.Canvas(root,width=400,height=600,bg='skyblue')
canvas.pack()
img = tk.PhotoImage(file='iroha.png')
canvas.create_image(200,300,image=img)
root.mainloop()
