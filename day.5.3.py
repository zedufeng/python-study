numbers=0
total_score=0
while True:
    name=input('输入学生姓名:')
    if name=='exit':
        break
    score = int(input('输入学生成绩:'))
for student in [name,score]:
        numbers=numbers+1
        total_score=total_score+score
        print(student)
print("总学生数:", numbers)
print('总分数：', total_score)