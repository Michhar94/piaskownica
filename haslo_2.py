import random
import string
import secrets
 
# Generator Hasła
# - string
# - losowe hasło
# - określo ilość znaków - ponad 8
# - Duże litery
# - małe litery
# - cyfry
# - znaki specjalne
 
 
n_znakow = input('Podaj ilość znaków (musi być w przedziale 8-20):')
n_znakow = int(n_znakow)
if n_znakow < 8 or n_znakow > 20:
    print('Nieprawidłowa ilość znaków')
 
 
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
digits = string.digits
punctuation = string.punctuation
 
 
digits = ''.join(random.choice(digits) for i in range(n_znakow//4))
lowercase = ''.join(random.choice(lowercase) for i in range(n_znakow//4))
uppercase = ''.join(random.choice(uppercase) for i in range(n_znakow//4))
punctuation = ''.join(random.choice(punctuation) for i in range(n_znakow//4))
wszystkie_znaki = digits + lowercase + uppercase + punctuation
if len(wszystkie_znaki) < n_znakow:
    brakujace = n_znakow - len(wszystkie_znaki)
    if brakujace == 3:
        wszystkie_znaki += ''.join(random.choice(lowercase))
        wszystkie_znaki += ''.join(random.choice(uppercase))
        wszystkie_znaki += ''.join(random.choice(punctuation))
    elif brakujace == 2:
        wszystkie_znaki += ''.join(random.choice(lowercase))
        wszystkie_znaki += ''.join(random.choice(uppercase))
    elif brakujace == 1:
        wszystkie_znaki += ''.join(random.choice(lowercase))
    
 
#haslo = random.shuffle(wszystkie_znaki)
haslo = ''.join(secrets.choice(wszystkie_znaki) for i in range(n_znakow))
print('Oto Twoje hasło:', haslo, '\nHasło jest długie na', len(haslo), 'znaków')