import openpyxl as op
 
wb = op.Workbook()
wb.save('./test.xlsx')
wb = op.load_workbook("./test.xlsx")
wb.create_sheet('sheet1')
 
for i in range(len):
    ws.cell(row=i,column=0).value = i
 
wb.close()
 
 
