def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    takes as input string encoded with encode_shift function. Returns decoded string.
    """
    # The encoding is a +5 shift (Caesar cipher). To decode, we apply a -5 shift.
    # The logic is:
    # 1. Convert the encoded character's ASCII value (ord(ch)) to its 0-indexed alphabet position
    #    relative to 'a': ord(ch) - ord("a").
    # 2. Subtract the shift value (5) to reverse the encoding.
    # 3. Apply the modulo 26 to handle wrap-around (e.g., 'a' - 5 = 'v').
    # 4. Add ord("a") back to get the ASCII value of the decoded character.
    # 5. Convert the ASCII value back to a character (chr).
    return "".join([chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) for ch in s])