def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data).read()
    num = []
    non_digit = []
    for i in f:
        if i.isdigit():
            num += i
        else:
            non_digit += i
    return non_digit
print(main('txt_file/data04.txt'))
# Read data from file