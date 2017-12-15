def key_scheduler(keylength=128):
    """
    Key-scheduling algorithm (KSA)

    :param keylength: the number of bytes in the key and can be in the range
        1 <= keylength <= 256
    :type keylength: int
    """
    if not (keylength >= 1 and keylength <= 256):
        return

    S = [i for i in range(keylength)]


class KeyLengthInvalid(Exception):

    def __init__(self, message=None):
        if not message:
            self.message = "keylength must between 1 and 256"
