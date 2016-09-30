#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import pandas as pd

class ExcelStorage(Storage):

    def __init__(self, filepath = None):
        super().__init__()

    def create(self, force = False):
        pass
