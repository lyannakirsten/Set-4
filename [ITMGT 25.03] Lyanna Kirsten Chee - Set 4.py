def bin_to_dec(binary_string):
    '''
    Convert a binary string to its base-10 integer representation.
    
    Example:
    bin_to_dec("101") -> 5
    bin_to_dec("1010") -> 10
    bin_to_dec("11111111") -> 255
    bin_to_dec("0") -> 0
    bin_to_dec("1") -> 1
    
    Parameters
    ----------
    binary_str: str
        The binary string to be converted to a base-10 integer.
        The string should contain only the characters '0' and '1'.
    
    Returns
    -------
    int
        The base-10 integer representation of the input binary string.
    
    Notes
    -----
    Binary is a base-2 number system that uses only two digits: 0 and 1. 
    Each digit in a binary number is called a "bit". The position of each bit 
    represents a power of 2, starting from the rightmost bit (2^0), the next bit 
    to the left (2^1), and so on. To understand a binary number, convert it to 
    decimal by summing the products of each bit and its corresponding power of 2.
    
    For example, the binary string "1011" is calculated as:
    (1 * 2^3) + (0 * 2^2) + (1 * 2^1) + (1 * 2^0)
    = 8 + 0 + 2 + 1 = 11
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    bin_to_dec = 0
    length = len(binary_string)
    
    for i in range(length):
        bit = binary_string[length-1-i]
        bit_value = int(bit)
        power_of_two = 2**i
        bin_to_dec += bit_value*power_of_two
    
    return bin_to_dec


def dec_to_bin(number):
    '''
    Convert a base-10 number to its binary string representation.
    
    Example:
    dec_to_bin(5) -> "101"
    dec_to_bin(10) -> "1010"
    dec_to_bin(255) -> "11111111"
    dec_to_bin(0) -> "0"
    dec_to_bin(1) -> "1"
    
    Binary is a base-2 number system that uses only two digits: 0 and 1. 
    Each digit in a binary number is called a "bit". The position of each bit 
    represents a power of 2, starting from the rightmost bit (2^0), the next bit 
    to the left (2^1), and so on. To understand a binary number, convert it to 
    decimal by summing the products of each bit and its corresponding power of 2.
    
    Parameters
    ----------
    number: int
        The base-10 integer to be converted to a binary string.
        The number should be a non-negative integer.
    
    Returns
    -------
    str
        The binary string representation of the input base-10 number.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    if number == 0:
        return "0"
    
    dec_to_bin = ""
    
    while number > 0:
        remainder = number%2
        dec_to_bin = str(remainder)+dec_to_bin
        number = number//2
    
    return dec_to_bin


def telephone_cipher(message):
    '''
    Before, when phones did not have touchscreen keypads, 
    the way to input letters was to click the physical keypads 
    repeatedly.
    
    For example:
    Clicking "222" will result in the letter C. 
    Clicking "7777" will result in the letter S. 
    and so on
    
    To read more about it, you may visit the following link:
    Telephone Keypad: https://en.wikipedia.org/wiki/Keypad
    
    Using the `encoder_dict` in "set_4_given.py",
    your task is to convert a letter string into its equivalent
    numerical string as typed in a Telephone Keypad.
    
    Note: In the case of text inputs like "ABC", to demarcate the
    same letters, an underscore "_" is placed in between.
    
    Examples:
    telephone_cipher("ABC") -> "2_22_222"
    telephone_cipher("HELLO WORLD") -> "4433555_555666096667775553"
    telephone_cipher("TEST") -> "83377778"
    telephone_cipher("HOW DO YOU DO") -> "4466690366609996668803666"
    telephone_cipher("ABRACADABRA") -> "2_227772_222_232_227772"
    
    Parameters
    ----------
    message: str
        the text string consisting of capital letters
    
    Returns
    -------
    str
        the equivalent numerical string typed in a Telephone Keypad
        with underscores demarcating characters who share the same key
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    encoder_dict = {
        " ":"0",
        "A":"2",
        "B":"22",
        "C":"222",
        "D":"3",
        "E":"33",
        "F":"333",
        "G":"4",
        "H":"44",
        "I":"444",
        "J":"5",
        "K":"55",
        "L":"555",
        "M":"6",
        "N":"66",
        "O":"666",
        "P":"7",
        "Q":"77",
        "R":"777",
        "S":"7777",
        "T":"8",
        "U":"88",
        "V":"888",
        "W":"9",
        "X":"99",
        "Y":"999",
        "Z":"9999"
    }
    
    telephone_cipher = []
    
    for i, char in enumerate(message):
        current_num_str = encoder_dict[char]
        
        if i > 0 and encoder_dict[message[i-1]][0] == current_num_str[0]:
            telephone_cipher.append('_')
        
        telephone_cipher.append(current_num_str)
    
    return ''.join(telephone_cipher)


def telephone_decipher(message):
    '''
    Using the `decipher_dict` in "set_4_given.py",
    decrypt a message that was originally typed using the Telephone Keypad
    as done in the `telephone_cipher` function above.
    
    Example:
    telephone_decipher("2_22_222") -> "ABC"
    telephone_decipher("4433555_555666096667775553") -> "HELLO WORLD"
    telephone_decipher("83377778") -> "TEST"
    telephone_decipher("4466690366609996668803666") -> "HOW DO YOU DO"
    telephone_decipher("2_227772_222_232_227772") -> "ABRACADABRA"
    
    Parameters
    ----------
    message: str
        the numerical string typed in a Telephone Keypad
        with underscores demarcating characters who share the same key
    
    Returns
    -------
    str
        the equivalent text string consisting of capital letters
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    decipher_dict = {
        "0": " ",
        '2': 'A',
        '22': 'B',
        '222': 'C',
        '3': 'D',
        '33': 'E',
        '333': 'F',
        '4': 'G',
        '44': 'H',
        '444': 'I',
        '5': 'J',
        '55': 'K',
        '555': 'L',
        '6': 'M',
        '66': 'N',
        '666': 'O',
        '7': 'P',
        '77': 'Q',
        '777': 'R',
        '7777': 'S',
        '8': 'T',
        '88': 'U',
        '888': 'V',
        '9': 'W',
        '99': 'X',
        '999': 'Y',
        '9999': 'Z'
    }

    telephone_decipher = []
    i = 0
    
    while i < len(message):
        if message[i] == '_':
            i += 1
            continue
            
        j = i
        
        while j < len(message) and message[j] == message[i]:
            j += 1
        
        current_letter_str = message[i:j]
        telephone_decipher.append(decipher_dict[current_letter_str])
        
        i = j
    
    return ''.join(telephone_decipher)