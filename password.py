import random
def shuffle(string):
    ls=list(string)
    random.shuffle(ls)
    return ''.join(ls)
uppercaseletter1=chr(random.randint(65,90))
uppercaseletter2=chr(random.randint(65,90))
lowercaseletter1=chr(random.randint(97, 122))
lowercaseletter2=chr(random.randint(97, 122))
number=chr(random.randint(48,57))
password=uppercaseletter1+uppercaseletter2+lowercaseletter1+lowercaseletter2+number
password=shuffle(password)
print(password)

