from random import randint

def AlgorithmeRapide(x, y, n):
    """puissance modulaire: (x**y)%n avec x, y et n entiers"""
    result = 1
    while y>0:
        if y&1>0:
            result = (result*x)%n
        y >>= 1
        x = (x*x)%n
    return result


# fonction pour calculer le pgcd de deux nombre
def pgcd(a, b):
    if b == 0:
        return a
    else:
        r = a % b
        return pgcd(b, r)


def is_prime(num, test_count):
    if num == 1:
        return False
    if test_count >= num:
        test_count = num - 1
    for x in range(test_count):
        val = randint(1, num - 1)
        if pow(val, num - 1, num) != 1:
            return False
    return True



def find_e(m):
    l = []
    for i in range(11, m):
        if pgcd(i, m) == 1:
            l.append(i)
    p = randint(0, len(l) - 1)
    return l[p]





# fonction pour generer un nombre premier aléatoire
def generate_prime(n):
    found_prime = False
    while not found_prime:
        p = randint(2 ** (n - 1), 2 ** n)
        if is_prime(p, 1000):
            return p

def get_int_from_alphabet(lettre):
    switcher = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7,
        'i': 8,
        'j': 9,
        'k': 10,
        'l': 11,
        'm': 12,
        'n': 13,
        'o': 14,
        'p': 15,
        'q': 16,
        'r': 17,
        's': 18,
        't': 19,
        'u': 20,
        'v': 21,
        'w': 22,
        'x': 23,
        'y': 24,
        'z': 25,
    }
    return switcher.__getitem__(lettre)

def get_alphabet_from_int(entier):
    switcher = {
        0:'a',
        1: 'b',
        2: 'c',
        3: 'd',
        4: 'e',
        5: 'f',
        6: 'g',
        7: 'h',
        8: 'i',
        9: 'j',
        10: 'k',
        11: 'l',
        12: 'm',
        13: 'n',
        14: 'o',
        15: 'p',
        16: 'q',
        17: 'r',
        18: 's',
        19: 't',
        20: 'u',
        21: 'v',
        22: 'w',
        23: 'x',
        24: 'y',
        25: 'z',


    }
    return switcher.__getitem__(entier)



#transformer les lettres du messages en des entiers afin de pouvoir faire le traitement RSA
def StringToint(message):
    message = message.lower()
    message = message.replace(" ", "")
    chiffres=[]
    for i in range(0,len(message)):
        m=get_int_from_alphabet(message[i] )
        chiffres.append(m)
    return chiffres

#repasser a un message compréhensible  a savoir des lettres
def intToString(entier):

    message=[]
    for i in range(0,len(entier)):
        m=get_alphabet_from_int(entier[i] )
        message.append(m)
    return message
