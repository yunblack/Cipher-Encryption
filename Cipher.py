# name: Juyoung Daniel Yun
# email: juyoung.yun@stonybrook.edu
# id: 112368205

def encrypt(value, dict):
    str=''
    for i in range(0,value.__len__()):
        str+=dict[value[i]]
    return str

def encryptCase(value,dict):
    str=''
    for i in range(0,value.__len__()):
        if value[i].lower() in dict:
            if value[i].islower():
                str+=encrypt(value[i],dict)
            elif value[i].isupper():
                str+=(encrypt(value[i].lower(),dict)).upper()
        else:
            str+=value[i]
    return str

def crypto_quote(value,dict):
    str=''
    f = open(value,'r')
    while True:
        line = f.readline()
        str+=encryptCase(line,dict)
        if not line: break
    f.close()
    return str

def main():

    cipher={'a':'d',
            'b':'e',
            'c':'f',
            'd':'g',
            'e':'h',
            'f':'i',
            'g':'j',
            'h':'k',
            'i':'l',
            'j':'m',
            'k':'n',
            'l':'o',
            'm':'p',
            'n':'q',
            'o':'r',
            'p':'s',
            'q':'t',
            'r':'u',
            's':'v',
            't':'w',
            'u':'x',
            'v':'y',
            'w':'z',
            'x':'a',
            'y':'b',
            'z':'c'}

    print(encrypt('abba',cipher))
    print(encryptCase('Et tu, Brute?',cipher))
    print(crypto_quote("./data/quote1.txt",cipher))

if __name__ == '__main__':
    main()