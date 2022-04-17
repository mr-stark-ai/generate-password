# generate password
import random # use for generate randomly generate numbers,strings etc
upper_case="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower_case="abcdefghijklmnopqrstuvwxyz"
number="0123456789"
symbol="!@#$%^&*()?/-"

use=upper_case+lower_case+number+symbol # join the upper,lowe,symbols for generate a password

length=8 #length of the generated password
password="".join(random.sample(use,length))

print('your generated password is: ',password) # print the new generated password
