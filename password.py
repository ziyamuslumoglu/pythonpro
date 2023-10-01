import random 
kaliplar="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
len=int(input("şifreniz kaç basamaklı olsun?"))
password="" 
for i in range(len):
    password += random.choice(kaliplar)
 
print(password)


