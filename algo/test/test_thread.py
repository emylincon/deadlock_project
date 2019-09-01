from threading import Thread
import time
import os

stop = 0


def yes():
    global stop

    while True:
        if stop == 1:
            print('stopped yes')
            break
        else:
            print('i am yes')
            time.sleep(2)


def yes1():
    global stop

    while True:
        if stop == 1:
            print('stopped yes1')
            break
        else:
            print('i am yes1')
            time.sleep(2)


def yes2():
    global stop

    while True:
        if stop == 1:
            print('stopped yes2')
            break
        else:
            print('i am yes2')
            time.sleep(2)


def yes3():
    global stop

    while True:
        if stop == 1:
            print('stopped yes3')
            break
        else:
            print('i am yes3')
            time.sleep(2)


def start():
    global stop

    list = [yes, yes1, yes2, yes3]
    thread_record = []
    for i in list:
        a = Thread(target=i)
        thread_record.append(a)
        a.daemon = True
        a.start()

    while True:
        x = input('Enter: ')
        if x == 'stop':
            os.system('echo "yes" >> da.py')
            for i in thread_record:
                i.join()
            stop += 1
            time.sleep(2)
            print('\nprogramme terminated')
            break
        else:
            print('you: ', x)


start()
