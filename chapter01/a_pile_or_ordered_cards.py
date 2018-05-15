# -*- coding: utf-8 -*-
# Copyright @ 2018 HuiXin Zhao

# 黑桃:S-Spade
# 红桃:H-Heart
# 方块:D-Diamond
# 梅花:C-Club

import collections
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """
        通过实现 __len__和 __getitem__ 这两个特殊方法,FrenchDeck 就跟一个 Python 自
    有的序列数据类型一样.同时这个类还可以用于标准库中诸如random.choice、reversed 和
    sorted 这些函数。另外,对合成的运用使得 __len__ 和 __getitem__ 的具体实现可以代理给
    self._cards这个 Python 列表(即 list 对象)。
        shuffle 函数要调换集合中元素的位置,而 FrenchDeck 只实现了不可变的序列协议。可变
    的序列还必须提供 __setitem__ 方法。
    """
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades clubs hearts diamonds'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    # 可变序列必须提供__setitem__方法
    def __setitem__(self, key, value):
        """
            random.shuffle 函数不关心参数的类型,只要那个对象实现了部分可变序列协议即可。
        即便对象一开始没有所需的方法也没关系,后来再提供也行。
        """
        self._cards[key] = value


# 对纸牌排序，按花色：黑红片花，序号2最小A最大
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


if __name__ == '__main__':
    from random import choice
    deck = FrenchDeck()
    print("deck响应len：", len(deck))
    for i in range(3):
        print("随机取3张：", choice(deck))
    print("只取最上面3张：", deck[:3])
    print("取所有的A：", deck[12::13])
    for card in deck:
        print("正向迭代deck：", card)
    for card in reversed(deck):
        print("反向迭代deck：", card)
    print("对纸牌排序：")
    for card in sorted(deck, key=spades_high):
        print(card)
