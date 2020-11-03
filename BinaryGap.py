def BinaryGap(N):
    """
    Determines the maximum 'binary gap' in an integer
    :return: a count of the longest sequence of zeros in the binary representation of the integer
    """
    # protect against crazy inputs
    if not isinstance(N, int):
        raise TypeError("Input must be an integer")
    if N < 1:
        raise ValueError("Input must be a positive integer")
    print ((bin(N)))
    # convert the number to a string containing '0' and '1' chars
    binary_string = str(bin(N))[2:]
    print (binary_string)
    count=0
    count_list = []
    for i in binary_string: 
        if (i=='1'):
            count_list.append(count)
            count=0
        else:
            count=count+1
    print("Longest Binary Gap",max(count_list))
    return max(count_list)
class TestBinaryGap():
    if __name__ == '__main__':
        print(BinaryGap(10))