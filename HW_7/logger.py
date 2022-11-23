from datetime import datetime as dt


def calculation_logger(data, answer):
    '''Creates log file with current time and action'''
    time = dt.now().strftime('%H:%M:%S')
    with open('log.txt', 'a', encoding='UTF-8') as file:
        file.write(f'{time}; operation number {answer};  data = {data}\n')
