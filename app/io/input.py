def input_from_console():
    """
    Receives text input from the user via the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Enter text: ")


def read_file_builtin(file_path):
    """
    Reads the content of a file using Python's built-in functions.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The content of the file as a string.
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def read_file_pandas(file_path):
    """
    Reads the content of a CSV file using the pandas library.

    Args:
        file_path (str): The path to the CSV file.

    Returns:
        str: A string representation of the DataFrame without index.
    """
    import pandas as pd
    df = pd.read_csv(file_path)
    return df.to_string(index=False)
