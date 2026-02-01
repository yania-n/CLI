import argparse
from exercise_2a.greet_objects import UserInfo, greet_user, write_text

def get_parser():
    # Create ArgumentParser object.
    parser= argparse.ArgumentParser(description= 'Get user info and greet user', add_help = False)
    parser.add_argument('--name', type= str, default= 'Yania', help= 'user name')
    parser.add_argument('--age', type= int, default= 30, help= 'age of the user')    
    parser.add_argument('--filepath', default= 'exercise_2a/output.txt', help= 'destination file path')
    return parser

def user_greeting(args):

    # Create user object.
    user= UserInfo(args.name, args.age) 

    # Greet user with a message.
    greeting= greet_user(user)

    # Display the greeting message.
    print(greeting)

    return greeting

if __name__== "__main__":
    standalone_parser = argparse.ArgumentParser(parents = [get_parser()])
    args = standalone_parser.parse_args()
    greeting = user_greeting(args)
    
    # Store the greeting message in a file.
    file_path= args.filepath
    write_text(greeting, file_path)