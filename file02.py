def main(data:str):
    """
    The data is from the file. Return number of characters in the file.
    Args:
        data: str
    Returns:
        int: return answer
    """
    f = open(data).read()
    length = len(f)
    return length

# Read data from file
print(main('txt_file/data02.txt'))