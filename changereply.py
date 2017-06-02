import random
import func

#我的答案
def change_reply(reply):

    list = [
            [
                ['小笼包'],
                'replace',
                '小拯'
            ],
            [
                ['是女孩', '的女孩'],
                'change',
                '我是帅哥'
            ],
            [
                ['呵呵'],
                'replace',
                '嘻嘻'
            ],
            [
                ['爱'],
                'change',
                '我爱丽莉的'
            ],
        ]

    for l in list:
        reply = func.arr_in_str_do(reply, l[0], l[1], reply, l[2])

    return reply