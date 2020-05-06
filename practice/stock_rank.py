# https://financedata.github.io/marcap/
# https://woosa7.github.io/krx_stock_master/
import pandas as pd
import numpy as np
import requests
from io import BytesIO
from datetime import datetime


def stock_master_price(date=None):
    if date == None:
        date_=datetime(year=2016,month=1,day=4)
        date = date_.strftime('%Y%m%d')  # 오늘 날짜


    # STEP 01: Generate OTP
    gen_otp_url = 'http://marketdata.krx.co.kr/contents/COM/GenerateOTP.jspx'
    gen_otp_data = {
        'name': 'fileDown',
        'filetype': 'xls',
        'url': 'MKD/04/0404/04040200/mkd04040200_01',
        'market_gubun': 'ALL',  # 시장구분: ALL=전체
        'indx_ind_cd': '',
        'sect_tp_cd': '',
        'schdate': date,
        'pagePath': '/contents/MKD/04/0404/04040200/MKD04040200.jsp',
    }

    r = requests.post(gen_otp_url, gen_otp_data)
    code = r.content  # 리턴받은 값을 아래 요청의 입력으로 사용.

    # STEP 02: download
    down_url = 'http://file.krx.co.kr/download.jspx'
    down_data = {
        'code': code,
    }

    r = requests.post(down_url, down_data)
    print(r.content)
    input()
    df = pd.read_excel(BytesIO(r.content), header=0, thousands=',')

    return df


df = stock_master_price()
print(df)