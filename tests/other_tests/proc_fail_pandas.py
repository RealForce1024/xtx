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

es_mercode2mertype = ExcelStorage("快捷失败映射数据.xlsx", sheetName = "商户号")
mercode2mertype_data = es_mercode2mertype.read()
df_mer = pd.DataFrame(mercode2mertype_data[1:], columns = ["create_date", "mer_code", "sub_account_no", "mer_level_2nd_code", "member_id", "owner", "biz_level_1", "biz_level_2", "mer_name", "to_biz", "fee", "contact", "remark"])

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

df_bankname_nan = df_tmp[pd.isnull(df_tmp["bank_name"])]
df_bankname_nan.groupby(["interface_id"])["orders_count"].sum().to_csv("bank_name_nan.csv")

df_tmp["bank_err_fkey"] = df_tmp["bank_name"] + "$" + df_tmp["bank_error_msg"]

df_tmp = pd.merge(df_tmp, df_bankerr2regerr, left_on = "bank_err_fkey", right_on = "bank_err_key", how="left")

df_errcat_nan = df_tmp[pd.isnull(df_tmp["err_category"])]

df_errcat_nan.groupby(["bank_name_x", "bank_error_msg", "err_category"])["orders_count"].sum().to_csv("err_cat_nan.csv")

df_tmp = pd.merge(df_tmp, df_mer, left_on = "merchant_code", right_on = "mer_level_2nd_code", how = "left")

df_tmp["owner"] = df_tmp["owner"].fillna("网银自营")
df_tmp["biz_level_1"] = df_tmp["biz_level_1"].fillna("网银自营")
df_tmp["biz_level_2"] = df_tmp["biz_level_2"].fillna("网银自营")

# df_tmp.drop([""])
# df_tmp.to_csv("final.csv")

df_final = df_tmp.loc[:,["create_date_x", "interface_id", "channel_id", 
	"cardtype", "bank_error_code", "bank_error_msg", "merchant_code", "bank_merchant_code", 
	"money_section", "orders_amount_double", "orders_count_int", "bank_name_x", 
	"err_category", "owner", "biz_level_1", "biz_level_2", "mer_name"]]
	
df_final.to_csv("final.csv")

#print(df_tmp)

# es = ExcelStorage("快捷失败数据_201609_mod.xlsx")
# es.create(force = True)
# es.write(df_tmp.values)