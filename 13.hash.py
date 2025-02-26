class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]  # Создаем список списков для хранения данных

    def _hash(self, key):
        """Собственная хэш-функция для строк."""
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char)) % self.size  # Простой алгоритм хэширования
        return hash_value

    def insert(self, key, value):
        """Добавляет пару ключ-значение в хэш-таблицу."""
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:  # Если ключ уже существует, обновляем значение
                item[1] = value
                return
        self.table[index].append([key, value])  # Если ключ новый, добавляем в цепочку
    

    def __str__(self):
        """Возвращает строковое представление хэш-таблицы."""
        return "\n".join(f"{i}: {items}" for i, items in enumerate(self.table))

    def save_to_file(self, filename):
        """Сохраняет хэш-таблицу в файл."""
        with open(filename, "w", encoding="utf-8") as file:
            for index, items in enumerate(self.table):
                file.write(f"{index}: {items}\n")  # Записываем каждый элемент таблицы


# Пример использования
if __name__ == "__main__":
    # Чтение текста из файла
    with open("13text.txt", "r", encoding="utf-8") as file:
        text = file.read()

    # Разделение текста на слова
    words = text.split()

    # Создание хэш-таблицы
    hash_table = HashTable(size=20)  # Размер таблицы можно настроить

    # Добавление слов в хэш-таблицу (ключ — слово, значение — номер слова)
    for i, word in enumerate(words, start=1):
        hash_table.insert(word, i)

    # Вывод хэш-таблицы
    print(hash_table)

    hash_table.save_to_file("13output.txt")
    print("Хэш-таблица сохранена в файл '13output.txt'")

    