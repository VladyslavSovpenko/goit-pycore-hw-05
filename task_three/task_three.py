import collections
import sys
import utils


# Скрипт повинен приймати шлях до файлу логів як аргумент командного рядка.
# Скрипт повинен приймати не обов'язковий аргумент командного рядка, після аргументу шляху до файлу логів. Він відповідає за виведення всіх записи певного рівня логування. І приймає значення відповідно до рівня логування файлу. Наприклад аргумент error виведе всі записи рівня ERROR з файлу логів.
# Скрипт має зчитувати і аналізувати лог-файл, підраховуючи кількість записів для кожного рівня логування (INFO, ERROR, DEBUG, WARNING).
# Реалізуйте функцію parse_log_line(line: str) -> dict для парсингу рядків логу.
# Реалізуйте функцію load_logs(file_path: str) -> list для завантаження логів з файлу.
# Реалізуйте функцію filter_logs_by_level(logs: list, level: str) -> list для фільтрації логів за рівнем.
# Реалізуйте функцію count_logs_by_level(logs: list) -> dict для підрахунку записів за рівнем логування.
# Результати мають бути представлені у вигляді таблиці з кількістю записів для кожного рівня. Для цього реалізуйте функцію display_log_counts(counts: dict), яка форматує та виводить результати. Вона приймає результати виконання функції count_logs_by_level.
#
#
# Рекомендації для виконання:
#
# Перш ніж почати, ознайомтеся зі структурою вашого лог-файлу. Зверніть увагу на формат дати та часу, рівні логування INFO, ERROR, DEBUG, WARNING і структуру повідомлень.
# Зрозумійте, як розділені різні компоненти логу, це зазвичай пробіли або спеціальні символи.
# Розділіть ваше завдання на логічні блоки і функції для кращої читабельності і подальшого розширення.
# Парсинг рядка логу виконує ****функцію parse_log_line(line: str) -> dict, яка приймає рядок з логу як вхідний параметр і повертає словник з розібраними компонентами: дата, час, рівень, повідомлення. Використовуйте методи рядків, такі як split(), для розділення рядка на частини.
# Завантаження лог-файлів виконує функція load_logs(file_path: str) -> list, що відкриває файл, читає кожен рядок і застосовує на нього функцію parse_log_line, зберігаючи результати в список.
# Фільтрацію за рівнем логування виконує функція filter_logs_by_level(logs: list, level: str) -> list. Вона дозволить вам отримати всі записи логу для певного рівня логування.
# Підрахунок записів за рівнем логування повинна робити функція count_logs_by_level(logs: list) -> dict, яка проходить по всім записам і підраховує кількість записів для кожного рівня логування.
# Вивід результатів виконайте за допомоги функції display_log_counts(counts: dict), яка форматує та виводить результати підрахунку в читабельній формі.
# Ваш скрипт повинен вміти обробляти різні види помилок, такі як відсутність файлу або помилки при його читанні. Використовуйте блоки try/except для обробки виняткових ситуацій.
#
#
# Критерії оцінювання:
#
# Скрипт виконує всі зазначені вимоги, правильно аналізуючи лог-файли та виводячи інформацію.
# Скрипт коректно обробляє помилки, такі як неправильний формат лог-файлу або відсутність файлу.
# При розробці обов'язково було використано один з елементів функціонального програмування: лямбда-функція, списковий вираз, функція filter, тощо.
# Код добре структурований, зрозумілий і містить коментарі там, де це необхідно.


def parse_log_line(line: str):
    Record = collections.namedtuple("Record", ["date", "time", "level", "message"])
    match = utils.LOG_PATTERN.match(line)
    if match:
        date, time, level, message = match.groups()
        row = Record(date, time, level, message)
        return row
    else:
        raise ValueError(f"Line does not match pattern: {line}")


def load_file(filename):
    with open(filename) as input_file:
        for line in input_file:
            yield line.strip()


def filter_logs_by_level(logs: list, level: str) -> list:
    if level.upper() in ["INFO", "WARNING", "ERROR", "DEBUG"]:
        return list(filter(lambda x: level.upper() in x, logs))
    else:
        raise ValueError(f"Invalid log level: {level}")


def count_logs_by_level(logs: list) -> dict:
    log_levels = [x[2] for x in logs]
    return collections.Counter(log_levels)


def main():
    if len(sys.argv) < 2:
        raise ValueError("Please provide an input file")
    else:
        filename = sys.argv[1]
        rows = load_file(filename)

        logs = fill_the_list(rows)

        display_logs_by_level(logs, "info")

        display_count_by_level(logs)


def fill_the_list(rows):
    logs = []
    for row in rows:
        log_entry = parse_log_line(row)
        if log_entry:
            logs.append(log_entry)
    return logs


def display_logs_by_level(logs:list, level:str):
    print("Деталі логів для вибраного рівня:", *filter_logs_by_level(logs, level), sep="\n")


def display_count_by_level(logs):
    counter = count_logs_by_level(logs)
    print(f"{'Рівень логування':<17} | {'Кількість':<8}")
    print('-' * 18 + '|' + '-' * 9)
    for level, count in counter.items():
        print(f"{level:<17} | {count:<8}")


if __name__ == '__main__':
    main()
