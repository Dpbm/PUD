def even(final_number=6, round='previous', jump_zero=False):
    """
        EVEN FUNCTION
        
        RETURN
            list of even numbers

        ARGUMENTS
            
            final_number --> last number of range
                default  --> 6
            
            round        --> put the next or previous number case final_number is and odd number 
                default  --> 'previous'
                possibilities --> 'previous', 'next' 

                examples 
                    next
                        final_number = 5
                        return = [0, 2, 4, 6]
                    
                    previous
                        final_number = 5
                        return = [0, 2, 4]
            
            jump_zero   --> remove zero from the return if is True
                default --> False
    """
    
    round_type = {
        'previous':1,
        'next': 2
    }

    returnable = list(range(0, final_number + round_type[round], 2))

    if jump_zero:
        returnable.remove(0)

    return returnable