
def infoText(nickname, uid, reputation):
    text = f'''
Ник: {nickname}
Айди: {uid}
Репутация: {reputation}
    '''
    return text

def raiderText(nickname, uid):
    text = f'''
обнаружен очередной детдомовец
его ник: {nickname}
айди: ndc://user-profile/{uid}
он будет кикнут с чата и передан лидерам!
    '''
    return text

messageTypes = [
    "1:0",
    "52:0",
    "53:0",
    "54:0",
    "55:0",
    "56:0",
    "57:0",
    "58:0",
    "59:0",
    "60:0",
    "100:0",
    "114:0",
    "115:0",
    "122:0",
    "123:0",
    "124:0",
    "125:0",
    "126:0",
    "128:0",
    "129:0",
    "65281:0",
    "65282:0",
    "65283:0",
]

randomNumberText = '''
я загадал число! попробуй угадать и получишь 1 снюс
отправь следующее сообщение числом
'''
