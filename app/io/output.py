def print_to_console(text):
    """
    Prints the given text to the console.

    Args:
        text (str): The text to be printed.
    """
    print(text)


def write_to_file_builtin(file_path, text):
    """
    Writes text to a file using Python's built-in functions.

    Args:
        file_path (str): The path to the file.
        text (str): The text to write to the file.
    """
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(text)


def write_file_pandas(file_path, data):
    """
    Writes the provided data to a CSV file using the pandas library.

    Args:
        file_path (str): The path where the CSV file will be saved.
        data (dict): A dictionary where keys are column names and values are lists of column data.

    Example:
        data = {
            'Name': ['Alice', 'Bob'],
            'Age': [25, 30]
        }
        write_file_pandas('output.csv', data)
    """
    import pandas as pd

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)