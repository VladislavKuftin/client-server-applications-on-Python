import platform
import subprocess
from chardet import detect

 #Задание 1: Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и проверить тип и содержание соответствующих переменных.
 #Затем с помощью онлайн-конвертера преобразовать строковые представление в формат Unicode и также проверить тип и содержимое переменных

print("part 1")
word1 = "разработка"
word2 = "сокет"
word3 = "декоратор"

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)

word1 = "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"
word2 = "\u0441\u043e\u043a\u0435\u0442"
word3 = "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"

print(type(word1), type(word2), type(word3))
print(word1, word2, word3)
print('\n')


#Задание 2: Каждое из слов «class», «function», «method» записать в байтовом типе.
#Сделать это необходимо в автоматическом, а не ручном режиме, с помощью добавления литеры b к текстовому значению,
#(т.е. ни в коем случае не используя методы encode, decode или функцию bytes) и определить тип, содержимое и длину соответствующих переменных.


print("part 2")
i=input('Введите ваше слово:\n')
var = eval('b'+'"'+i+'"')

print('тип переменной: {}\n'.format(type(var)))
print('содержание переменной - {}\n'.format(var))
print('длинна строки: {}\n'.format(len(var)))



#Задание 3: Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
#Важно: решение должно быть универсальным, т.е. не зависеть от того, какие конкретно слова мы исследуем.

########################################################################
print("part 3")
VAR_1 = 'attribute'
VAR_2 = 'класс'
VAR_3 = 'функция'
VAR_4 = 'type'

WORDS = [VAR_1, VAR_2, VAR_3, VAR_4]

for word in WORDS:
    if not word.isascii():
        print(f'Слово "{word}" невозможно записать в виде байтовой строки')


#Задание 4: Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
#и выполнить обратное преобразование (используя методы encode и decode).


########################################################################
print("part 4")
word1 = input('Введите ваше слово:\n').encode('utf-8')
print(word1)
print(word1.decode('utf-8'))

#Задание 5: Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
########################################################################


print("part 5")
urls = ['yandex.ru', 'youtube.com']
code = '-n' if platform.system().lower() == 'windows' else '-c'

for url in urls:
    args = ['ping', code, '4', url]
    YA_PING = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in YA_PING.stdout:
        result = detect(line)
        print(result)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))


# Задание 6: Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор».
# Далее забыть о том, что мы сами только что создали этот файл и исходить из того, что перед нами файл в неизвестной кодировке.
# Задача: открыть этот файл БЕЗ ОШИБОК вне зависимости от того, в какой кодировке он был создан.
########################################################################


# print("part 6")
# resurs_string = ['сетевое программирование', 'сокет', 'декоратор']
#
# # Создаем файл
# with open('test.txt', 'w+') as f_n:
#     for i in resurs_string:
#         f_n.write(i + '\n')
#     f_n.seek(0)
#
# print(f_n)  # печатаем объект файла, что бы узнать его кодировку
#
# file_coding = locale.getpreferredencoding()
#
# # Читаем из файла
# with open('resurs.txt', 'r', encoding=file_coding) as f_n:
#     for i in f_n:
#         print(i)
#
#     f_n.seek(0)
#
#

LINES_LST = ['сетевое программирование', 'сокет', 'декоратор']
with open('test.txt', 'w') as file:
    for line in LINES_LST:
        file.write(f'{line}\n')
file.close()

# узнаем кодировку файла
with open('test.txt', 'rb') as file:
    CONTENT = file.read()
ENCODING = detect(CONTENT)['encoding']
print(ENCODING)

# открываем файл в правильной кодировке
with open('test.txt', 'r', encoding=ENCODING) as file:
    CONTENT = file.read()
print(CONTENT)