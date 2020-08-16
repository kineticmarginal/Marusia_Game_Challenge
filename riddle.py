## -*- coding: utf-8 -*-
import random
import os
from os import path

def wordsTopicOpen(filename='Covid.txt'):
    words = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line_temp = line.split()
            words_temp = [line_temp[0], line_temp[1], ' '.join(line_temp[2:])]
            words.append(words_temp)
        f.close()
    return words

def shuffleWords(words):
    random.shuffle(words)
    return words

def wordPlay(word):
    riddle = word[0]
    trans = word[1]
    example = word[2]
    word_len = len(riddle)
    print("\nСлово состоит из " + str(word_len) + " букв.")
    print("У тебя есть " + str(word_len + int(word_len/3)) + " попыток!")
    print("Для получения подсказки введи в поле ответа 'letter' или 'example'.")
    # Добавить получение подсказки
    # 1 - открыть одну букву
    # 2 - показать пример с пропущенным словом
    guessed_letters = 0
    rede = ['_' for i in range(word_len)]

    key = False
    letter_key = True
    example_key = True
    for j in range(word_len + int(word_len/3)):
        for r in rede:
            print(r, end=' ')
        answer = input(' Буква или слово: ')

        if answer == 'letter' and not letter_key:
            print("Ты уже использовал эту подсказку!")
        if answer == 'letter' and letter_key:
            letter_key = False
            hint = ''
            for i in range(word_len):
                if rede[i] == '_':
                    hint = riddle[i]
                    break
            for i in range(word_len):
                if riddle[i] == hint:
                    rede[i] = riddle[i]
                    guessed_letters += 1

        if answer == 'example' and not example_key:
            print("Ты уже использовал эту подсказку!")
        if answer == 'example' and example_key:
            example_key = False
            s = example.split()
            for word in s:
                word = word.lower()
                if riddle not in word:
                    print(word + ' ', end='')
                else:
                    for r in rede:
                        print(r, end=' ')
            print()

        else:
            if answer in riddle and answer not in rede:
                for i in range(word_len):
                    if riddle[i] == answer:
                        rede[i] = riddle[i]
                        guessed_letters += 1
            if answer == riddle:
                print('Молодец, ты угадал!')
                print(riddle + ' - ' + trans + '. ' + example)
                key = True
                break
        if guessed_letters == word_len:
            print('Молодец, ты угадал!')
            print(riddle + ' - ' + trans + '. ' + example)
            key = True
            break
    if not key:
        print("Ты был близок.")
        print("Загаданное слово: " + riddle + ' - ' + trans + '. ' + example)
        print("Попробуй ещё раз!")

def chooseTopic():
    words_topic = input('\nВыбери тему: ')
    words = wordsTopicOpen(str(directory + '/' +words_topic + '.txt'))
    words = shuffleWords(words)
    return words

def wordHandler():
    showTopic()
    words = chooseTopic()

    for word in words:
        wordPlay(word)
        command = int(input('\nДля продолжения игры введите цифру 1, для смены темы - 2, для выхода - 3: '))
        if command == 2:
            wordHandler()
            return 0
        if command == 3:
            print('Спасибо за игру!')
            return 0

def showTopic():
    files = os.listdir(directory)
    print('\nДоступные темы: ', end='')
    for file in files:
        name = path.splitext(file)[0]
        print(name + ', ', end='')

directory = './data'
print("\nОтгадай все буквы в слове на английском языке для получения перевода и примера с этим словом.")
print("У тебя есть 2 подсказки: открытие одной буквы в слове или показ примера с этим словом.")
print("Да прибудет с тобой сила!")
wordHandler()
