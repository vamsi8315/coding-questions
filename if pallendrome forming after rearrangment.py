NO_OF_CHARS=256
def canFormPalindrome(st) : 
  
    # Create a count array and initialize   
    # all values as 0 
    count = [0] * (NO_OF_CHARS) 
  
    # For each character in input strings, 
    # increment count in the corresponding 
    # count array 
    for i in range( 0, len(st)) : 
        count[ord(st[i])] = count[ord(st[i])] + 1
  
    # Count odd occurring characters 
    odd = 0
      
    for i in range(0, NO_OF_CHARS ) : 
        if (count[i] & 1) : 
            odd = odd + 1
  
        if (odd > 1) : 
            return False
              
    # Return true if odd count is 0 or 1,  
    return True
