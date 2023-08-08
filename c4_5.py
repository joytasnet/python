count = 0
student_num = int(input('学生の数を入力>>'))
score_list=list()
while count < student_num:
    count+=1
    score=int(input(f'{count}人目の試験の得点を入力>>'))
    score_list.append(score)
print(score_list)
total = sum(score_list)
print(f'平均点は{total/student_num}点です')

