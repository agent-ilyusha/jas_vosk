# -- coding: utf-8
import os
from os import path
# import sys
# import time
# from fuzzywuzzy import fuzz
# from fuzzywuzzy import process


def recursion_file(folder):
    try:
        for el in os.walk(folder):
            for file in el:
                print(file)
                print(el)
                if file == list():
                    pass
                elif path.isdir(folder+file[0]):
                    recursion_file(folder)

    except PermissionError:
        recursion_file(folder)


list_path = (os.listdir(path.join('C:\\Users\\1\\Desktop\\')))


for el in list_path:
    varib = path.join(path.join('C:\\Users\\1\\Desktop\\'+el))
    if path.isdir(varib):
        file_my = recursion_file(varib)
        if file_my == 1:
            break



