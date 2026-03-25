def menu():
    print('欢迎使用句子查找系统')
    print('请选择功能：','请输入功能对应数字编号')
    print('1.查看文件全部内容')
    print('2.查看包含关键词的句子')
    print('3.查看以指定词语开头的句子')
    print('4.同时查找两种句子')
    print('0.退出系统')
def open_file():
    filename=input('请输入要查找的文件名')
    try:
        file=open(filename,'r')
        return file
    except FileNotFoundError:
        print('文件未找到，请检查文件名是否正确')
        return None
def whole_file():
    file=open_file()
    if file:
        print('文件内容如下：')
        for line in file:
            print(line)
            file.close()
def main_word_check(line, main_word):
    return main_word in line
def start_word_check(line,start_word):
    return line.startswith(start_word)
def main_word():
    count_mainword=0
    main_word=input('请输入要查找的关键词')
    file=open_file()
    if file:    
        for line in file:
            if main_word_check(line, main_word):
                line=line.strip()
                print('含有关键词的句子：',line)
                count_mainword=count_mainword+1
                file.close()
    print('含有关键词的句子数量：', count_mainword)
def start_word():
    count_startword=0
    start_word=input('请输入要查找的起始词语')
    file=open_file()
    if file:
        for line in file:
            if start_word_check(line, start_word):
                line=line.strip()
                print('以指定词语开头的句子：',line)
                count_startword=count_startword+1
                file.close()
    print('以指定词语开头的句子数量：',count_startword)
def or_word():
    count_bothword=0
    main_word=input('请输入要查找的关键词')
    start_word=input('请输入要查找的起始词语')
    file=open_file()
    if file:
        for line in file:
            if main_word_check(line, main_word) or start_word_check(line, start_word):
                line=line.strip()
                print('满足两种条件其中一种的句子：',line)
                count_bothword=count_bothword+1
                file.close()
    print('满足两种条件其中一种的句子数量：',count_bothword)
while True:
    menu()
    choice=input('请输入功能对应数字编号')
    try:        
        choice=int(choice)
    except:     
        print('输入无效，请输入数字编号')
        continue
    if choice==1:
        whole_file()
    elif choice==2:
        main_word()
    elif choice==3:
        start_word()
    elif choice==4:
        or_word()
    elif choice==0:
        print('感谢使用句子查找系统，再见！')
        break