from variable import *
from root_dir import *
from add_directories import *
from core import *
from general_def import *

def option_root_dir_1():
    print(OK + 'По умолчанию корневой каталог на андроид устройствах:' + RESET)
    print(ERROR + '/data/data/com.termux/files/home/storage/shared' + RESET)
    root_dir(input(TEXT_COLOR_INPUT + 'Укажите корневой каталог: ' + RESET))
    option_ok()


def option_add_dir_2():
    print(OK + 'Список файлов и каталогов для отслеживания:' + RESET)
    with open(VAR_ADD, 'r', encoding='utf-8') as f:
        dir_txt_f = [dir_txt for dir_txt in f.read().split('\n') if dir_txt]
        for dir_txt in dir_txt_f:
            print(dir_txt)
            print_defis()
    print(ERROR + 'Для возврата в предыдущее меню используйте Ctrl+C' + RESET)
    add_directories(input(TEXT_COLOR_INPUT + 'Укажите файлы и папки для очистки: ' + RESET))


def option_del_file_3():
    delet_file_dir()
