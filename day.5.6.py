numbers=0
total_score=0
smallest_score=None
largest_score=None
while True:
    Name=input('请输入学生姓名')
    if Name=='done':
        break
    score=input('请输入学生成绩')
    try:
        score=int(score)
    except:
        print('Invalid input')
        continue
    if(smallest_score is None or score<smallest_score):
        smallest_score=score
    if(largest_score is None or score>largest_score):
        largest_score=score
    numbers=numbers+1
    total_score=total_score+score
print("平均分",total_score/numbers)
print("总学生数:", numbers)
print("总分:", total_score)
print("最低分:", smallest_score)
print("最高分:", largest_score)
