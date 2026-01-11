from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

model = LinearRegression()

class ModelObject:

    def __init__(self):
        pass

    def call_model(X_train, y_train):
        '''Train the model'''
        model.fit(X_train, y_train)

    def call_predict(X_test):
        '''Make prediction'''
        y_pred = model.predict(X_test)

        return y_pred

    def train_model(self, X_train, X_test, y_train):
        self.call_model(X_train, y_train)
        y_pred = self.call_predict(X_test)
        
        return y_pred

    def evaluate(y_test, y_pred):
        # Evaluate the model
        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)

        return mse, r2