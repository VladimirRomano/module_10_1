import time
import threading

def  write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count + 1):
            file.write(f'Какое-то слово № {i}' + '\n')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

start_time = time.time()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

end_time = time.time()
s_t = round(end_time - start_time, 3)
print(f"Работа функций {s_t} секунд")

start_time_thread = time.time()

t_1 = threading.Thread(target=write_words, args=(10, 'example5.txt'))
t_2 = threading.Thread(target=write_words, args=(30, 'example6.txt'))
t_3 = threading.Thread(target=write_words, args=(200, 'example7.txt'))
t_4 = threading.Thread(target=write_words, args=(100, 'example8.txt'))

t_1.start()
t_2.start()
t_3.start()
t_4.start()

t_1.join()
t_2.join()
t_3.join()
t_4.join()

end_time_threads = time.time()
s_tr = round(end_time_threads - start_time_thread, 3)
print(f"Работа потоков {s_tr} секунд")