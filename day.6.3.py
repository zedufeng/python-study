count_mainword=0
count_startword=0
f=open('word.txt','r')
main_word=input('请输入要查找的关键词')
start_word=input('请输入要查找的起始词')
def search_word(main_word,start_word):
    for line in f:
        line=line.strip()
        if main_word in line:
            count_mainword=count_mainword+1
        if line.startswith(start_word):
            count_startword=count_startword+1
        if line.startswith(start_word) or main_word in line:
            print(line)
print('含有关键词的句子数量：', count_mainword)
print('以指定词语开头的句子数量：',count_startword)
f.close()