def CaesarCipherChar(c, k):
    if ord(c.lower()) + k > ord('z'):
        if c.isupper():
            return  chr(ord(c.lower()) + k - ord('z')-1 + ord('A') )
        else:
            return  chr(ord(c.lower()) + k - ord('z')-1 + ord('a') )
    else:
        return  chr(ord(c) + k)
def CaesarCipher(s, k):
    l = ''
    for i in s:
        if i.isalpha():
            l += CaesarCipherChar(i, k)
        else:
            l += i
    return  l
print(CaesarCipher('SDfdfdyz./', 2))