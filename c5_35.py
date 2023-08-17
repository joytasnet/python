name='松田'
a=10

def change_name():
    global name
    name ='浅木'

def hello():
    print('こんにちは',name,'さん')

change_name()
hello()
