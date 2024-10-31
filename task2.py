import threading
import os.path
import time

event = threading.Event()

def read_file():
    with open('wow.txt', 'r', encoding='utf-8') as f:
       if os.path.exists('wow.txt'):
           f.read()
           if 'Wow!' in f:
               f.close()
               event.set()
       else:
           time.sleep(5)


read_file()

def file_wait():
    event.wait()
    with open('wow.txt', 'r', encoding='utf-8') as file:
        if event:
            os.remove('wow.txt')
        elif 'Wow!' in file:
            time.sleep(5)


file_wait()