from exercise_1a.write_function import write_fn
from exercise_1a.greet_function import greet_fn
from exercise_2b import model_ selection as model
from exercise_2b import model_evaluation as evaluate
from exercise_2b import split_dataset
import pandas as pd

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
         

    def greet_user(self) -> str:
        '''Greets the user with a message.
        
        Args: 
            user (UserInfo): User information.
        
        Returns:
            str: A greeting string.
        '''
        greeting= greet_fn(self.name, self.age)
        return greeting
        

    def write_text(greeting: str ,file_path: str) -> None:
        '''
        Stores the greeting string into a file. 

        Args: 
            greeting (str): The greeting string
            file_path (str): destination where output will be stored
        '''
        write_fn(greeting,file_path)


class ModelObject:
    '''
    Docstring for ModelObject
    '''
    def __init__(self, model_lr: model, X_train, X_test, y_train, y_test):
        self.model = model_lr
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test

    def call_model(self):
        '''Train the model'''
        model.fit(self.X_train, self.y_train)

    def call_predict(self):
        '''Make prediction'''
        y_pred = model.predict(self.X_test)
        return y_pred
    
    def call_evaluate(self, y_pred):
        '''Evaluate the model'''
        mse,r2 = evaluate(self.y_test, y_pred)
        return mse, r2


def welcome_user() -> None:
    # Create user object.
    user= UserInfo('Millie', 22)

    # Greet the user.
    greeting= UserInfo.greet_user(user)

    # Store the greeting message.
    file_path= 'exercise_2a/test.txt'
    UserInfo.write_text(greeting, file_path)
    
    # Display the greeting message.
    return print(greeting)

def predictive_model():

    '''Load dataset'''
    file_path = 'exercise_2b\dataset.csv'
    data = pd.read_excel(file_path)
    df = pd.DataFrame(data)

    '''Identify the features (X) and target (y)'''
    X = df[['beds', 'baths', 'size', 'zip_code']]
    y = df['price']

    '''split the dataset into train and test set in a ratio of 80/20'''
    X_train, X_test, y_train, y_test = split_dataset(X, y)

    ModelObject.__init__(model, X_train, X_test, y_train, y_test)
    ModelObject.call_model()
    y_pred = ModelObject.call_predict(X_test)
    mse_value, r2_value = ModelObject.call_evaluate(y_pred)
predictive_model()


def main():
    welcome_user()
    X_new = [3, 1, 98106, 915000.0]
    result= ModelObject.call_predict(X_new)
    print(f'X: {X_new} /n predicted price: {result.y_pred} /n mse: {result.mse_value}, /n r2 score: {result.r2_value}') 
    

if __name__== '__main__':
    
    main()