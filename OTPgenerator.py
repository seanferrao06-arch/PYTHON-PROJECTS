import random

def otp_generator():
    otp = random.randint(1000,9999)
    return otp  

Otp = otp_generator()
print("Your OTP is:", Otp)
