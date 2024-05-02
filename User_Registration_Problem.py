import re
import logging 

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',filename="user_registration.log",level=logging.INFO)

def first_name(f_name):
    '''
    Description : Validate the input string as a first name.
    Args    : first_name (str)-input string to be validated.
    Returns : bool: True if the input string is a valid first name else False.
    '''
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.match(pattern, f_name):
        return True
    else:
        return False

def last_name(l_name):
    '''
    Description : Validate the input string as a last name.
    Args    : last_name(str)-input string to be validated.
    Returns : bool: True if the input string is a valid first name else False.
    '''
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.match(pattern,l_name):
        return True
    else:
        return False

def main():
    """
    Main function to get user input 
    returns : None.
    """
    try:
        f_name=input("Enter your first name: ")
        l_name=input("Enter your last name: ")
        print(first_name(f_name))
        print(last_name(l_name))
    except Exception as e:
        logger.error("Error occourd: %s",e)


if __name__=="__main__":
    main()