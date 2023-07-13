#!/usr/bin/env python
#-*- coding: utf-8 -*-

# /*
#  * @Author: kif kif101001000@163.com 
#  * @Date: 2023-07-13 16:52:04 
#  * @Last Modified by:   kif kif101001000@163.com  
#  * @Last Modified time: 2023-07-13 16:52:04 
#  */
import os
from openpyxl import Workbook
from openpyxl import load_workbook
import xlrd
import xlwt
from fileEdit import init_excel_sheet1,init_excel_sheet2,saveFile,saveFlanFile
from sender import sendFile
from config import name
import datetime
import emoji

def addTaskLog(taskLogList):
    print('please input the following information about Todays planned tasks: ')
    task={}
    task['date'] = input('please input date: ')
    task['name'] = input('please input name: ')
    task['taskName'] = input('please input task name: ')
    task['arranger'] = input('please input arranger: ')
    task['planTime'] = input('please input plan time: ')
    task['actualTime'] = input('please input actual time: ')
    task['status'] = input('please input status: ')
    task['remark'] = input('please input remark: ')
    antherTask = input('do you have another task? y/n: ')
    if antherTask == 'y':
        print('please input the following information about Todays unplanned tasks: ')
        task['anthertaskName'] = input('please input task name: ')
        task['antherarranger'] = input('please input arranger: ')
        task['antherplanTime'] = input('please input plan time: ')
        task['antheractualTime'] = input('please input actual time: ')
    else:
        print('no more task')
        task['anthertaskName']=''
        task['antherarranger']=''
        task['antherplanTime']=''
        task['antheractualTime']=''
    taskLogList.append(task)

def addTaskFlan(taskPlanList):
    print('please input the following information about Todays planned tasks: ')
    task={}
    task['date'] = input('please input date: ')
    task['name'] = input('please input name: ')
    task['taskName'] = input('please input task name: ')
    task['arranger'] = input('please input arranger: ')
    task['planTime'] = input('please input plan time: ')
    task['remark'] = input('please input remark: ')
    taskPlanList.append(task)
def main():
    Workbook = xlwt.Workbook()   #创建工作簿
    sheet1 = Workbook.add_sheet(u'执行记录',cell_overwrite_ok=True)  #创建sheet
    sheet2 = Workbook.add_sheet(u'计划',cell_overwrite_ok=True)  #创建sheet
    init1 = init_excel_sheet1(sheet1)
    init2 = init_excel_sheet2(sheet2)
    taskLogList=[]
    taskPlanList=[]
    if init1 and init2:
        print(emoji.emojize('init success :saluting_face:'))
        # 输入a 表示增加一条记录，输入l表示查询所有记录
        # 输入q表示退出
        while True:
            print('|-----------------------------------------------|')
            print('|-------------kifs work log sender--------------|')
            print('|-----------------------------------------------|')
            print('|------------a: add a record--------------------|')
            print('|------------l: list all records----------------|')
            print('|------------q: quit----------------------------|')
            print('|-----------------------------------------------|')
            print('|----------------code by kif--------------------|')
            cmd = input('please input your command: ')
            if cmd == 'a':
                # 执行记录还是计划
                flag = input('Add execution records or plans? 1/2: ')
                if flag == '1':
                  addTaskLog(taskLogList)
                elif flag == '2':
                   addTaskFlan(taskPlanList)
            elif cmd == 'l':
                print('----------taskLogList-----------:')
                for task in taskLogList:
                    print('date: '+task['date']+ ' name: '+task['name']+' taskName: '+task['taskName']+' arranger: '+task['arranger']+' planTime: '+task['planTime']+' actualTime: '+task['actualTime']+' status: '+task['status']+' remark: '+task['remark']+' anthertaskName: '+task['anthertaskName']+' antherarranger: '+task['antherarranger']+' antherplanTime: '+task['antherplanTime']+' antheractualTime: '+task['antheractualTime']+'\n')
                print('----------taskPlanList-----------:')
                for task in taskPlanList:
                    print('date: '+task['date']+ ' name: '+task['name']+' taskName: '+task['taskName']+' arranger: '+task['arranger']+' planTime: '+task['planTime']+' remark: '+task['remark'])
            elif cmd == 'q':
                print('quit')
                print('save file')
                saveFile(taskLogList,sheet1)
                saveFlanFile(taskPlanList,sheet2)
                print('please input file name: ')
                fileName = input()
                # 判断是否输入了文件后缀
                if fileName == '':
                    fileName = '技术部工作日志-'+name+'-'+ datetime.datetime.now().strftime("%Y-%m-%d") +'.xlsx'
                if fileName.find('.') == -1:
                    fileName = fileName+'.xlsx'
                path = os.path.join('./file',fileName)
                Workbook.save(path) #保存文件
                print('save file success')
                # 是否发送
                send = input('send file? y/n: ')
                if send == 'y':
                    print('send file-------')
                    sendFile(path,fileName)
                else:
                    print('no send file')
                break
            else:
                print('invalid command')
    else:
        print('init failed')

if __name__ == '__main__':
    main()
    