from string import ascii_letters, ascii_lowercase, ascii_uppercase

def letters(type="all", start=0, end=(26+26)):
    """
        LETTERS FUNCTION
        
        RETURN
            A string with letters

        ARGUMENTS
            
            type --> type of return
                default  --> all

                possibilities
                    all       --> all letters in uppercase and lowercase
                    uppercase --> all letters in uppercase
                    lowercase --> all letters in lowercase
            
            start        --> the first letter to be returned
                default  --> 0
                possibilities --> 0 .. (end - 1)

            end          --> the last letter to be returned
                default  --> 52
                
                possibilities
                    (start + 1) .. 52 --> to all
                    (start + 1) .. 26 --> to uppercase and lowercase
    """

    if start < 0 or (end > (26 + 26) and type != "all")  or (end > (26 + 26) and type == "all") or end < 0 or (end > 26 and type != "all") or start > end or start == end:
        raise "start or end argument invalid"

    returnable = ascii_letters

    if type == "uppercase":
        returnable = ascii_uppercase
    elif type == "lowercase":
        returnable = ascii_lowercase
    
    return returnable[start:end]