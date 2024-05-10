import random

def generate_otp():
    otp = ""
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp

print("Generated OTP:", generate_otp())