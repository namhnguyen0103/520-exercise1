def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
    
    # 1. Check the minimum length condition
    if len(s) < 3:
        return False
        
    # 2. Iterate through all three-character windows
    # We iterate up to len(s) - 3 because the indices are i, i+1, i+2
    for i in range(len(s) - 2):
        # The three consecutive characters are s[i], s[i+1], s[i+2]
        char1 = s[i]
        char2 = s[i+1]
        char3 = s[i+2]
        
        # Check if they are NOT distinct (i.e., any two are equal)
        if char1 == char2 or char1 == char3 or char2 == char3:
            # Found a case where 3 consecutive letters are NOT distinct, so the string is NOT happy
            return False
            
    # 3. If the loop completes without returning False, the string is happy
    return True