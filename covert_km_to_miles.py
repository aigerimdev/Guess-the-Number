def am_i_speeding(speed, speed_limit):
    if speed > speed_limit:
        return True
    else:
        return False

def convert_km_to_mi(num):
    return num * 0.62137

def is_valid_num(num):
    return isinstance(num, int) or isinstance(num, float)

