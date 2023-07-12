import paramiko
import re

'''
远程登录linux服务器并执行命令，可用于一键自动化部署项目
'''

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='127.0.0.1', username='root', password='xxx')
stdin, stdout, stderr = ssh.exec_command('java -version')
res  = stdout.read().decode('utf-8')
res2 = stderr.read().decode('utf-8')

print(res)  # 输出返回的结果
ssh.close()

def java8_is_install(res):
    flag = False
    try:
        jai = (re.findall(r'(java\ version\ \"1.8.+\")?', res))[0]
        if (jai == "" or jai == None):
            flag = False
        else:
            flag = True
    except:
        flag = False

    return flag