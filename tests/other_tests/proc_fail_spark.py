#!/usr/bin/env python
# -*- coding: utf-8  -*-

from pyspark.sql import SparkSession
from pyspark.sql.types import DoubleType, IntegerType
import numpy as np

from xtx.storage import *

spark = SparkSession \
    .builder \
    .appName("Process quiakpay fail data") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

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
df_interid2bank_data = spark.createDataFrame(interid2bank_data[1:], schema=["interface_id", "bank_name"])

es_bankerr2regerr = ExcelStorage("快捷失败映射数据.xlsx", sheetName = "银行错误2错误分类")
bankerr2regerr_data = es_bankerr2regerr.read()
df_bankerr2regerr = spark.createDataFrame(bankerr2regerr_data[1:], schema = ["bank_name", "bank_err", "bank_err_key", "err_category"])

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
		

df_fail_data = spark.createDataFrame(fail_data[1:], schema = columnNames)

df_fail_data = df_fail_data.withColumn("orders_amount_double", df_fail_data.orders_amount.astype(DoubleType()))
df_fail_data = df_fail_data.withColumn("orders_count_int", df_fail_data.orders_count.astype(IntegerType()))


df_tmp = df_fail_data.join(df_interid2bank_data, df_fail_data.interface_id == df_interid2bank_data.interface_id, how = "left")

rdd_tmp = df_tmp.rdd

rdd_tmp = rdd_tmp.map(lambda x: x + (x.bank_name + "$" + x.bank_error_msg,))

print(rdd_tmp.collect()[0])

# print(rdd_tmp)


# df_tmp = df_tmp.withColumn("bank_err_fkey", df_tmp.bank_name +  df_tmp.bank_error_msg)
# print(df_tmp.show())

# df_tmp = df_tmp.join(df_bankerr2regerr, df_tmp.bank_err_fkey == df_bankerr2regerr.bank_err_key, how = "left")

# g = df_tmp.groupby(["err_category"]).agg({"orders_count_int":"sum"}).collect()

# print(df_tmp.show())
#print(g)
#print(df_tmp.select("err_category").show())
# groupby_tmp = df_tmp.groupby(["bankname"])["orders_amount_float", "orders_count_float"].sum()
# print(groupby_tmp)

# print(groupby_tmp.sort_index(axis = 0, ascending = False))

# es = ExcelStorage("快捷失败数据_201609_mod.xlsx")
# es.create(force = True)
# es.write(fail_data = fail_data)