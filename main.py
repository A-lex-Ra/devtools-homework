import sys
import time

def default():
    print('Привет первый курс')
    print('Всем хорошей домашки')

def main():

    start = time.time()

    default()

    end = time.time()

    working_time = end - start
    
    print(working_time)

if __name__ == '__main__':
    
    main()
    