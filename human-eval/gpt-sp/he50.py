def decode_shift(s: str) -> str:
    """
    Takes as input a string encoded with `encode_shift` and returns the decoded string.
    This function reverses the Caesar cipher with a shift of +5 applied in `encode_shift`.

    Each lowercase letter ('a' to 'z') is shifted backward by 5 positions in the alphabet,
    wrapping around from 'a' back to 'z' as needed. Non-lowercase characters are preserved
    unchanged for safety and readability.

    Example:
    >>> encode_shift("hello")
    'mjqqt'
    >>> decode_shift("mjqqt")
    'hello'
    >>> decode_shift(encode_shift("abc xyz!"))
    'abc xyz!'
    >>> decode_shift("")
    ''
    """

    # --- Step 1: Input validation ---
    if not isinstance(s, str):
        raise TypeError("Input must be a string.")

    # --- Step 2: Initialize output list ---
    decoded_chars = []

    # --- Step 3: Iterate through each character ---
    for ch in s:
        # Check if character is lowercase alphabetic
        if 'a' <= ch <= 'z':
            # Convert to index 0–25
            index = ord(ch) - ord('a')

            # Shift backward by 5, with modulo 26 to wrap around
            new_index = (index - 5) % 26

            # Convert back to character
            decoded_char = chr(new_index + ord('a'))
            decoded_chars.append(decoded_char)
        else:
            # Leave non-lowercase characters unchanged
            decoded_chars.append(ch)

    # --- Step 4: Combine list of characters into final string ---
    return "".join(decoded_chars)
