import argparse
from exercise_2a.greeting_message import UserInfo, greet_user, write_text

def user_greeting():

    # Create ArgumentParser object.
    parser= argparse.ArgumentParser(description= 'Get user info and greet user')
    parser.add_argument('--name', type= str, default= 'Yania', help= 'user name')
    parser.add_argument('--age', type= int, default= 30, help= 'age of the user')    
    parser.add_argument('--filepath', default= 'exercise_2a/output.txt', help= 'destination file path')
    args= parser.parse_args()

    # Create user object.
    user= UserInfo(args.name, args.age) 

    # Greet user with a message.
    greeting= greet_user(user)
    
    # Store the greeting message in a file.
    file_path= args.filepath
    write_text(greeting, file_path)

    # Display the greeting message.
    print(greeting)


def main():
    user_greeting()


if __name__== "__main__":
    main()  