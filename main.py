#!/usr/bin/env python
#-*- coding: utf-8 -*-

# /*
#  * @Author: kif kif101001000@163.com 
#  * @Date: 2023-07-13 16:52:04 
#  * @Last Modified by:   kif kif101001000@163.com  
#  * @Last Modified time: 2023-07-13 16:52:04 
#  */
import os
from openpyxl import load_workbook
import xlwt
from fileEdit import init_excel_sheet1,init_excel_sheet2,saveFile,saveFlanFile
from send import sendFile
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
        print(emoji.emojize(':heart_on_fire: init success  :heart_on_fire: \n'))
        # 输入a 表示增加一条记录，输入l表示查询所有记录
        # 输入q表示退出
        while True:
            print('\n\n')
            print('|-----------------------------------------------|')
            print('|-------------KIFS WORK LOG SENDER--------------|')
            print('|-----------------------------------------------|')
            print(emoji.emojize('|------------a: :backhand_index_pointing_right: add a record-----------------|'))
            print(emoji.emojize('|------------l: :backhand_index_pointing_right: list all records-------------|'))
            print(emoji.emojize('|------------s: :backhand_index_pointing_right: send  email     -------------|'))
            print(emoji.emojize('|------------q: :backhand_index_pointing_right: quit-------------------------|'))
            print('|-----------------------------------------------|')
            print('|----------------EDIT BY KIF--------------------|')
            print('\n\n')

            cmd = input('please input your command: \n')
            if cmd == 'a':
                # 执行记录还是计划
                flag = input('Add execution records or plans? 1/2: \n')
                if flag == '1':
                  addTaskLog(taskLogList)
                elif flag == '2':
                   addTaskFlan(taskPlanList)
            elif cmd == 'l':
                print(emoji.emojize(':sparkles::sparkles::sparkles::sparkles:taskLogList start:sparkles::sparkles::sparkles::sparkles::'))
                for task in taskLogList:
                    print('date: '+task['date']+ ' name: '+task['name']+' taskName: '+task['taskName']+' arranger: '+task['arranger']+' planTime: '+task['planTime']+' actualTime: '+task['actualTime']+' status: '+task['status']+' remark: '+task['remark']+' anthertaskName: '+task['anthertaskName']+' antherarranger: '+task['antherarranger']+' antherplanTime: '+task['antherplanTime']+' antheractualTime: '+task['antheractualTime']+'\n')
                
                print(emoji.emojize(':sparkles::sparkles::sparkles::sparkles:taskLogList end:sparkles::sparkles::sparkles::sparkles::'))
                print('\n\n\n')
                print(emoji.emojize(':sparkles::sparkles::sparkles::sparkles:taskPlanList start:sparkles::sparkles::sparkles::sparkles::'))
                for task in taskPlanList:
                    print('date: '+task['date']+ ' name: '+task['name']+' taskName: '+task['taskName']+' arranger: '+task['arranger']+' planTime: '+task['planTime']+' remark: '+task['remark'])
                print(emoji.emojize(':sparkles::sparkles::sparkles::sparkles:taskPlanList end:sparkles::sparkles::sparkles::sparkles::'))
            elif cmd == 'q':
                print(emoji.emojize('quit :thermometer:'))
                print(emoji.emojize('save file :artist_palette:'))
                saveFile(taskLogList,sheet1)
                saveFlanFile(taskPlanList,sheet2)
                print(emoji.emojize('please input file name: :teddy_bear:\n'))
                fileName = input()
                # 判断是否输入了文件后缀
                if fileName == '':
                    fileName = '技术部工作日志-'+name+'-'+ datetime.datetime.now().strftime("%Y-%m-%d") +'.xlsx'
                if fileName.find('.') == -1:
                    fileName = fileName+'.xlsx'
                path = os.path.join('./file',fileName)
                Workbook.save(path) #保存文件
                print(emoji.emojize('save file success :womans_clothes:'))
                # 是否发送
                send = input('send file? y/n: ')
                if send == 'y':
                    print(emoji.emojize('send file-------:yellow_circle: :orange_circle: :red_circle: :blue_circle:'))
                    flag = sendFile(path,fileName)
                    if flag:
                        print(emoji.emojize('send file success :womans_clothes:'))
                    else:
                        print(emoji.emojize('send file failed :japanese_symbol_for_beginner:'))
                else:
                    print(emoji.emojize('no send file :japanese_symbol_for_beginner:'))
                break
            elif cmd == 's':
                # 获取file目录下的文件列表
                print(emoji.emojize('file list: :teddy_bear: \n'))
                files = os.listdir('./file')
                for file in files:
                    print(emoji.emojize(':teddy_bear:'),file)
                print(emoji.emojize('\nplease select file: :teddy_bear:'))
                fileName = input()
                # 判断是否输入了文件后缀
                if fileName == '':
                    print(emoji.emojize('file name error: :teddy_bear:'))
                    continue
                if fileName.find('.') == -1:
                    fileName = fileName+'.xlsx'
                path = os.path.join('./file',fileName)
                if not os.path.exists(path):
                    print(emoji.emojize('file not exists: :teddy_bear:'))
                    continue
                send = input('send file? y/n: ')
                if send == 'y':
                    print(emoji.emojize('send file-------:yellow_circle: :orange_circle: :red_circle: :blue_circle:'))
                    flag = sendFile(path,fileName)
                    if flag:
                        print(emoji.emojize('send file success :triangular_flag:'))
                    else:
                        print(emoji.emojize('send file failed :cross_mark:'))
                else:
                    print(emoji.emojize('no send file :cross_mark:'))
                break
            else:
                print('invalid command')
    else:
        print('init failed')

if __name__ == '__main__':
    main()
    