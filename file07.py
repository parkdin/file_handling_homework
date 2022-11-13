def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    
    num = 0
    for i in data:
        if i.isdigit():
            num += int(i)
    return num
# Read data from file
data = open('txt_file/data07.txt').read()
print(main(data))