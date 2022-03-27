import pandas as pd
import argparse
import pathlib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
    
def init_argparse():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [--data <path-to-data>]',
        description='data.'
    )

    parser.add_argument('data',
                        type=pathlib.Path,
                        help='path to data',
                        default=['./out.csv'])   
                      
    return parser
    
def preprocess(df):
    del df['timestamp']
    del df['system']
    del df['train_score']
    del df['test_score']
    del df['average processor power']
    del df['activation']
    del df['solver']
    
    return df
    
def train_model(df):
    model = LinearRegression()
    X = df.drop(['score'], axis=1)
    y = df['score']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1, test_size=0.1)
    
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions, squared=False)

    print('The r2 is: ', r2)
    print('The rmse is: ', rmse)
                        
if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()   

    df = pd.read_csv(args.data)
    df = preprocess(df)
    train_model(df)
    