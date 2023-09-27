# --encoding: utf-8

from os import system


def kill_process(name_process: str = ' ') -> str:
    system('tasklist > task_list.txt')
    with open('task_list.txt', 'r') as file_task_list:
        for el in file_task_list.readlines():
            # if
            pass
    return 'Файл не был найден'


kill_process(name_process='1768')
