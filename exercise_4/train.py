import exercise_4.utils as utils
from exercise_4.config import ModelObjects
from sklearn.model_selection import train_test_split
from sklearn.datasets import fetch_lfw_people
import joblib

faces = fetch_lfw_people(min_faces_per_person = 60)
joblib.dump(faces.target_names, 'exercise_4/target_names.pkl')

Xtrain, Xtest, ytrain, ytest = train_test_split(faces.data, faces.target, random_state=42)

def best_model_fn(model, param_grid, Xtrain, ytrain):

    best_model = utils.grid_search(model, param_grid, Xtrain, ytrain)
    return best_model

def select_model(model_name, Xtrain, ytrain):
    
    Models = ModelObjects()

    if model_name =='RandomForest':

        model = Models.rf_model
        param_grid = Models.rf_param_grid
        best_rf_model = best_model_fn(model, param_grid, Xtrain, ytrain)
        joblib.dump(best_rf_model, 'exercise_4/best_rf_model.pkl')
        print('Model saved successfully')
        return best_rf_model

    elif model_name == 'SVC':

        model = Models.svc_model
        param_grid = Models.svc_param_grid
        best_svc_model = best_model_fn(model, param_grid, Xtrain, ytrain)
        joblib.dump(best_svc_model, 'exercise_4/best_svc_model.pkl')
        print('Model saved successfully')
        return best_svc_model

def evaluate_model(Xtest, ytest, yfit, target_names, model_name):
    report = utils.classification_report_fn(ytest, yfit, target_names)
    confusion_mat = utils.plot_confusion_matrix(ytest, yfit, target_names, model_name)
    utils.display_images(Xtest, ytest, yfit, target_names)
    output = f"Model selected: {model_name}\nClassification Report:\n{report}\n\nConfusion Matrix:\n{confusion_mat}"
    return output

def train_model(user_input):

    if user_input == 'RF':
        model_name ='RandomForest'
       
    elif user_input == 'SVC':
        model_name ='SVC'
    
    print(f"Selected model: {model_name}\n")
    model = select_model(model_name, Xtrain, ytrain)
    yfit = model.predict(Xtest)
    output = evaluate_model(Xtest, ytest, yfit, faces.target_names, model_name)
    utils.write_fn(output, f'exercise_4/test_output.txt ')
    return model

if __name__ == '__main__':

    user_input = input("Enter the model type (RF for Random Forest, SVC for Support Vector Machine): ")
    
    train_model(user_input.strip().upper())