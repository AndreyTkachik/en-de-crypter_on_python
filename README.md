# Шифровальщик на питоне

## Основной функционал
- Несколько режимов работы (описаны ниже). Режим выбирается с помощью аргументов командной строки.
- Шифрование и дешифрование файлов шифрами Цезаря, Виженера и Вернама.
- Пути к файлам должны передаваться как аргументы командной строки.
- Автоматический взлом шифра Цезаря методами частотного анализа.

## Архитектура
Проект представляет собой 5 файла, 3 из кторых - это файлы с кодировками, файл с константами для частотного анализа и файл, который выполняет саму работу шифровальщика и предоставляет графический интерфейс.

## Запуск
```
python3 main.py
```

Ключ требуется только при шифровании или явном дешифровании.

### Поддерживаемые инструкции:
- caesar_encrypt
- caesar_decrypt
- caesar_brute_force
- caesar_frequency_analysis_decrypt
- vigenere_encrypt
- vigenere_decrypt
- vernam_encrypt
- vernam_decrypt

## Функционал
Слева графический интерфейс, справа открыт редактор текста для того чтобы контролировать шифровку текста.
![alt text](https://github.com/AndreyTkachik/en-de-crypter_on_python/blob/in_progress/images/1.png?raw=true)
Применение шифра Цезаря.
![alt text](https://github.com/AndreyTkachik/en-de-crypter_on_python/blob/in_progress/images/2.png?raw=true)
![alt text](https://github.com/AndreyTkachik/en-de-crypter_on_python/blob/in_progress/images/3.png?raw=true)
Явная дешифровка шифра Цезаря.
![alt text](https://github.com/AndreyTkachik/en-de-crypter_on_python/blob/in_progress/images/4.png?raw=true)
Применение шифра Цезаря.
![alt text](https://github.com/AndreyTkachik/en-de-crypter_on_python/blob/in_progress/images/5.png?raw=true)
Дешифровка с использованием частотного анализа.
![alt text](https://github.com/AndreyTkachik/en-de-crypter_on_python/blob/in_progress/images/6.png?raw=true)
