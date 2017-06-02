#屏蔽词
def do_filter(reply):
    list = ['不打扰了哈']

    for word in list:
        reply = reply.replace(word,'~');

    return reply
