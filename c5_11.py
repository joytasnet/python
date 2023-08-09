def calc_average(scores):
    avg = sum(scores) / len(scores)
    print(f'平均点は{avg:.1f}です')

student_list = ['浅木','松田']
for student in student_list:
    print(f'{student}さんの試験結果を入力してください>>')
    network=int(input('ネットワークの得点?>>'))
    database=int(input('データベースの得点?>>'))
    security=int(input('セキュリティの得点?>>'))
    if student == '浅木':
        asagi_scores=[network,database,security]
        calc_average(asagi_scores)
    else:
        matsuda_scores=[network,database,security]
        calc_average(matsuda_scores)


