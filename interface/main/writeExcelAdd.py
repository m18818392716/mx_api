from xlutils import copy
import xlrd
import xlwt
excel_path='../dataconfig/writeExcel.xlsx'#文件路径
#excel_path=unicode('D:\\测试.xls','utf-8')#识别中文路径
rbook = xlrd.open_workbook(excel_path,formatting_info=True)#打开文件




wbook = copy.copy(rbook)#复制文件并保留格式
w_sheet = wbook.get_sheet(0)#索引sheet表


row=2
col=0
value=20180803


style = "font: color-index red,bold on"
red_style = xlwt.easyxf(style)

w_sheet.write(row,col,value,red_style)
wbook.save(excel_path)#保存文件