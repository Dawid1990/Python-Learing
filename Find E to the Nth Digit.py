import math

def find_e_to_the_Nth_digit(Nth_digit):
    if Nth_digit > 20:
        return '{}{}'.format(Nth_digit, " is too large")
    else:
        return '{0:.{1}f}'.format(math.e, Nth_digit)

if __name__ == "__main__":
    print find_e_to_the_Nth_digit(2)