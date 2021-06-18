import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from random import randint
key = "f83ed97a23ab7ddf549c25455088dd6e67edb1abd39c7d360c493c5976406e97f417494ee2e0fdd21c282"
# Авторизуемся как сообщество
vk = vk_api.VkApi(token=key)

def send_message(user_id, message):
    from random import randint
    vk.method('messages.send',
              {'user_id': user_id,
               "random_id":randint(1,1000) ,
               'message': message,}
              )
WHAT = """what?
    supported commands:
    hello
            game
кот
"""
dev_id = 410855977
send_message(dev_id,' OUR CASTLE IS WELLAND RICH')
debug = False
game_mode = False
gamers = {}
# Работа с сообщениями
longpoll = VkLongPoll(vk)
# Основной цикл
for event in longpoll.listen():
    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
            text = event.text.lower()
            user_id = event.user_id
            if user_id == dev_id:
                if text == 'debug':
                    debug = not debug
                    send_message(dev_id,'debug is now '+str(debug))
                if debug:
                    text = ''
                    for i in dir(event):
                        if i[0]!='_':
                            send_message(dev_id,i+' : '+str(eval('event.'+i)))
                    continue
            if text == "hello":
                send_message(user_id, "Hi")
            elif text == "game":
                game_mod = True
                chilso = randint(1,100)
                gamers[user_id] = chislo
                send_message(user_id, "lets go")
            elif user_id in gamers:
                chislo = gamers[user_id]
                x = int(text)
                if chislo < x:
                    send_message(user_id, "моё число меньше")
                elif chislo > x:
                    send_message(user_id, "моё число больше")
                elif chislo == x:
                    send_message(user_id, "you won")
            elif "кот" in text:
                send_message(user_id, "мяу")
            else:
                send_message(user_id, WHAT)
            
