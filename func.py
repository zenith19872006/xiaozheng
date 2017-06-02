import requests

#图灵回答
def get_response_tuling(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : '8edce3ce905a4c1dbb965e6b35c3834d',
        'info'   : msg,
        'userid' : 'zz-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return '我爱丽莉！'

#判断输入的语句中是否包含数组中的词，并做相应的处理
#teststr用来做判断的句子
#arr    判断数组
#do     要做什么动作
#orginstr待处理返回句子
#dostr  处理材料
def arr_in_str_do(teststr,arr,do,orginstr,dostr):
    for word in arr:
        if word in teststr:
            # 部分替换
            if do == 'replace':
                return orginstr.replace(word, dostr)
            # 完全替换
            elif do == 'change':
                return dostr
            # 完全替换
            elif do == 'check':
                return 1
            # 追加处理
            elif do == 'add':
                return orginstr+dostr
    if do == 'check':
        return 0
    else:
        return orginstr
