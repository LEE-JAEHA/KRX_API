from pykrx import stock
import numpy as np
import openpyxl as op
import pandas as pd
import pickle


def tmp_stock_list():
    """
    stock list 가 잘못되어 수정전 임시 파일로 기업 리스트 읽어옴
    :return:
    """
    wb = op.Workbook()
    wb = op.load_workbook("../data/indicator/tmp_stock_list.xlsx")
    sheet1 = wb["Sheet"]
    for idx, val in enumerate(sheet1):
        if idx == 0:
            continue
        company_list.append([val[0].value, val[1].value])
        # (종목명,종목번호)
    wb.close()



tmp_stock_list()