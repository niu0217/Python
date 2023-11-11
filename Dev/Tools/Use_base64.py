import base64

# base64处理的是byte类型的数据，所以在字符串之前需加上b
pwd_after_encrypt = base64.b64encode(b'this is a scret!')
# 若想解密得到字符串类型的密码，则需用’ascii’来decode byte类型的数据
pwd_before_encrypt = base64.b64decode(b'dGhpcyBpcyBhIHNjcmV0IQ==').decode('ascii')

print(pwd_after_encrypt)
print(pwd_before_encrypt)
