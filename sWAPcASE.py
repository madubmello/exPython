novaFrase = []

def swap_case(s):
    for i in s:
        if i.isupper() is True:
            novaFrase.append(str(i.lower()))
        else:
            novaFrase.append(str(i.upper()))
    frasePronta = "".join(novaFrase)
    return frasePronta

s = input()
result = swap_case(s)
print(result)
