def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    f = open(data).read()
    digit = 0
    non_digit = 0
    for i in f:
        if i.isdigit():
            digit += 1
        else:
            non_digit += 1
    return [digit, non_digit]

print(main('txt_file/data05.txt'))
# Read data from file