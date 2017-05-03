def get_alphabet():
    """
    This function returns the alphabet in a list
    :return: list
    """
    alphabet = [chr(97+a) for a in range(26)]

    return alphabet


def cypher_alphabet(key="money"):
    """
    Creates the cypher alphabet with the key provided
    :param key: string
    :return: dictionary
    """
    alphabet = get_alphabet()

    cypher = list(key) + [a for a in alphabet if a not in key]

    cypher_d = {a: c for a, c in zip(alphabet, cypher)}

    return cypher_d


def encrypt(msg, key="money"):
    """
    Encrypts the input msg using the key provided
    :param msg: string
    :param key: string
    :return encrypted_msg: string
    """
    # Cypher the alphabet
    cypher = cypher_alphabet(key)

    encrypted_msg = ""
    for s in msg:
        encrypted_msg += cypher.get(s, s)

    return encrypted_msg


def decrypt(encrypted_msg, key="money"):
    """
    Decrypts the input msg with the key provided
    :param encrypted_msg: string
    :param key: string
    :return msg: string
    """
    # Cypher the alphabet
    cypher = cypher_alphabet(key)
    reversed_cypher = {v: k for k, v in cypher.items()}

    msg = ""
    for s in encrypted_msg:
        msg += reversed_cypher.get(s, s)

    return msg



