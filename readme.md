
### kospi_top_100.py  
<ul>  
<li>./data/modify_data.xlsx 파일에 있는 종목을 읽어와 ./data/stock_list_with_name&num.xlsx 에 종목명과 종목코드를 쓴다.</li>  
</ul>  

---
### combine_data_in_one_file.py  
<ul>  
<li>./data/stock_list_with_name&num.xlsx 에 있는 정보를 읽어와  <br>"./data/combine_data.xlsx" 에 20170102부터 20190406까지 top100 종목의 종가를 <br>하나의 시트안에 저장한다.</li>  
<li>make_stock_data 는 ./data/stock_list_with_name&num.xlsx 에 있는 정보를 읽어와 <br>"./data/stock_data/ 에 "종목번호_종목명.xlsx" 로 저장한다.  
    <ul>  
    <li>*하나의 파일에 저장해야 해서 이 파일은 거의 쓰지 않음*  
    </li>  
    </ul>  
</li>  
</ul>

---
### rate_of_increase_decrease.py  
<ul>  
	<li>
	./data/modify_data.xlsx 파일에 있는 종목을 읽어와 ./data/combine_data_ratio.xlsx 에 날짜별 top100 개 기업에 대한 등락율을 기록한다<br>
	상위5개 하위 5개 기록...
	</li>  

</ul>  
  ---