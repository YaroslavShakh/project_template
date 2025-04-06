# main.py

from app.io.input import input_from_console, read_file_builtin, read_file_pandas
from app.io.output import print_to_console, write_to_file_builtin

def main():

    console_text = input_from_console()


    try:
        builtin_text = read_file_builtin("input.txt")
    except FileNotFoundError:
        builtin_text = "Файл не знайдено (builtin)."


    try:
        pandas_text = read_file_pandas("input.csv")
    except Exception as e:
        pandas_text = f"Помилка з pandas: {e}"


    print_to_console(console_text)
    print_to_console(builtin_text)
    print_to_console(pandas_text)


    write_to_file_builtin("output.txt", f"{console_text}\n\n{builtin_text}\n\n{pandas_text}")


if __name__ == "__main__":
    main()
