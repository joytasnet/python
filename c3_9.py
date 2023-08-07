score = int(input('試験の点数を入力>>'))
if (score < 0 or score > 100):
    print('異常な値です')
    print('入力し直してください')
elif score >= 60:
    print('合格!')
    print('よくがんばりましたね')
else:
    print('不合格です')
    print('追試を受けてください')

