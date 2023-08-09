import random

#counter変数countを0で初期化
count  = 0

#whileを使って無限ループを作成
while True:
    #countを1増やす
    count +=1

    #1-9999の乱数を生成
    n = random.randint(1,9999)

    #[1: 321]このようなフォーマットで表示
    print(f'{count}: {n}')

    #もし、7777だったらwhileループを抜ける
    if n == 7777:
        break

#何回で7777が出たのかを表示
print(f'{count}回で7777が出ました!')
