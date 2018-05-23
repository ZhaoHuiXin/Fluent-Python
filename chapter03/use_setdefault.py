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
            location = (line_no, column_no)
            # 如果单词不存在,把单词和一个空列表
            # 放进映射,然后返回这个空列表,
            # 这样就能在不进行第二次查找的情况下更新列表了
            index.setdefault(word, []).append(location)
            '''
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(new_value)
            '''
        print("*" * 50)
# 以字母的顺序打印结果:
for word in sorted(index, key=str.upper):  # 将方法用作一等函数的示例
    print(word, index[word])


