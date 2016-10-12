#!/usr/bin/env python
# -*- coding: utf-8  -*-

import pandas as pd
import numpy as np

from xtx.storage import *


columnNames = [
    "create_date",
    "interface_id",
    "channel_id",
    "cardtype",
    "bank_error_code",
    "bank_error_msg",
    "uni_error_msg",
    "merchant_code",
    "bank_merchant_code",
    "money_section",
    "orders_amount",
    "orders_count"]

cs = CsvStorage("快捷失败数据_201609.csv")
fail_data = cs.read(encoding="GB2312")

es_interid2bank = ExcelStorage("快捷失败映射数据.xlsx", sheetName = "接口ID2银行")
interid2bank_data = es_interid2bank.read()
df_interid2bank_data = pd.DataFrame(interid2bank_data[1:], columns=["interface_id", "bank_name"]).dropna()

es_bankerr2regerr = ExcelStorage("快捷失败映射数据.xlsx", sheetName = "银行错误2错误分类")
bankerr2regerr_data = es_bankerr2regerr.read()
df_bankerr2regerr = pd.DataFrame(bankerr2regerr_data[1:], columns = ["bank_name", "bank_err", "bank_err_key", "err_category"]).dropna()

todel = []
for row in fail_data:
    if len(row) > len(columnNames):
        todel.append(row)

mod_rows = []
for row in todel:
	prefail_data = row[:5]
	postfail_data = row[-6:]
	centerfail_data = row[5:-6]
	mod_row = prefail_data + ["".join(centerfail_data)] + postfail_data
	fail_data.remove(row)
	fail_data.append(mod_row)
	

for row in fail_data:
    if len(row) != len(columnNames):
        print("ERR ROW:")
        print(row)
		

df_fail_data = pd.DataFrame(fail_data[1:], columns = columnNames)

df_fail_data["orders_amount_double"] = df_fail_data["orders_amount"].astype(np.float64)
df_fail_data["orders_count_int"] =  df_fail_data["orders_count"].astype(np.int32)


df_tmp = pd.merge(df_fail_data, df_interid2bank_data, on = "interface_id", how = "left")

df_tmp["bank_err_fkey"] = df_tmp["bank_name"] + "$" + df_tmp["bank_error_msg"]

df_tmp = pd.merge(df_tmp, df_bankerr2regerr, left_on = "bank_err_fkey", right_on = "bank_err_key", how="left")

df_tmp[pd.isnull(df_tmp["err_category"])].to_csv("err_cat_nan.csv")

#print(df_tmp)

# es = ExcelStorage("快捷失败数据_201609_mod.xlsx")
# es.create(force = True)
# es.write(fail_data = fail_data)