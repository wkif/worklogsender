import os
from openpyxl import Workbook
from openpyxl import load_workbook
import xlrd
import xlwt



def set_style(name,height,bold=False):
	'''
	设置单元格样式
	'''
	style = xlwt.XFStyle()    # 初始化样式
	font = xlwt.Font()        # 为样式创建字体
	font.name = name          # '宋体'
	font.color_index = 4
	font.height = height
	alignment = xlwt.Alignment()
	alignment.horz = 0x02
	alignment.vert = 0x01
	style.alignment = alignment

	# borders= xlwt.Borders()
	# borders.left= 6
	# borders.right= 6
	# borders.top= 6
	# borders.bottom= 6

	style.font = font
	# style.borders = borders

	return style


def getStyle(flag):
	my_style = xlwt.XFStyle()
	font = xlwt.Font()
	font.name = '宋体'
	my_style.font = font
	alignment = xlwt.Alignment()
	alignment.horz = 0x02
	alignment.vert = 0x01
	my_style.alignment = alignment
	if flag==1:
		pattern = xlwt.Pattern()
		pattern.pattern = xlwt.Pattern.SOLID_PATTERN
		pattern.pattern_fore_colour = 41
		my_style.pattern = pattern
	if flag==2:
		pattern = xlwt.Pattern()
		pattern.pattern = xlwt.Pattern.SOLID_PATTERN
		pattern.pattern_fore_colour = 47
		my_style.pattern = pattern
	return my_style
	
def init_excel_sheet1(sheet1):
	sheet1.write_merge(0,1,0,0,'序号',getStyle(0))
	sheet1.write_merge(0,1,1,1,'日期',getStyle(0))
	sheet1.write_merge(0,1,2,2,'人员姓名',getStyle(0))
	sheet1.write_merge(0,0,3,8,'今日计划内任务',getStyle(1))
	sheet1.write_merge(0,0,9,11,'今日计划外任务',getStyle(2))
	sheet1.write_merge(1,1,3,3,'任务名称',getStyle(0))
	sheet1.write_merge(1,1,4,4,'安排人',getStyle(0))
	sheet1.write_merge(1,1,5,5,'计划工时',getStyle(0))
	sheet1.write_merge(1,1,6,6,'实际工时',getStyle(0))
	sheet1.write_merge(1,1,7,7,'状态',getStyle(0))
	sheet1.write_merge(1,1,8,8,'备注',getStyle(0))
	sheet1.write_merge(1,1,9,9,'任务名称',getStyle(0))
	sheet1.write_merge(1,1,10,10,'安排人',getStyle(0))
	sheet1.write_merge(1,1,11,11,'实际工时',getStyle(0))
	return True

def init_excel_sheet2(sheet2):
	sheet2.write_merge(0,1,0,0,'序号',getStyle(0))
	sheet2.write_merge(0,1,1,1,'日期',getStyle(0))
	sheet2.write_merge(0,1,2,2,'人员姓名',getStyle(0))
	sheet2.write_merge(0,0,3,6,'计划任务',getStyle(1))
	sheet2.write_merge(1,1,3,3,'任务名称',getStyle(0))
	sheet2.write_merge(1,1,4,4,'安排人',getStyle(0))
	sheet2.write_merge(1,1,5,5,'计划工时',getStyle(0))
	sheet2.write_merge(1,1,6,6,'备注',getStyle(0))
	return True

def saveFile(taskList,sheet1):
	row=2
	for task in taskList:
		sheet1.write(row,0,row-1,set_style('宋体',220,True))
		sheet1.write(row,1,task['date'],set_style('宋体',220,True))
		sheet1.write(row,2,task['name'],set_style('宋体',220,True))
		sheet1.write(row,3,task['taskName'],set_style('宋体',220,True))
		sheet1.write(row,4,task['arranger'],set_style('宋体',220,True))
		sheet1.write(row,5,task['planTime'],set_style('宋体',220,True))
		sheet1.write(row,6,task['actualTime'],set_style('宋体',220,True))
		sheet1.write(row,7,task['status'],set_style('宋体',220,True))
		sheet1.write(row,8,task['remark'],set_style('宋体',220,True))
		sheet1.write(row,9,task['anthertaskName'],set_style('宋体',220,True))
		sheet1.write(row,10,task['antherarranger'],set_style('宋体',220,True))
		sheet1.write(row,11,task['antheractualTime'],set_style('宋体',220,True))
		row=row+1
		
def saveFlanFile(taskPlanList,sheet2):
	row=2
	for task in taskPlanList:
		sheet2.write(row,0,row-1,set_style('宋体',220,True))
		sheet2.write(row,1,task['date'],set_style('宋体',220,True))
		sheet2.write(row,2,task['name'],set_style('宋体',220,True))
		sheet2.write(row,3,task['taskName'],set_style('宋体',220,True))
		sheet2.write(row,4,task['arranger'],set_style('宋体',220,True))
		sheet2.write(row,5,task['planTime'],set_style('宋体',220,True))
		sheet2.write(row,6,task['remark'],set_style('宋体',220,True))
		row=row+1
	