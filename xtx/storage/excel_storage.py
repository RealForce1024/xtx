#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path
import pandas as pd

from xtx.storage.file_storage import FileStorage
from xtx.storage.exceptions import (StorageExistsError
    , StorageNotFoundError
    , UnmatchExtensionError)

class ExcelStorage(FileStorage):

    def __init__(self, filepath = None):
        super().__init__(filepath)
        
    def __read_excel2003(self, filepath, sheetIndex = None, \
		sheetName = None):
        import xlrd

        tabledata = []
        wb = xlrd.open_workbook(filepath)

		# get worksheet
        ws = None
        if not sheetName is None:
            ws = wb.sheet_by_name(sheetName)
        else:
            if not sheetIndex is None:
                ws = wb.sheet_by_index(sheetIndex)
            else:
                raise ValueError("The targetSheet arguments must be specified one:  sheetIndex=%s, sheetName=%s" % \
					(sheetIndex, sheetName))

		# get cell data
        for rowIndex in range(0, ws.nrows):
            row = ws.row(rowIndex)
            rowdata = []
            for colIndex in range(0, ws.ncols):
                cell = row[colIndex]
                cellval = cell.value
                rowdata.append(cellval)
            tabledata.append(rowdata)

        return tabledata

    def __read_excel2007(self, filepath, sheetIndex = None, \
		sheetName = None):
        from openpyxl.workbook import Workbook
        from openpyxl import load_workbook
        
        tabledata = []
        wb = load_workbook(filename = filepath)
        
		# get worksheet
        ws = None
        if not sheetName is None:
            ws = wb.get_sheet_by_name(sheetName)
        else:
            if not sheetIndex is None:
                ws = wb.get_sheet_by_name(wb.get_sheet_names()[sheetIndex])
            else:
                raise ValueError("The targetSheet arguments must be specified one:  sheetIndex=%s, sheetName=%s" % \
					(sheetIndex, sheetName))
        
		# get cell data
        for rowNum in range(1, ws.max_row + 1):
            rowdata = []
            for colNum in range(1, ws.max_column + 1):
                cellval = ws.cell(row = rowNum, column= colNum).value
                rowdata.append(cellval)
            tabledata.append(rowdata)
        
        return tabledata
        
    def write(self, data, overwrite = True):
        if not os.path.exists(self.filepath):
            raise StorageNotFoundError(self.filepath)
        raise NotImplementedError

    def read(self, line_limit = -1, sheetIndex = -1, sheetName = None):
        if not os.path.exists(self.filepath):
            raise StorageNotFoundError(self.filepath)
        
        data = None
        extName = self.filepath.split(".")[-1]
        if extName == "xls":
            data = self.__read_excel2003(filepath = self.filepath, sheetIndex = sheetIndex, \
            sheetName = sheetName)
        elif extName == "xlsx":
            data = self.__read_excel2007(filepath = self.filepath, sheetIndex = sheetIndex, \
            sheetName = sheetName)
        else:
            raise UnmatchExtensionError(self.filepath)
        return data
    