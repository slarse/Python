def rabin_karp(pattern, text):
    """

    The Rabin-Karp Algorithm for finding a pattern within a piece of text
    with complexity O(nm), most efficient when it is used with multiple patterns
    as it is able to check if any of a set of patterns match a section of text in o(1) given the precomputed hashes.

    This will be the simple version which only assumes one pattern is being searched for but it's not hard to modify

    1) Calculate pattern hash

    2) Step through the text one character at a time passing a window with the same length as the pattern
        calculating the hash of the text within the window compare it with the hash of the pattern. Only testing
        equality if the hashes match

    """
    p_len = len(pattern)
    p_hash = hash(pattern)

    for i in range(0, len(text) - (p_len - 1)):

        # written like this t
        text_hash = hash(text[i:i + p_len])
        if text_hash == p_hash and \
                text[i:i + p_len] == pattern:
            return True
    return False