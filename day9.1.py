#作业名称；英文文本词频分析器（练习版）

def get_file_name():
    while True:
        filename=input("please enter file name")
        try:
            fil=open(filename)
        except:
            FileExistsError
            print("please enter corret filename again")
            continue
        fil.close()
        break
    return filename
filename=get_file_name()
word=open(filename)


def clean_word(word):
    for word in word.split():
        word=word.lower()
        word=word.strip("\".,!?;:'()[]{}")
    return word

def read_and_count(filename):
    counts={}
    line_count=0
    word_count=0
    fil=open(filename)
    for line in fil:
        line_count=line_count+1
        line.split()
        words=line.split()
        for word in words:
            word=clean_word(word)
            if word=='':
                continue
            word_count=word_count+1
            counts[word]=counts.get(word,0)+1
    return line_count,word_count,counts
counts=read_and_count(filename)[2]



def find_biggest(counts):
    bigcount=None
    bigword=None
    for word,count in counts.items():
        if bigcount is None or count>bigcount:
            bigword=word
            bigcount=count
    return bigword, bigcount

n=5
def get_top_words(counts,n):
    pairs=[]
    num=None
    for word, count in counts.items():
        pairs.append((count, word))
    pairs.sort(reverse=True)
    top_word=pairs[0][1]
    print(pairs[1])
    return pairs,top_word

line_count=read_and_count(filename)[0]
word_count=read_and_count(filename)[1]
counts=read_and_count(filename)[2]
bigword=find_biggest(counts)[0]
bigcount=find_biggest(counts)[1]
pairs=get_top_words(counts,n)[0]
top_word=get_top_words(counts,n)[1]



def print_report (line_count, word_count, counts, bigword, bigcount, top_words):
    print("===== TEXT REPORT =====")
    print('Total lines:',line_count)
    print('Total word:',word_count)
    print("Unique words: ",len(counts))
    print("Most frequent word:",bigword)
    print("Its count:",bigcount)
    rank = 1
for count, word in top_word[:5]:
    print(rank, word, count)
    rank += 1

    print("pass")

def main():
        if len(counts) == 0:
            print("There aren't word in file")
        print_report(line_count, word_count, counts, bigword, bigcount, top_word)
main()





