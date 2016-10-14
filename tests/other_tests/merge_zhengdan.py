#!/usr/bin/env python
# -*- coding: utf-8  -*-

import pandas as pd
import numpy as np

from xtx.storage import *

es_sanzhang_1 = ExcelStorage(r"三账数据/0831-0910/正单.xlsx", sheetIndex = 0)
es_sanzhang_2 = ExcelStorage(r"三账数据/0911-0920/正单.xlsx", sheetIndex = 0)
es_sanzhang_3 = ExcelStorage(r"三账数据/0921-0927/正单.xlsx", sheetIndex = 0)
es_sanzhang_4 = ExcelStorage(r"三账数据/0928-0929/正单.xlsx", sheetIndex = 0)
# es_sanzhang_5 = ExcelStorage(r"三账数据/0930/正单.xlsx", sheetIndex = 0)

# 1
ls_sanzhang_1 = es_sanzhang_1.read()
df_sanzhang_1 = pd.DataFrame(ls_sanzhang_1[1:], columns = ls_sanzhang_1[0])
del ls_sanzhang_1
print("0831-0910 shape: " , df_sanzhang_1.shape)



# 2
ls_sanzhang_2 = es_sanzhang_2.read()
df_sanzhang_2 = pd.DataFrame(ls_sanzhang_2[1:], columns = ls_sanzhang_2[0])
del ls_sanzhang_2
print("0911-0920 shape: " , df_sanzhang_2.shape)

df_sanzhang = df_sanzhang_1.append(df_sanzhang_2, ignore_index = True)
del df_sanzhang_1
del df_sanzhang_2



# 3
ls_sanzhang_3 = es_sanzhang_3.read()
df_sanzhang_3 = pd.DataFrame(ls_sanzhang_3[1:], columns = ls_sanzhang_3[0])
del ls_sanzhang_3
print("0921-0927 shape: ", df_sanzhang_3.shape)

df_sanzhang = df_sanzhang.append(df_sanzhang_3, ignore_index = True)
del df_sanzhang_3


# 4
ls_sanzhang_4 = es_sanzhang_4.read()
df_sanzhang_4 = pd.DataFrame(ls_sanzhang_4[1:], columns = ls_sanzhang_4[0])
del ls_sanzhang_4
print("0928-0929 shape: ", df_sanzhang_4.shape)

df_sanzhang = df_sanzhang.append(df_sanzhang_4, ignore_index = True)
del df_sanzhang_4


# 5
# ls_sanzhang_5 = es_sanzhang_5.read()
# df_sanzhang_5 = pd.DataFrame(ls_sanzhang_5[1:], columns = ls_sanzhang_5[0])
# del ls_sanzhang_5
# print("0930 shape: " , df_sanzhang_5.shape)

# df_sanzhang = df_sanzhang.append(df_sanzhang_5, ignore_index = True)
# del df_sanzhang_5


print(df_sanzhang)

df_sanzhang.to_csv("sanzhang.csv", index = False)
