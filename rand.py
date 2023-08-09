import random

# 空っぽのリスト(変数名dices)を作成する
dices = [] #dices = list()

# 何回振るかを聞きその結果を変数countに代入
count = int(input('何回振る?>>'))

# count回回るforループを作成
for _ in range(count):

    # forループの中でサイコロの目をランダムに生成し、dicesにappendする
    dices.append(random.randint(1,6))

# forループを抜けた後にprint関数にdicesを渡して一覧表示
print(dices)

# sum関数を使って配列の合計を出力
print(f'合計は{sum(dices)}でした')
print(f'最大は{max(dices)}でした')
print(f'最小{min(dices)}でした')

