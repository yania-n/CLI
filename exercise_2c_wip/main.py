import argparse
from multiple_class_objects import UserInfo,  ModelObject


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
    greeting= UserInfo.greet_user(user)
    
    # Store the greeting message in a file.
    file_path= args.filepath
    UserInfo.write_text(greeting, file_path)

    # Display the greeting message.
    print(greeting)



def prediction_model():

    # Create ArgumentParser object.
    model_parser= argparse.ArgumentParser(description= 'Predict with linear regression model')
    model_parser.add_argument('-beds', type= int, help= 'Total number of beds')
    model_parser.add_argument('-baths', type= int, help= 'Total number of bathrooms')
    model_parser.add_argument('-size', type= float, help= 'Size of the house floor in square feet')
    model_parser.add_argument('-zip_code', type= str, help= 'The zip code of the location')
    model_args= model_parser.parse_args()

    # Initialize feature values.
    X_new = [model_args.beds, model_args.baths, model_args.size, model_args.zip_code]

    # Make prediction.
    predicted_price= ModelObject.call_predict(X_new)
    
    # Display the prediction
    print(f' X: {X_new}, /n predicted price: {predicted_price}')


def main():

    user_input = input("Enter 'a' to receive a greeting message or 'b' to use the predictive model")
    
    if user_input == 'a':
        print("Run the main.py file with your name and age")
        user_greeting()

    elif user_input== 'b':
        print("Run the main.py file with these values: number of beds available, number of bathrooms, floor size of the house, and zip code of your area")
        prediction_model()


if __name__== "__main__":
    main()