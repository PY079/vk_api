# Импорт access_token и id группы, вам 2 строку кода писать не нужно
from toke1 import toke, own_id
import vk_api, os, sys

def menu(): # Создаем меню
    print('''
1. Ифно о последнем посте
2. Создать пост
3. Удалить последний пост
0. ВЫХОД
    ''')
    try:
        vvod = int(input('Введите номер --> '))
        os.system('cls')
        if vvod == 1:
            wall_get()
        if vvod == 2:
            wall_post()
        if vvod == 3:
            wall_del()
        if vvod == 0:
            sys.exit()
    except ValueError: # Если пользователь ввёл буквы
        os.system('cls')

def con(): # Создаём подключени
    os.system('cls')
    global session, vk
    session = vk_api.VkApi(token=toke) 
    vk = session.get_api()


def wall_get(): 
    global mes_id
    wal = vk.wall.get(owner_id=own_id, count=1, offset=0)
    #print(wal)
    items = wal['items'] # Выбираем список items 

    for i in items:
        mes_text = i['text'] # Текст с поста
        mes_id = i['id'] # id поста (номер поста за всё существование стриницы)

    try:   
        print(f'Текст:\n\n{mes_text}\n')
        print(f'Id поста - {mes_id}')
    except UnboundLocalError:
        print(f'Получение поста - НЕУСПЕШНО\n')

def wall_post(): # Постим абсолютно любой текст
    a = vk.wall.post(owner_id = own_id, close_comments=1, message='''
        Hello world 
                ''')
    wall_get() 
            
def wall_del(): #Удаляем последний пост 
    a = vk.wall.delete(owner_id = own_id, post_id = mes_id)
    wall_get()

if __name__ == "__main__": # Для удобства 
    con()
    while True:
        menu()
