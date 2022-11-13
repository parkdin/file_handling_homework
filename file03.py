def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    num = []
    for i in data:
        if i.isdigit():
            num += i
    return num
data = open('txt_file/data07.txt').read()
print(main(data))
# Read data from file