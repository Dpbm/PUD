def odd(final_number=5, round='previous'):
    """
        ODD FUNCTION
        
        RETURN
            list of odd numbers

        ARGUMENTS
            
            final_number --> last number of range
            
            round        --> put the next or previous number case final_number is and even number 
                default  --> 'previous'
                possibilities --> 'previous', 'next' 
    """
    round_type = {
        'previous':1,
        'next': 2
    }

    return list(range(1, final_number + round_type[round], 2))