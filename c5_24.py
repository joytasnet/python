def eat(breakfast,lunch='ラーメン',dinner='カレー'):
    print(f'朝は{breakfast}を食べました')
    print(f'昼は{lunch}を食べました')
    print(f'晩は{dinner}を食べました')

print('8月1日')
eat(breakfast='納豆ごはん',dinner='カレーうどん')
print('8月2日')
eat(dinner='カレーうどん',breakfast='納豆ごはん')
print('8月3日')
eat('納豆ごはん',dinner='カレーうどん')
