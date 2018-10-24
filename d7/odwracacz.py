
def odwroc_zdanie(zdanie):
    return zdanie[::-1]

def test():
    print(odwroc_zdanie('ala ma kota'))
    print(odwroc_zdanie('kajak'))

#dodatkowy if na koncu plików, służący do testów.
if __name__ == '__main__':
    test()