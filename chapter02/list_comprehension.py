# -*- coding=utf-8 -*-
#
# Copyright @ 2018 HuiXin Zhao

"""compare with filter and map"""
symbols = '$¢£¥€¤'
beyond_ascii_lc = [ord(s) for s in symbols if ord(s) > 127]
beyond_ascii_fm = list(filter(lambda c: c > 127, map(ord, symbols)))
