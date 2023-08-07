scores = []
scores.append(int(input('国語>>')))
scores.append(int(input('算数>>')))
scores.append(int(input('理科>>')))
scores.apeend(int(input('社会>>')))
scores.apeend(int(input('英語>>')))
print(f'合計:{sum(scores)}')
print(f'平均:{sum(scores)/len(scores)}')
