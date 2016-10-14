#!/usr/bin/env python
# -*- coding: utf-8  -*-

import pandas as pd
import numpy as np

from xtx.storage import *

cs_merged = CsvStorage("sanzhang.csv")
ls_merged = cs_merged.read(encoding = "gbk")
df_merged = pd.DataFrame(ls_merged[1:], columns = ls_merged[0])

pay_tools = ["B2CN", "NETB", "EXPR", "CARD", "COLL"]
trade_types = ["P100", "P101", "P102", "P106", "P107", "P400", "X001"]

df_merged = df_merged[df_merged["支付工具"].isin(pay_tools)]
df_merged = df_merged[df_merged["交易类型"].isin(trade_types)]

df_merged["交易笔数_int"] = df_merged["交易笔数"].astype(np.int32)
df_merged["支付金额_float"] = df_merged["支付金额"].astype(np.float64)

print("merged: ", df_merged.shape)

df_merged.to_csv("filtered_zhengdan.csv", index = False)


