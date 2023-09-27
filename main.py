# --coding: utf-8
import random
import json
import speech
import torch_iter
import os


def start_func():
    with open('json_files/command_json.json', encoding='utf-8') as file:
        var = json.load(file)
        list_my_name = var['my_name']
        list_answer = var['answer_bot']

    torch_iter.torch_func(f'Привет,{random.choice(list_my_name)}')
    while True:
        torch_iter.torch_func(speech.sound_pad())


if __name__ == "__main__":
    start_func()

