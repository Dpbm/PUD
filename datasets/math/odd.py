def odd(final_number=5, round='previous'):
    """
        Odd FUNCTION
        
        RETURN
            list of odd numbers

        ARGUMENTS
            
            final_number --> last number of range
                default  --> 5
            
            round        --> put the next or previous number case final_number is and even number 
                default  --> 'previous'
                possibilities --> 'previous', 'next' 

                examples 
                    next
                        final_number = 6
                        return = [1, 3, 5, 7]
                    
                    previous
                        final_number = 6
                        return = [1, 3, 5]
    """
    round_type = {
        'previous':1,
        'next': 2
    }

    return list(range(1, final_number + round_type[round], 2))