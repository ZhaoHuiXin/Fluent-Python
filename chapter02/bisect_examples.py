# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao

import bisect

# eg1:
def grade(score, breakpoints=(60, 70, 80, 90), grades='FDCBA'):
    i = bisect.bisect(breakpoints, score)
    return grades[i]


if __name__ == '__main__':
    res1 = [grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
    print(res1)

    # eg2:
    data = [('red', 5), ('blue', 1), ('yellow', 8), ('black', 0)]
    data.sort(key=lambda x: x[1])
    keys = [d[1] for d in data]
    for i in range(9):
        print(data[bisect.bisect_left(keys, i)])
