from fonctionsutils import *


# générer une paire de clés public/privée (plus le nombre mit dans la fonction
# pour générer un entier preier est gand plus l clé sera fiable mais plus le prog
# prendra du temps a la générer)
def cle_privee(e, m):
    li = []
    for i in range(11, m):
        d = (1 + i * m) / e
        if (d.is_integer()):
            li.append(d)
    a = randint(0, len(li) - 1)
    return li[a]


def cle_RSA():
    p = generate_prime(8)
    q = generate_prime(8)
    n = p * q
    m = (p - 1) * (q - 1)
    e = find_e(m)

    d = cle_privee(e, m)
    return e, int(d), n

def chiffrement(message,e,n):
    suiteEntiers=StringToint(message)

    sortie=[]
    for i in range(0,len(suiteEntiers)):
        sortie.append(AlgorithmeRapide(suiteEntiers[i],e,n))

    return sortie

def dechiffrement(chiffre,d,n):

    message=[]
    for i in range(0,len(chiffre)):
        message.append(AlgorithmeRapide(chiffre[i],d,n))

    return message

if __name__ == '__main__':
    C = cle_RSA()
    print("cle public", C[0], C[2])
    print("cle privée", int(C[1]), C[2])
    val = input("Enter votre message a chiffrer: ")
    print(val ," ==> ",StringToint(val)," en claire")
    chiffre=chiffrement(val,C[0], C[2])
    print(val, " ==> ", chiffre, " en chiffre")
    print("dechiffrement ...")
    clair=dechiffrement(chiffre, C[1], C[2])
    print(clair ,"====> ",intToString(clair))


