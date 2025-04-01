import requests


login_url = "http://10.100.1.5/eportal/InterFace.do?method=login"


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Accept': '*/*',
    'Origin': 'http://10.100.1.5',
    'Referer': 'http://10.100.1.5/eportal/index.jsp?wlanuserip=852741297bb41a1b390659a3b6044f4c&wlanacname=a57672291393aa19&ssid=&nasip=bda1d0b1a7e3370d3b3a8a85599b4300&snmpagentip=&mac=b2fcfcfde2a45affbdd40517301bbd25&t=wireless-v2&url=2c0328164651e2b4f13b933ddf36628bea622dedcc302b30&apmac=&nasid=a57672291393aa19&vid=30953b9cab08e6f7&port=8bd1bb9d7a29cbc6&nasportid=5b9da5b08a53a5403369c3a2784609dbc8ad14ec61bcfd09890945fb4b96e7ac7c8dda32ebafbb46',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'close'
}


data = {
    'userId': '', # 这里输入学号
    'password': '', # 这里输入密码
    'service': '%E4%B8%AD%E5%9B%BD%E7%94%B5%E4%BF%A1',
    'queryString': 'wlanuserip%3D852741297bb41a1b390659a3b6044f4c%26wlanacname%3Da57672291393aa19%26ssid%3D%26nasip%3Dbda1d0b1a7e3370d3b3a8a85599b4300%26snmpagentip%3D%26mac%3Db2fcfcfde2a45affbdd40517301bbd25%26t%3Dwireless-v2%26url%3D2c0328164651e2b4f13b933ddf36628bea622dedcc302b30%26apmac%3D%26nasid%3Da57672291393aa19%26vid%3D30953b9cab08e6f7%26port%3D8bd1bb9d7a29cbc6%26nasportid%3D5b9da5b08a53a5403369c3a2784609dbc8ad14ec61bcfd09890945fb4b96e7ac7c8dda32ebafbb46',
    'operatorPwd': '',
    'operatorUserId': '',
    'validcode': '',
    'passwordEncrypt': 'false'
}

response = requests.post(login_url, data=data, headers=headers)
print(response.text)

if "success" in response.text:
    print("登录成功")
else:
    print("登录失败")