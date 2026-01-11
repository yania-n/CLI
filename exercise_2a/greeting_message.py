from exercise_1a.write_function import write_fn
from exercise_1a.greet_function import greet_fn

class UserInfo:
    '''
    Add user info.
    
    Attributes: 
        name (str): user's name 
        age (int): user's age in years

    '''

    def __init__(self, name: str, age: int):
        
        if age < 0:
            raise ValueError('Age must be non-negative')
    
        self.name= name
        self.age= age
         

def greet_user(user: UserInfo) -> str:
    '''Greets the user with a message.
    
    Args: 
        user (UserInfo): User information.
    
    Returns:
        str: A greeting string.
    '''
    greeting= greet_fn(user.name, user.age)
    return greeting
    

def write_text(greeting: str ,file_path: str) -> None:
    '''
    Stores the greeting string into a file. 

    Args: 
        greeting (str): The greeting string
        file_path (str): destination where output will be stored
    '''
    write_fn(greeting,file_path)


def main() -> None:
    # Create user object.
    user= UserInfo('Millie', 22)

    # Greet the user.
    greeting= greet_user(user)

    # Store the greeting message.
    file_path= 'exercise_2a/test.txt'
    write_text(greeting, file_path)
    
    # Display the greeting message.
    print(greeting)

if __name__== '__main__':
    main()