from aiogram import types
from misc import dp

list1 = []


def get_chat_list(prm_chat_id):
    print(list1)
    items = [list_index for list_index, (chat_index, _, _) in enumerate(list1) if chat_index == prm_chat_id]
    if items:
        print(items[0])
        return [list1[items[0]][1], list1[items[0]][2]]
    else:
        list1.append([prm_chat_id, [], 1])
        return []


def set_chat_list(prm_chat_id, prm_chat_list, prm_chat_item):
    print(list1)
    print(prm_chat_list)
    items = [list_index for list_index, (chat_index, _, _) in enumerate(list1) if chat_index == prm_chat_id]
    list1[items[0]][1] = prm_chat_list
    list1[items[0]][2] = prm_chat_item


@dp.message_handler()
async def echo(message: types.Message):
    message_text = message.text
    chat_answer = get_chat_list(message.chat.id)
    print(chat_answer)
    chat_list = []
    chat_index = 1
    if chat_answer:
        chat_list = chat_answer[0]
        chat_index = chat_answer[1]

    s = ''

    if message_text.startswith('/del_'):
        item_found = message_text[5:]
        items = [i for i, (_, x) in enumerate(chat_list) if x == int(item_found)]
        if items:
            s = u'\U00002757'+'Вы удалили: '+chat_list[items[0]][0]+'\n\n'
            del chat_list[items[0]]
    else:
        message_text_list = message_text.split('\n')
        for it in message_text_list:
            chat_list.append([it, chat_index])
            chat_index = chat_index + 1

    print(chat_list)
    for it in chat_list:
        if it[0]:
            s = s + u'\U00002705'+' '+it[0]+'\t/del_'+str(it[1])+'\n\n'
    if chat_list:
        await message.reply(s)
    else:
        await message.reply('Ваш список пуст')
    set_chat_list(message.chat.id, chat_list, chat_index)
