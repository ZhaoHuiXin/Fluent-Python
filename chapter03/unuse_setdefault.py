import sys
import re

WORD_RE = re.compile(r'\w+')

index = {}
with open(sys.argv[1], encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        print("line_no:", line_no, "line:", line)
        for match in WORD_RE.finditer(line):
            print("match:", match)
            word = match.group()
            print("match.group():", word)
            print("match.start():", match.start())
            column_no = match.start()+1
            location = (line_no, column_no)  # 每行开始首字母的坐标
            # 以word为键，得不到就返回一个空列表,得到了还是一个有单词坐标的列表
            occurrences = index.get(word, [])
            occurrences.append(location)
            # 把新的列表放回字典，又牵扯到一次查询操作
            index[word] = occurrences
        print("*" * 50)
# 以字母的顺序打印结果:
for word in sorted(index, key=str.upper):  # 将方法用作一等函数的示例
    print(word, index[word])


