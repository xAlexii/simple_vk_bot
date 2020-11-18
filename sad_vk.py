import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
key = "09c669d9e4b4b25bd5dffd1a5ccf3c5793d408fa87ae5df04ecb3e8244f1c179a8a38c6345b3869a7969f"
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
dev_id = 76904317
send_message(dev_id,' hi i am alive')
debug = False
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
                send_message(user_id, "There is no game yet\n"+WHAT)
            elif "кот" in text:
                send_message(user_id, "мяу")
            else:
                send_message(user_id, WHAT)
            
