import pandas as pd
from exercise_2b.split_dataset import split_dataset
from exercise_2b.model_initialization import ModelObject

# Load dataset
data = pd.read_csv('exercise_2b\dataset.csv')
df = pd.DataFrame(data)

# Identify the features (X) and target (y)  
X = df[['beds', 'baths', 'size', 'zip_code']]
y = df['price']

X_train, X_test, y_train, y_test = split_dataset(X, y)

ModelObject.model_fit(X_train, y_train)
y_pred = ModelObject.call_predict(X_test)
mse, r2 = ModelObject.evaluate(y_test, y_pred)

def main():
    # Display result
    df = X_test
    df['Actual'] = y_test
    df['Predicted'] = y_pred
    print(f' RESULT:')
    print(f'\n{df}')
    print(f'Mean square error: {mse}')
    print(f'R-squared Score: {r2}')
    
if __name__ == '__main__':
    main()