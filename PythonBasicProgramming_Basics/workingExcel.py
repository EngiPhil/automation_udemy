import xlrd
import xlwt

# We need to create object of workbook

wk = xlrd.open_workbook("/InputFiles\\dataXLS.xls")

print(wk.nsheets)

# Sheet level
ws = wk.sheet_by_index(0)
print(ws.nrows)
print(ws.ncols)

wkx = xlwt.Workbook()
# Adding sheet to the excel
wsx = wkx.add_sheet('Testing')
wsx.write(0, 0, 'Testing Filip')
wsx.write(0, 1, 'Another value')

wkx.save("C:\\Users\\FilipV\\Filip\\PyCharm\\Automation1\\OutputFiles\\dataXLSCreated.xls")
