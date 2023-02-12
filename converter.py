def convert(num):
    if type(num) == int or int(num) == num:
        return str(bin(int(num)))[2:]

    bin_string = ""
    number = str(num)
    place = 0.5

    whole, fractional = number.split('.', 1)

    bin_string += str(bin(int(whole))) + '.'

    bin_string = bin_string[2:]

    fractional = int(fractional) / 10**len(fractional)

    while fractional > 0:
        print(place, fractional % place == 0, fractional, place)
        if fractional % place == 0:
            bin_string += '1'
            fractional -= place
        else:
            bin_string += '0'

        place /= 2

    return bin_string
