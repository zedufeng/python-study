"""
作业名称：英文文本词频分析器（练习版）

说明：
1. 这个文件只给“要求”和“代码框架”，不提供完整答案。
2. 你需要自己补全函数内容。
3. 重点练习：
   - 文件读取
   - 字符串清洗
   - 字典计数
   - for word, count in counts.items()
   - 找最大值
   - 元组列表排序
4. 建议配合 sample_text_v2.txt 一起测试。
5. 参考输出见 expected_output_v2.txt

完成目标：
- 统计总行数
- 统计总单词数
- 统计不重复单词数
- 找出出现次数最多的单词
- 输出出现次数前 5 的单词
"""

def get_file_name():
    """
    要求：
    1. 提示用户输入文件名
    2. 如果文件可以正常打开，就返回文件名
    3. 如果文件打不开，就提示并重新输入
    4. 建议使用 while True + try/except
    """
    pass


def clean_word(word):
    """
    要求：
    1. 把单词转成小写
    2. 去掉单词前后常见标点符号
    例如：.,!?;:"'()[]{}
    3. 返回清洗后的结果

    示例：
    "Hello," -> "hello"
    "Python!" -> "python"
    """
    pass


def read_and_count(filename):
    """
    要求：
    1. 打开文件并逐行读取
    2. 统计总行数 line_count
    3. 统计总单词数 word_count
    4. 用字典 counts 统计每个单词出现次数
    5. 每个单词都要先调用 clean_word()
    6. 空字符串不要统计
    7. 返回：
    counts, line_count, word_count

    提示：
    - line.split()
    - counts.get(word, 0) + 1
    """
    pass


def find_biggest(counts):
    """
    要求：
    1. 使用下面这种“找最大值模式”：

       bigcount = None
       bigword = None

       for word, count in counts.items():
           if bigcount is None or count > bigcount:
               bigword = word
               bigcount = count

    2. 返回：
       bigword, bigcount

    说明：
    - 这里只比较 count
    - 但更新时要同时更新 bigword 和 bigcount
    """
    pass


def get_top_words(counts, n):
    """
    要求：
    1. 创建一个空列表 pairs
    2. 遍历 counts.items()
    3. 把每组数据变成元组 (count, word)，加入 pairs
    4. 对 pairs 进行从大到小排序
    5. 取前 n 个
    6. 最终返回格式要求为：
       [(word1, count1), (word2, count2), ...]

    提示：
    - 为什么这里存成 (count, word)？
      因为这样排序时会优先按 count 排
    """
    pass


def print_report(line_count, word_count, counts, bigword, bigcount, top_words):
    """
    要求：
    按下面格式打印结果（内容值根据你的程序运行结果变化）：

    ===== TEXT REPORT =====
    Total lines: 4
    Total words: 20
    Unique words: 10
        pirnt("")
 hello
    Its count: 4

    ===== TOP 5 WORDS =====
    1 hello 4
    2 world 3
    3 python 3
    4 code 2
    5 again 2
    """
    pass


def main():
    """
    要求：
    1. 调用 get_file_name()
    2. 调用 read_and_count(filename)
    3. 如果 counts 为空，提示文件无有效单词，并结束
    4. 调用 find_biggest(counts)
    5. 调用 get_top_words(counts, 5)
    6. 调用 print_report(...)
    """
    pass


# 程序入口
main()
