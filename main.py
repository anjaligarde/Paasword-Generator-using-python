import random
import string

small_letters=list(string.ascii_lowercase)
capital_letters=list(string.ascii_uppercase)
number=['1','2','3','4','4','5','6','7','8','9','0']
symbols=['~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=',':',';','"',"'",',','<','>','.','/','*','?','/','|',
         '{','}','[',']'
]

password=[]
cap=int(input("How many capital alphabets you want in your Password? :"))
for i in range(0,cap+1):
  password+=random.choice(capital_letters)

small=int(input("How many small alphabets you want in your password :"))
for j in range(0,small+1):
  password+=random.choice(small_letters)

sym=int(input("How many symbols you want in your Password? :"))
for i in range(0,sym+1):
  password+=random.choice(symbols)

num=int(input("How many numbers you want in your Password? :"))
for i in range(0,num+1):
  password+=random.choice(number)

random.shuffle(password)
passwords=""
for a in password:
    passwords+=a

print("Your Password is",passwords)
