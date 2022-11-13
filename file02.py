def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data, 'r').read()
    length = len(f)
    return length

# Read data from file
data = 'txt_file/data02.txt'
print(main(data))