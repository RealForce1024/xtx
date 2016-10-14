#!/usr/bin/env python
# -*- coding: utf-8  -*-

import pandas as pd
import numpy as np

from xtx.storage import *

s_cb = ExcelStorage(r"2016-09/20160930.xls", sheetIndex = 0)
ls_cb = s_cb.read()
df_cb = pd.DataFrame(ls_cb[1:], columns = ["date", "src_type", "bank", "cardtype", "users_count", "cards_count"])

s_bankMappings = ExcelStorage("映射数据.xlsx", sheetName = "银行名称映射")
ls_bankMappings = s_bankMappings.read()
df_bankMappings = pd.DataFrame(ls_bankMappings[1:], columns = ["alias", "uni_name"])
print("Bank Mapping: ", df_bankMappings.shape)
df_bms = df_bankMappings.drop_duplicates(subset=["alias"], keep="first")
print("Bank Mapping Droped Duplicates: ", df_bms.shape)


df_tmp = pd.merge(df_cb, df_bms, left_on = "bank", right_on = "alias", how="left")
df_uniname_nan = df_tmp.loc[pd.isnull(df_tmp["uni_name"]), ["bank"]]
df_uniname_nan.to_csv("uniname_nan.csv")

df_tmp.to_csv("final.csv")

