def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    num = []
    non_digit = []
    for i in data:
        if i.isdigit():
            num += i
        else:
            non_digit += i
    return non_digit
data = open('txt_file/data04.txt').read()
print(main(data))
# Read data from file