def decimal_to_binary(decimal_num):
    binary_list = [0]*8
    quotient = decimal_num
    i = 7
    while quotient > 0:
        remainder = quotient % 2
        quotient = quotient // 2
        binary_list[i] = remainder
        i -= 1
    binary_str = "".join([str(num) for num in binary_list])
    return binary_str

def decimal_to_hex(decimal_num):
    hex_list = [0]*2
    quotient = decimal_num
    i = 1
    while quotient > 0:
        remainder = quotient % 16
        quotient = quotient // 16
        if remainder < 10:
            hex_list[i] = remainder
        else:
            hex_list[i] = chr(ord('A') + remainder - 10)
        i -= 1
    hex_str = "".join([str(num) for num in hex_list])
    return hex_str

decimal_num = int(input("Enter a decimal number between 0 and 255: "))
binary_num = decimal_to_binary(decimal_num)
hex_num = decimal_to_hex(decimal_num)
print("Decimal: {}\nBinary: {}\nHexadecimal: {}".format(decimal_num, binary_num, hex_num))
