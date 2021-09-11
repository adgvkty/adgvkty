from telethon import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest

client_name = ''  # придумываете сами
client_id = 0  # получаем во время создания кастомного клиента
client_hash = ''  # аналогично с предыдущим пунктом

client = TelegramClient(client_name, client_id, client_hash)


async def get_message():
    c_username = ''  # cюда писать юзерку канала
    channel_entity = await client.get_entity(c_username)
    last_post_id = await client(GetHistoryRequest(peer=channel_entity,
                                                  limit=0,
                                                  offset_date=None,
                                                  offset_id=0,
                                                  max_id=0,
                                                  min_id=0,
                                                  add_offset=0,
                                                  hash=0))
    last_post_id = last_post_id.messages[0].id  # получаем ид самого последнего сообщения, де-факто их кол-во
    for i in range(last_post_id):
        post = await client(GetHistoryRequest(
            peer=channel_entity,
            limit=0,
            offset_date=None,
            offset_id=i,  # фактически, указываем id скачиваемого сообщения, практически у оффсета другой принцип
            max_id=0,
            min_id=0,
            add_offset=0,
            hash=0))
        if post.messages:  # проверка есть ли в посте вообще сообщение (фильтр на тех. сообщения)
            if post.messages[0].media:  # проверка на наличие медиа в сообщении
                await client.download_media(post.messages[0].media, "\directory\suka")
                # если не указать директорию, то оно будет качаться в папку со скриптом
                print(f'Done, msg_id = {i}')  # вывод сообщения с id скачаного сообщения для ощущения прогресса


with client:
    client.loop.run_until_complete(get_message())  # залупываем функцию
