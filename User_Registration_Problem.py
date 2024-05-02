import re
import logging 

logger=logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(message)s',filename="user_registration.log",level=logging.INFO)

def validate_first_name(first_name):
    '''
    Description : Validate the input string as a first name.
    Parameter   : first_name (str)-input string to be validated.
    Returns     : bool- True if the input string is a valid first name else False.
    '''
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.match(pattern, first_name):
        return True
    else:
        return False

def validate_last_name(last_name):
    '''
    Description : Validate the input string as a last name.
    Parameter   : last_name(str)-input string to be validated.
    Returns     : bool- True if the input string is a valid first name else False.
    '''
    pattern = r'^[A-Z][a-z]{2,}$'
    if re.match(pattern,last_name):
        return True
    else:
        return False

def validate_email(email_address):
    '''
    Description : Validate the input string as a email.
    Parameter   : inp_email - input to be validated.
    Returns     : bool- True if the input string is a valid email address else False.
    '''
    pattern = r'^\w+\.+\w+@\w+\.+\w+$'
    if re.match(pattern,email_address):
        return True
    else:
        return False

def main():
    """
    Main function to get user input 
    returns : None
    """
    try:
        first_name=input("Enter your first name: ")
        last_name=input("Enter your last name: ")
        email_address=input("Enter your email: ")
        print(validate_first_name(first_name))
        print(validate_last_name(last_name))
        print(validate_email(email_address))
    except Exception as e:
        logger.error("Error occourd: %s",e)


if __name__=="__main__":
    main()