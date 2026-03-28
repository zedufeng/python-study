fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    print(line.rstrip())
    word=line.split()
    if not word in lst:
        lst.append(word)
print(lst)