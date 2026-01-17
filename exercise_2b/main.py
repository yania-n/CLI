# use argument passer to take in some feature values from command line 
# and predict the price for that specific house
# then save the prediction to a text file

import pandas as pd
import argparse
import exercise_2b.model_training as model_train
from exercise_1a.write_function import write_fn

def get_parser():
    parser = argparse.ArgumentParser(description="Predict house price based on features", add_help = False)
    parser.add_argument('--beds', type = int, required = True, help = 'number of beds')
    parser.add_argument('--baths', type = int, required = True, help = 'number of baths')
    parser.add_argument('-s', '--size', type = float, required = True, help = 'size of the house in square feet')
    parser.add_argument('-z', '--zip_code', type = int, required = True, help = 'zip code of the house location')

    return parser

def predict_price(args):
    features = pd.DataFrame([[args.beds, args.baths, args.size, args.zip_code]])
    features.columns = ['beds', 'baths', 'size', 'zip_code']
    predicted_value = model_train.ModelObject.call_predict(features)
    predicted_value = (predicted_value[0]).round(3)
    mse, r2 = model_train.mse, model_train.r2

    output = f'Property feature: \n{features}, \nPredicted price: {predicted_value}'
    print(output)
    return output

if __name__ == '__main__':
    standalone_parser = argparse.ArgumentParser(parents = [get_parser()])
    args = standalone_parser.parse_args()
    output = predict_price(args)
    
    # Write result to a file
    filepath = 'exercise_2b/predicted_price.txt'
    write_fn(output, filepath) 

# provide features in this format when running the script: --beds 2 --baths 2 --size 900 -z 98107