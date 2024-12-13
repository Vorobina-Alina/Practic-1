# Practic-1
#Практическая 1
1. Переход в директорию lab1 из директории Practic-1 осуществляется при помощи команды cd
2. С помощью команды touch создаем файлы task1.py, task2.py, task3.py, errors.txt, output.txt
3. команда nano используется для того, чтобы открыть файл для редактирования. Сохраняем изменения при помощи ctrl+o, выходим при помощи ctrl+x
4. Файлы task1.py, task2.py, task3.py были сделаны исполняемыми при помощи команды chmod +x
5. Конвейер был запущен при помощи команды ./task1.py|./task2.py|./task3.py >output.txt 2>errors.txt
6. На выход в консоли оказалась пустая строка, а результат работы программы был записан в файл output.txt

#Практическая 2

1. В директории Practic-1 создаем директорию lab2 при помощи команды cd
2. Созадем файл PracticTask2.py
3. Редактируем содержимое файла с помощью nano PracticTask2.py, сохраняем изменени с помоью ctrl+o и выходим из редактора с помощью ctrl+x
4. Те же операции проделываем для файла names.txt, который содержит список имен
5. созадем файл errors.txt
6. Файл PracticTask2.py делается исполняемым при помощи команды chmod +x
7. Для запуска программы в первом режиме используем команду ./PracticTask2.py <names.txt 2>errors.txt
8. На выход получаем: Nice to see you Masha! Nice to see you Nadya! Nice to see you Nastya! Nice to see you Dasha!
9. в файл errors.txt записалось Error: Name 'alina' needs to start with an uppercase letter! Error: Name 'natasha' needs to start with an uppercase letter! Error: Name 'sonya' needs to start with an uppercase letter! Error: Name 'katya' needs to start with an uppercase letter! Error: Name 'lena' needs to start with an uppercase letter! Error: Name 'kristina' needs to start with an uppercase letter!
10. Для запуска программы во втором режиме используем команду ./PraticTask2.py
11. На выход получаем: Hey, what's your name?
12. Вводим: Alina
13. Вывод: Nice to see you Alina! Hey, what's your name?
14. Нажимаем Ctrl+c
15. Получаем: Hey, what's your name? ^C Goodbye!
