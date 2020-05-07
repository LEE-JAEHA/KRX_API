import openpyxl as op
 
wf = op.Workbook()
wb = wf.active
wb['A1'] = "종목코드";
wb['B1'] = "회사명"

for i in range(len):
    wb.cell(row=i,column=0).value = i

wb.cell(row="A",colum=0)



wb.save('./test.xlsx')
wb.close()
 
 
