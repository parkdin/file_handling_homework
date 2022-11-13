def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    max_char = 0
    for i in data:
        if i.isdigit():
            if int(i) > max_char:
                max_char = int(i)
    return max_char
# Read data from file
data = open('txt_file/data08.txt').read()
print(main(data))