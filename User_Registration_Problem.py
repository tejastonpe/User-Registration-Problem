import re
import logging 

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',filename="user_registration.log",level=logging.INFO)

def first_name(inp):
    '''
    Description : Validate the input string as a first name.
    Args    : inp (str)-input string to be validated.
    Returns : bool: True if the input string is a valid first name else False.
    '''
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.match(pattern,inp):
        return True
    else:
        return False

def main():
    """
    Main function to get user input 
    returns : None.
    """
    try:
        inp=input("Enter your first name: ")
        print(first_name(inp))
    except Exception as e:
        logger.error("Error occourd: %s",e)


if __name__=="__main__":
    main()