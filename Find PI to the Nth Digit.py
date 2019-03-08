import math as m
import cmath as mc

def find_pi_to_Nth_digit(Nth_digit):
    return '{0:.{1}f}'.format(mc.pi, Nth_digit)

if __name__ == '__main__':
    print (find_pi_to_Nth_digit(2))
