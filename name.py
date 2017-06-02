#昵称替换
def chang_nickname(nickname):

    dict = {'张拯': '主人',
            'lily-D': '乖乖',
            'Yvonne不在线': '娅娅',
            'Yvonne Du': '滢滢',}

    for i in dict:
        if i == nickname:
            return dict[i]

    return nickname