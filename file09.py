def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    min_char = 0
    for i in data:
        if i.isdigit():
            if int(i) < min_char:
                min_char = int(i)
    return min_char
# Read data from file
data = open('txt_file/data08.txt').read()
print(main(data))