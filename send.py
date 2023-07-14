# /*
#  * @Author: kif kif101001000@163.com 
#  * @Date: 2023-07-14 18:53:32 
#  * @Last Modified by:   kif kif101001000@163.com  
#  * @Last Modified time: 2023-07-14 18:53:32 
#  */
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import xlrd
from config import sender, password,to_addr,cc_mail


def mailWrite(path):

    #表格的标题和头
    header = '<html><head><meta http-equiv="Content-Type" content="text/html; charset=utf-8" /></head>'
    th = """
<body text="#000000" >
<table style="text-align: center;width:100%;border-collapse: collapse;border: 1px solid #999;">
	<tr style="height:10px;border: 1px solid #999;">
		<td rowspan="2" style=" padding: 20px 0;border: 1px solid #999;">序号</td>
		<td rowspan="2" style=" padding: 20px 0;border: 1px solid #999;">日期</td>
		<td rowspan="2" style=" padding: 20px 0;border: 1px solid #999;">人员姓名</td>
		<td colspan="6" style=" padding: 20px 0;border: 1px solid #999;background-color: #ddebf7">今日任务内安排</td>
		<td colspan="3" style=" padding: 20px 0;border: 1px solid #999; background-color: #ffe699">今日任务外安排</td>

	</tr>
	<tr style="border: 1px solid #999;">
		<td style=" padding: 20px 0;border: 1px solid #999;">任务名称</td>
		<td style=" padding: 20px 0;border: 1px solid #999;">安排人</td>
		<td style=" padding: 20px 0;border: 1px solid #999;">计划工时</td>
		<td style=" padding: 20px 0;border: 1px solid #999;">实际工时</td>
		<td style=" padding: 20px 0;border: 1px solid #999;">状态</td>
		<td style=" padding: 20px 0;border: 1px solid #999;">备注</td>
		<td style=" padding: 20px 0;border: 1px solid #999;">任务名称</td>
		<td style=" padding: 20px 0;border: 1px solid #999;">安排人</td>
		<td style=" padding: 20px 0;border: 1px solid #999;">实际工时</td>

	</tr>

"""
    filepath = path
    book = xlrd.open_workbook(filepath)
    sheet = book.sheet_by_index(0)
    nrows = sheet.nrows - 1
    ncols = sheet.ncols
    body = ''
    cellData = 1
    for i in range(2,nrows+1):
        trL='<tr style="border: 1px solid #999;">'
        trR='</tr>'
        for j in range(ncols):
            cellData = sheet.cell_value(i , j)
            # #读取单元格数据，赋给cellData变量供写入HTML表格中
            td = '	<td style=" padding: 10px 0;border: 1px solid #999;">' + str(cellData) + '</td>'
            trL = trL + td
        tr = trL + trR
        body = body + tr
    tail = '</table></body></html>'
    mailcontent = header+th+body+tail
    return mailcontent

def sendFile(path,fileName):
    print('sendFile',path)
    content = mailWrite(path)
    html = MIMEText(content,'html','utf-8')
    msg = MIMEMultipart()
    #邮件主题
    msg['Subject'] = Header(fileName,'utf-8').encode()
    #发件人
    msg['From'] = sender
    #收件人
    msg['To'] = ','.join(to_addr)
    msg['Cc'] = ','.join(cc_mail)   # 为mail 的message 定义了一个头部属性。抄送对象。
    msg.attach(html)

    #邮件附件
    part = MIMEApplication(open(path, 'rb').read())
    #filename=邮件附件中显示的文件的名称，可自定义
    part.add_header('Content-Disposition', 'attachment', filename=fileName)
    msg.attach(part)
    #发送邮件
    #创建连接和登陆，smtp服务器地址，端口，发件人账号和密码,
    con = smtplib.SMTP_SSL("smtp.exmail.qq.com",465)
    con.login(sender,password)
    #sendmail(发件人，收件人，内容)
    to = ','.join(to_addr)
    con.sendmail(sender,to,msg.as_string())
    con.quit()
    print('已经发送给',to_addr,'抄送给',cc_mail)
    return True




