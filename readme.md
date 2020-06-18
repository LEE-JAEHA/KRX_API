
## 데이터 마이닝을 통한 주가 상승 종목 예측

#### kospi_top_100.py 

<li>./data/modify_data.xlsx 파일에 있는 종목을 읽어와 ./data/stock_list_with_name&num.xlsx 에 종목명과 종목코드를 쓴다.</li>    

#### combine_data_in_one_file.py   
<li>./data/stock_list_with_name&num.xlsx 에 있는 정보를 읽어와 "./data/combine_data.xlsx" 에 20170102부터 20190406까지 top100 종목의 종가를 하나의 시트안에 저장한다.</li>    
<li>make_stock_data 는 ./data/stock_list_with_name&num.xlsx 에 있는 정보를 읽어와 "./data/stock_data/ 에 "종목번호_종목명.xlsx" 로 저장한다. </li>   

> 하나의 파일에 저장해야 해서 이 파일은 거의 쓰지 않음
  
 
### rate_of_increase_decrease.py <ul>
<ul>     
   <li>  
   ./data/modify_data.xlsx 파일에 있는 종목을 읽어와 ./data/combine_data_ratio.xlsx 에 날짜별 top100 개 기업에 대한 등락율을 기록한다   

> 상위5개 하위 5개 기록...  
   </li>
</ul>    
  

### combine_data_in_one_row=date.py
<ul>    
<li>"./data/combine_data.xlsx" 에 있는 정보를 읽어와 "./data/combine_data_ratio.xlsx" 에 각 날짜별 등락율을 기록하며 "./data/combine_data_ratio_row=date.xlsx" 에 날짜별 TOP5를 적는다. </li>       
</ul> 


### combine_indicator_date.py  
<ul>    
<li>"./data/indicator/stock_data_indicator_0603.xlsx" 에 있는 정보를 읽어와 "./data/indicator/indicator_dict" 에 indicator: indicator[날짜][기업명] 에 대한 보조 지표 데이터를 가지고 있는 딕셔너리 파일을 저장한다.</li>      
</ul>  
