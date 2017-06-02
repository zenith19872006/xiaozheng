import random
import func

#我的答案
def get_my_reply(question):

    list = [
            [
                ['爱'],
                ['嗯，我爱丽莉','我爱丽莉啊']
            ],
            [
                ['老婆','单身','结婚'],
                ['我老婆是丽莉']
            ],
            [
                ['呵呵'],
                ['呵呵这个词可不要随便讲哦，会被揍的，吼吼吔','嘻嘻']
            ],
        ]

    for l in list:
        if func.arr_in_str_do(question, l[0], 'check', question, ''):
            return l[1][random.randint(1, len(l[1]))-1]

    return 0