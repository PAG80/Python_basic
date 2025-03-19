# Функция для создания текстового файла
def create_sample_file(file_path):
    with open(file_path, 'w') as file:
        file.write('Это пример текста.\nЗдесь несколько строк.\nИ вот еще одна строка.')

# Функция для чтения содержимого файла
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Функция для записи содержимого в файл
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)

# Реверсирование содержимого
def reverse_content(input_file_path, output_file_path):
    original_content = read_file(input_file_path)
    reversed_content = original_content[::-1]
    write_file(output_file_path, reversed_content)
    return original_content, reversed_content

# Вывод содержимого обоих файлов
def display_contents(original_content, reversed_content):
    print('Содержимое исходного файла:')
    print(original_content)
    print('\nСодержимое нового файла (в обратном порядке):')
    print(reversed_content)

# Путь к файлам
input_file_path = 'input.txt'
output_file_path = 'output.txt'

create_sample_file(input_file_path)

original_content, reversed_content = reverse_content(input_file_path, output_file_path)

display_contents(original_content, reversed_content)

