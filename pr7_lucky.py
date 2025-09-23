
import random
import string

def any_number(low=1, high=100):
    return random.randint(low, high)

def mix_list(n=5, low=1, high=50):
    data = list(range(low, high+1))
    random.shuffle(data)
    return data[:n]

def gen_pass(length=8):
    chars = string.ascii_letters + string.digits + "!@#$%&?"
    return "".join(random.choice(chars) for _ in range(length))

def otp_make(digits=6):
    return "".join(str(random.randint(0,9)) for _ in range(digits))
