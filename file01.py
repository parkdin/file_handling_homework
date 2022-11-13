def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    list = data.split(" ")
    return list
# Read data from file
data = open('txt_file/data07.txt').read()
print(main(data))