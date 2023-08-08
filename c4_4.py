is_awake = True
count = 0
while is_awake == True:
    count += 1
    print(f'ひつじが{count}匹')
    key = input('もうそろそろ眠りそうですか(y/n) >>')
    if key == 'y':
        is_awake = False
print('おやすみなさい')
