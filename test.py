#coding=utf8
import itchat
import random
import func
import name
import myreply
import changereply
import filter

@itchat.msg_register(itchat.content.TEXT)
def anwser(msg):

    #对方昵称
    nickname = msg['User']['NickName']
    print(nickname)
    nickname = name.chang_nickname(nickname)

    #直接回答
    question = msg['Text']
    print("问题：" + question)

    reply = myreply.get_my_reply(question)
    if reply:
        return reply

    #问图灵
    reply = func.get_response_tuling(msg['Text'])
    print("答案："+reply)


    #自定义回答
    reply = changereply.change_reply(reply)

    #过滤词
    reply = filter.do_filter(reply)

    #对方姓名
    if random.randint(1, 5) == 5:
        reply =  reply + ' ' + nickname

    #终极回答
    #reply = "我累了，我现在只会说，我爱丽莉！"

    print("修改后：" + reply)
    print()

    return reply

# 为了让实验过程更加方便（修改程序不用多次扫码），我们使用热启动
itchat.auto_login(hotReload=True)
#itchat.auto_login()
itchat.run()

