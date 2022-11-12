def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    num = []
    f = open(data).read()
    for i in f:
        if i.isdigit():
            num += i
    return num
print(main('txt_file/data03.txt'))
# Read data from file