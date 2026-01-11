import pandas as pd
from exercise_2b.split_dataset import split_dataset
from exercise_2b.model_initialization import ModelObject
from exercise_1a.write_function import write_fn

# Load dataset
data = pd.read_csv('exercise_2b\dataset.csv')
df = pd.DataFrame(data)

# Identify the features (X) and target (y)  
X = df[['beds', 'baths', 'size', 'zip_code']]
y = df['price']


X_train, X_test, y_train, y_test = split_dataset(X, y)

if __name__ == '__main__':
    y_pred = ModelObject.train_model(ModelObject, X_train, X_test, y_train)
    mse, r2 = ModelObject.evaluate(y_test, y_pred)

    # Display result
    df = X_test
    df['Actual'] = y_test
    df['Predicted'] = y_pred
    print(f' RESULT:')
    print(f'{df}')
    print(f'Mean square error: {mse}')
    print(f'R-squared Score: {r2}')

    # Write result to a file
    output = f'Mean square error: {mse}, R-squared Score: {r2}'
    write_fn(output, 'exercise_2b/model_output_test.txt')
