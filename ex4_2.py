count = 0
print('カレーを召し上がれ')
while True:
    count += 1
    print(f'{count}皿のカレーを食べました')
    ans = input('おかわりはいかがですか(y/n)>>')
    if ans != 'y':
        break
print('ごちそうさまでした')
