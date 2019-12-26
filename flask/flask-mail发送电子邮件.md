
# 采用Flask-Mail模块发送电子邮件

##python程序
命名为hello.py

```python
import os 
from flask import Flask
from flask_mail import Mail
from flask_script import Manager

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.126.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

manager = Manager(app)
mail = Mail(app)

if __name__ == "__main__":
    manager.run()
```

## 在cmd命令行中
```shell
ipython hello.py shell
```

```shell
# -----------------------------------------------
# MAIL_USERNAME和MAIL_PASSWORD写入windows环境变量中，一定要采用cmd命令行方式写入，不要用powershell
from flask_mail import Message
from hello import mail
msg = Message('test mail', sender='zhzhang09@126.com', recipients=['zhzhang09@126.com'])
msg.body = 'test body'
msg.html = '<b>test html</b>'
with app.app_context():
    mail.send(msg)
# Message参数说明：
# 第一个参数：邮件主题
# 第二个参数：发件人邮箱账号
# 第三个参数：收件人邮箱账号(可以写一个或多个)
# msg.body和msg.html是邮件正文

```shell


** 更多详情请参考链接：https://www.cnblogs.com/gandoufu/p/9497703.html

谢谢
