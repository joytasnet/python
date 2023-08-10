import random

print('サイコロ振ったよ')
d1=random.randint(1,6)
d2=random.randint(1,6)
print(f'1回目:{d1}')
print(f'2回目:{d2}')
print('2回目は1回目',end='')
if d1 == d2:
    print('と同じです')
elif d1 > d2:
    diff=d1-d2
    print(f'より{diff}小さいです')
else:
    diff=d2-d1
    print(f'より{diff}大きいです')

    
