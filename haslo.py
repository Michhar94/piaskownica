import random
import string  

n_znakow = 8
n_znakow_typu = 2
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
punctuation = string.punctuation
digits = string.digits

wszystkie_znaki = lowercase + uppercase + punctuation + digits

losowe_znaki = random.sample(wszystkie_znaki, n_znakow)
haslo = '' .join(losowe_znaki)


print()
print(haslo)
print()

