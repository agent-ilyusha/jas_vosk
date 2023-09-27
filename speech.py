# -- coding: utf-8
import vosk
from vosk import Model
import json
import sys
import sounddevice as sd
import queue
import module_time
from os import path
from fuzzywuzzy import fuzz
import morphy
import os


# Frame Rate
def callback(indata, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(bytes(indata))


def check_word(w1: str, w2: list) -> str:
    word = ('0', 0)

    for el in w2:
        if fuzz.partial_ratio(w1, el) > word[1]:
            word = (el, fuzz.partial_ratio(w1, el))

    return word[0]


def del_command_word(txt: str):
    with open(path.join('json_files/command_json.json'), encoding='utf-8') as file_command:
        command_list = json.load(file_command)['command_word']
        txt_list = txt.split()
        new_txt = ''
        for el in txt_list:
            if el not in (command_list or accelerating_words):
                new_txt += el + ' '
        return new_txt  # [::].split(' ')


def sound_pad():
    with sd.RawInputStream(samplerate=FRAME_RATE,
                           blocksize=8000,
                           device=DEVICE,
                           dtype='int16',
                           channels=1,
                           callback=callback):

        rec = vosk.KaldiRecognizer(MODEL, FRAME_RATE)
        while True:
            data = q.get()
            if rec.AcceptWaveform(data):
                var = rec.FinalResult()
                print(json.loads(var)['text'])
                # if set(json.loads(var)['text'].split()).intersection(accelerating_words):
                #     torch_iter.torch_func('сделаю все возможное')

                varib_func = del_command_word(json.loads(var)['text'])
                print(varib_func)
                if morphy.check_word_func(varib_func.split(' '), 'время') >= 80:
                    return module_time.time_func()

                elif morphy.check_word_func(varib_func.split(' '), 'дата') >= 80:
                    return module_time.data_func()

                elif morphy.check_word_func(varib_func.split(' '), 'погода') >= 80:
                    import main_for_kivy
                    varib_func = varib_func.split(' ')
                    del_word = check_word('погода', varib_func)
                    varib_func.remove(del_word)
                    clear_text = morphy.func_del_morthy(varib_func)
                    main_for_kivy.func_start(city=' '.join(clear_text))

                elif morphy.check_word_func(varib_func.split(' '), 'выключись') >= 80:
                    exit()

                else:
                    return 'Скажи еще раз и внятно, пожалуйста'


q = queue.Queue()
FRAME_RATE = 16000
CHANNELS = 1
MODEL = Model("vosk-model-ru-0.22")
DEVICE = 0
with open('json_files/command_json.json', encoding='utf-8') as file:
    var = json.load(file)
    accelerating_words = set(var['accelerating_words'])
    answer_comm = var['answer_bot']
