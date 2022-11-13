def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    length = len(data)
    return length

# Read data from file
data = open('txt_file/data07.txt').read()
print(main(data))