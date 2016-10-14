#!/usr/bin/env python
# -*- coding: utf-8  -*-

import pandas as pd
import numpy as np

from xtx.storage import *

cs_zhengdan = CsvStorage("filtered_zhengdan.csv")
ls_zhengdan = cs_zhengdan.read(encoding = "gbk")
df_zhengdan = pd.DataFrame(ls_zhengdan[1:], columns = ls_zhengdan[0])






