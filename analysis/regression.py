import numpy as np
import pandas as pd
import argparse
import pathlib
import itertools
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neural_network import MLPRegressor
import matplotlib.pyplot as plt
from sklearn.feature_selection import SelectKBest, r_regression


def init_argparse():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [--data <path-to-data>]',
        description='Train regression model on data.'
    )

    parser.add_argument('--data',
                        type=pathlib.Path,
                        help='path to data',
                        default='./out.csv')

    return parser


def preprocess(df):
    del df['timestamp']
    del df['system']
    del df['train_score']
    del df['test_score']
    del df['energy']
    del df['activation']
    del df['solver']
    del df['iterations']
    del df['avg_iteration_energy']

    return df


def compute_regression(X, y):
    # feature selection
    f_selector = SelectKBest(score_func=r_regression, k='all')
    # learn relationship from training data
    f_selector.fit(X, y)
    
    print(list(X.columns.values))

    print(f_selector.scores_)


def train_model(df, mlp=False, degree=1, hidden_layer_sizes=(10,), ax=None, ax_title=None):
    X = df.drop(['cost'], axis=1)
    y = df['cost']
    
    compute_regression(X, y)

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    model = MLPRegressor(random_state=1, max_iter=10000, hidden_layer_sizes=hidden_layer_sizes) \
        if mlp else make_pipeline(PolynomialFeatures(degree), LinearRegression())

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    rmse = mean_squared_error(y_test, predictions, squared=False)
    err_var = np.var(y_test - predictions)

    print('The r2 is: ', r2)
    print('The rmse is: ', rmse)
    print('The error variance is: ', err_var)

    ax.scatter(y_test, predictions)
    ax.plot(range(14), range(14), color='red')
    ax.set_xlabel('true cost')
    ax.set_ylabel('predicted cost')
    ax.set_title(ax_title)
    plt.axis('scaled')


def find_mlp_config(max_layers=2, max_layer_size=20):
    X = df.drop(['cost'], axis=1)
    y = df['cost']

    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

    def train(hidden_layer_sizes):
        reg = MLPRegressor(
            random_state=1,
            max_iter=10000,
            hidden_layer_sizes=hidden_layer_sizes
        ).fit(X_train, y_train)

        return mean_squared_error(y_test, reg.predict(X_test))

    configs = []
    for n_layers in range(1, max_layers + 1):
        configs.extend(itertools.product(*[list(range(1, max_layer_size + 1)) for _ in range(n_layers)]))

    return min(configs, key=train)


if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()

    df = pd.read_csv(args.data)
    df = preprocess(df)

    fig = plt.figure(figsize=[19.2, 9.6])

    ax = fig.add_subplot(131)
    train_model(df, mlp=False, degree=1, hidden_layer_sizes=(9, 2, 7), ax=ax, ax_title='Linear')

    ax = fig.add_subplot(132)
    train_model(df, mlp=False, degree=3, hidden_layer_sizes=(9, 2, 7), ax=ax, ax_title='Cubic')

    ax = fig.add_subplot(133)
    train_model(df, mlp=True, degree=1, hidden_layer_sizes=(9, 2, 7), ax=ax, ax_title='MLP')

    plt.show()
