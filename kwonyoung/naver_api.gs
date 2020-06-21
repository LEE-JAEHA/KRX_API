function myFunction() {
  
  var start_row = 2;
  var start_column = 4;
  var num_row = 100;
  var num_col = 2;
  
  var col_checker = 0;
  
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = ss.getSheets()[0];
  var range = sheet.getRange(start_row, 1, num_row, num_col);
  var values = range.getValues();
  
  var client_id = 'xxxxxxxxxxxxxxxxxxxx';
  var client_secret = 'xxxxxxxxxxxxxx';
  
  var headers = {
    'X-Naver-Client-Id': client_id,
    'X-Naver-Client-Secret': client_secret,
    'Content-Type': 'application/json'
  }
  
  var search = [];
  
  for (var x in values) {
    
    var name = values[x][0]
  
    var request_body = {
      "startDate": "2017-01-01",
      "endDate": "2020-04-20",
      "timeUnit": "date",
      "keywordGroups": [
        {
          "groupName": name,
          "keywords": [
            name
          ]
        }
      ]
    };
    
    var options = {
      'method' : 'post',
      'payload' : JSON.stringify(request_body),
      'headers' : headers
    };
    
    var response = UrlFetchApp.fetch("https://openapi.naver.com/v1/datalab/search", options);
    Logger.log(response);
    response = JSON.parse(response);
    Logger.log(response);
    
    results = response["results"][0]  
    
    Logger.log("results is " + results);
    
    var title = results["title"]
    var data = results["data"]
    
    Logger.log(title)
    Logger.log(data)
    
    var cnt = 0;
    var period = [];
    var search_tmp = [];
    search_tmp.push(name);
    
    for (var y in data) {
      search_tmp.push(data[y]["ratio"]);
      period.push(data[y]["period"]);
    }
    
    Logger.log("search_tmp.length is " + search_tmp.length)
    Logger.log("x is " + x);
    Logger.log("start_row + x is " + (Number(x) + Number(start_row)));
    
    Logger.log("col_checker is " + col_checker);
    var search_tmp_length = search_tmp.length;
    
    if (x == 0) {
      col_checker = search_tmp_length;
      sheet.getRange(Number(x) + Number(start_row), start_column, 1, search_tmp_length).setValues([search_tmp]);
      sheet.getRange(1, Number(start_column) + 1, 1, period.length).setValues([period]);
    
    } else if(col_checker == search_tmp_length) {
      sheet.getRange(Number(x) + Number(start_row), start_column, 1, search_tmp_length).setValues([search_tmp]);
      
    } else if (col_checker > search_tmp_length) {
      sheet.getRange(Number(x) + Number(start_row), start_column, 1, 2).setValues([[name, "invalid"]]);
    
    } else if (col_checker < search_tmp_length) {
      sheet.getRange(Number(x) + Number(start_row) - 1, start_column, 1, 2).setValues([[name, "invalid so far"]]);
      col_checker = search_tmp_length;
      sheet.getRange(1, Number(start_column) + 1, 1, period.length).setValues([period]);
      
    }
    
    
    
    search.push(search_tmp);
  
  }
  
  Logger.log("search_tmp.length is " + search_tmp.length)
  Logger.log("search.length is " + search.length)
  Logger.log("search[0].length is " + search[0].length)
  Logger.log("search[0] is " + search[0])
  Logger.log("search_tmp is " + search_tmp)


  
}
