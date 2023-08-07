isError = False
n = 50
if isError == False and n < 100:
    print('ok')

print('優' if n > 80 else '良' if n > 60 else '可' if n > 40 else '不可')

num = int(input('数値>>'))
print('偶数' if num % 2 == 0 else '奇数')
"""
if num % 2 == 0:
    print('偶数')
else:
    print('奇数')
"""

aisatsu = input('挨拶>>')

if aisatsu == 'こんにちは':
    print('ようこそ!')
elif aisatsu == '景気は?':
    print('ぼちぼちです')
elif aisatsu == 'さようなら':
    print('お元気で!')
else:
    print('どうしました?')

