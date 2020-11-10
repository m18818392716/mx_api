import xlrd
import xlwt
from xlutils.copy import copy

filename = ('../dataconfig/writeExcel.xlsx')
#excel_path=unicode('D:\\测试.xls','utf-8')#识别中文路径


# 创建文件名
# 创建Excel工作簿对象
# 创建工作表
# 创建样式字体红色

workbook = xlrd.open_workbook(filename,formatting_info=True)
# wbook = copy.copy(wb)
# sheet = wbook.get_sheet(0)
sheet = workbook.sheet_by_index(0)

wbook_update = copy(workbook)
sheet_update = wbook_update.get_sheet(0)


# style = "font:colour_index red;"
style = "font: color-index red,bold on"
styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour ocean_blue; font: bold on;')
red_style = xlwt.easyxf(style)

# 准备要写入的数据
datas = [
          ['name','code', 'cost', 'goods_category_id',
          'weight', 'net_weight', 'brand_id',
          'out_id', 'image_url', 'customs_code',
          'hs_code', 'customs_price', 'active',
          'is_group','cn_name','goods_name','goods_price'],
           [u'商品名称',u'商品编码', u'成本', u'商品类别',
            u'重量', u'净重', u'品牌', u'外部链接',
            u'图片URL', u'海关编码', u'hs编码',
            u'海关报价', u'商品状态(0/f)', u'是否组合商品(t/f)',
            u'申报中文名',u'商品名称',u'销售单价']
        ]

# 表头数据写入
row_count = len(datas)
for row in range(0, row_count):
    col_count = len(datas[row])
    for col in range(0, col_count):
        if row == 0:          # 设置表头单元格的格式
            sheet_update.write(row, col, datas[row][col])
        else:                 # 表头下面的数据格式
            sheet_update.write(row, col, datas[row][col],styleBlueBkg)

# sheet_update.write(2,red_style)

wbook_update.save(filename)





# # 合并单元格
# note = u'红色字体部分为说明部分，请删除。产品批量更新字段必须要name(就是sku)，其他需要更新的信息，自行复制下列字段添加到第一行(t为是，f为否)'
# sheet_update.write_merge(2, 2, 0, len(datas[1]), note)
