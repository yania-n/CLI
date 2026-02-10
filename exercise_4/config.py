from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
class ModelObjects:
    '''
    Docstring for ModelObjects
    
    '''

    def __init__(self):

        self.rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.rf_param_grid = [{'ccp_alpha':[0, 0.001, 0.002, 0.003, 0.004, 0.005]}]

        self.svc_model = Pipeline([('scaler', StandardScaler()),('svc',SVC(kernel='rbf', random_state=42))])
        self.svc_param_grid = [{'svc__C': [1, 5, 10, 50],'svc__gamma': [0.0001, 0.0005, 0.001, 0.005]} ] 

