def decode_shift(s: str):
    """
    Takes a string encoded with encode_shift (lowercase a-z) and returns the decoded string.
    """
    return "".join(chr(((ord(ch) - 5 - ord("a")) % 26) + ord("a")) for ch in s)
