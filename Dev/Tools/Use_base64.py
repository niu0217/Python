import base64


"""
示例：7~12行
"""
# base64处理的是byte类型的数据，所以在字符串之前需加上b
# pwd_after_encrypt = base64.b64encode(b'this is a scret!')
# 若想解密得到字符串类型的密码，则需用’ascii’来decode byte类型的数据
# pwd_before_encrypt = base64.b64decode(b'dGhpcyBpcyBhIHNjcmV0IQ==').decode('ascii')
# print(pwd_after_encrypt)
# print(pwd_before_encrypt)

"""
加密自己想要的数据：
"""
user = base64.b64encode(b'19502357024@163.com')
passward = base64.b64encode(b'OCCEELWFGVMQLLZP')

print(user)
print(passward)

