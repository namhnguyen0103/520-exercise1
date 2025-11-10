def encode_shift(s: str):
    """
    Returns encoded string by shifting every lowercase character by 5 in the alphabet.
    
    The encoding process:
    1. Get the ASCII value of the character (ord(ch)).
    2. Subtract ord('a') to get a 0-indexed position (0-25).
    3. Add 5 for the forward shift.
    4. Apply modulo 26 for wrap-around (z -> e).
    5. Add ord('a') back to convert the position back to the character's ASCII code.
    """
    # Note: This implementation assumes the input 's' contains only lowercase 'a'-'z'.
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    Takes as input a string encoded with the encode_shift function (a +5 Caesar cipher). 
    Returns the original decoded string by applying an inverse -5 shift.
    
    The decoding process applies the inverse modular arithmetic:
    1. Convert the character to its 0-indexed position (ord(ch) - ord('a')).
    2. Subtract the shift amount (5).
    3. Apply modulo 26 to ensure proper wrap-around for negative results 
       (e.g., 'e' -> 'z' is handled by -1 % 26 == 25 in Python).
    4. Add ord('a') back to get the ASCII value of the original character.
    5. Convert the ASCII value back to a character (chr()).
    """
    
    # We use a list comprehension for efficient, one-line iteration and transformation.
    return "".join([
        chr(((ord(ch) - ord("a") - 5) % 26) + ord("a")) 
        for ch in s
    ])
