import requests,qiniu,getopt,sys
from qiniu import BucketManager

access_key = 'hAr7ttsrGWq-GL5qRea6ApmvIuLmbmu2jkj09fSW'
secret_key = 'uaY-42qUeEFpaLAiotjB9VgYn6X65cqAsvxCQsVi'
bucket_name = 'acegear-html'
file_public_url = 'https://web.acegear.com/'

channels = ['home','jiuyao','android','baidu','UC','tencent','xiaomi','huawei','sumsang','oppo','qiku']
apknames_withchannel = []
version_code = 0
version_name = ''
try:
    opts, args = getopt.getopt(sys.argv[1:],"c:n:")
except getopt.GetoptError:
    sys.exit()
for opt, arg in opts:
    if opt == "-c":
        version_code = int(arg)
    if opt == "-n":
        version_name = arg

if version_code!=0 and version_name:
    print("options right :%s-%d" % (version_name, version_code))
else:
    print("no options!")
    sys.exit()
# sys.exit()
# version_code = 18
# version_name = '2.2.5'

for index in range(len(channels)):
    apknames_withchannel.insert(index, 'ag%d-%s-release.apk' % (version_code,channels[index]))

q = qiniu.Auth(access_key, secret_key)
localfilebase = '/Users/huangzilong/android/androidprojects/AceGearReborn/app/'
for ac in apknames_withchannel:
    print ac
    key = 'apk/%s' % ac
    localfile = localfilebase + ac
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = qiniu.put_file(token, key, localfile)
    if ret is not None:
        print('upload success/%s' % ac)
        print(file_public_url+key)
        version_url = "https://api2.acegear.cn/version"
        ps = {'os': 'android', 'channel': channels[apknames_withchannel.index(ac)], 'version': version_code, 'info': version_name,
              'download': file_public_url+key}
        response = requests.post(version_url, data=ps)
        print(response.text)
    else:
        print(info) # error message in info



# url = "https://api2.acegear.cn/version"
# ps = {'os':'android','channel':'python','version':'10','info':'2.2.1','download':'http://www.baidu.com'}

# response = requests.post(url, data=ps)
# jsonr = response.json()

# requests.post(url,data=response.text)

# print(response.text)
