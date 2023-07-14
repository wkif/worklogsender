# /*
#  * @Author: kif kif101001000@163.com 
#  * @Date: 2023-07-14 18:53:19 
#  * @Last Modified by:   kif kif101001000@163.com  
#  * @Last Modified time: 2023-07-14 18:53:19 
#  */

from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import smtplib

from config import sender, password,to_addr


def sendFile(filePath,fileName):
    title=fileName.split('.')[0]
    # 创建一个带附件的实例
    message = MIMEMultipart() 
    message['From'] = sender #发件人
    message['To'] =Header(",".join(to_addr)) #处理多个收件人信息，list 转字符串
    message['Subject'] = Header(title, 'utf-8').encode() # 邮件标题
    msg='''

序号	日期	人员姓名	今日计划内任务						今日计划外任务		
			任务名称	安排人	计划工时	实际工时	状态	备注	任务名称	安排人	实际工时
1	2023/7/13	凯凡	营销管理系统需求开发	漆玉	5	5	完成		hotelv预订员管理迁移	漆玉	4

'''
    message.attach(MIMEText(msg,'plain','utf-8'))
    # MIMEApplication对附件进行封装
    xlsxpart = MIMEApplication(open(filePath, 'rb').read())
    xlsxpart.add_header('Content-Disposition', 'attachment', filename=fileName)
    message.attach(xlsxpart)
    # 发送邮件
    try:
        smtpObj = smtplib.SMTP_SSL("smtp.exmail.qq.com", port=465)
        # smtpObj=smtplib.SMTP_SSL() #SMTP的SSL加密方式，端口要用465
        # smtpObj.connect(smtp_server,465) #连接腾讯服务器地址，传入地址和端口参数；腾讯企业邮箱STMP端口号是465
        smtpObj.login(sender,password) # 登录邮箱，传入发件人邮箱及独立密码
        smtpObj.sendmail(sender,to_addr,message.as_string()) 
        print('success!')
        smtpObj.quit()
    
    except smtplib.SMTPException as e:
        print('error',e)
    
sendFile('./file/技术部工作日志-凯凡-2023-07-13.xlsx','技术部工作日志-凯凡-2023-07-13.xlsx')