student_list = ['浅木','松田']
for student in student_list:
    print(f'{student}さんの試験結果を入力してください>>')
    network=int(input('ネットワークの得点?>>'))
    database=int(input('データベースの得点?>>'))
    security=int(input('セキュリティの得点?>>'))
    if student == '浅木':
        asagi_scores=[network,database,security]
        asagi_avg=sum(asagi_scores) / len(asagi_scores)
    else:
        matsuda_scores=[network,database,security]
        matsuda_avg=sum(matsuda_scores) / len(matsuda_scores)

print(f'浅木さんの平均点は{asagi_avg}です')
print(f'松田さんの平均点は{matsuda_avg}です')

