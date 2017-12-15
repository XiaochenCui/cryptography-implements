from helper import swap


def KSA(key):
    """
    Key-scheduling algorithm (KSA)

    :param key:
    :type key: string
    """
    keylength = len(key)

    S = list(range(256))
    j = 0
    for i in range(256):
        j = (j + S[i] + key[i % keylength]) % 256
        swap(S, i, j)
    return S


def PRGA(S):
    """
    Pseudo-random generation algorithm (PRGA)

    :param S:
    :type S: list
    """
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        swap(S, i, j)
        K = S[(S[i] + S[j]) % 256]
        yield K


def RC4(key):
    """
    Rivest Cipher 4
    """
    S = KSA(key)
    return PRGA(S)


def main():
    # ciphertext should be 45A01F645FC35B383552544B9BF5
    key = "Secret"
    plaintext = "Attack at dawn"

    keystream = RC4(bytearray(key, 'utf-8'))
    for c in plaintext:
        print('{:02X}'.format(ord(c) ^ next(keystream)), end='')
    print()


if __name__ == "__main__":
    main()
