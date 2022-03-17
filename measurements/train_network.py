import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import argparse


def init_argparse():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [OPTION] [FILE]...',
        description='Train a multi-layer perceptron classifier and log measurements.'
    )

    parser.add_argument('--dataset',
                        help='the dataset to train on (default=iris)',
                        choices=['iris', 'digits', 'wine', 'breast_cancer'],
                        default='iris')

    parser.add_argument('--hidden-layer-sizes',
                        help='the number of neurons per hidden layer, such that the ith argument represents the number'
                             'of neurons in the ith hidden layer (default=100)',
                        default=[100],
                        nargs='+',
                        type=int)

    parser.add_argument('--activation',
                        help='activation function for the hidden layer (default=relu)',
                        choices=['identity', 'logistic', 'tanh', 'relu'],
                        default='relu')

    parser.add_argument('--solver',
                        help='the solver for weight optimization (default=adam)',
                        choices=['lbfgs', 'sgd', 'adam'],
                        default='adam')

    parser.add_argument('--learning-rate',
                        help='learning rate schedule for weight updates (default=constant)',
                        choices=['constant', 'invscaling', 'adaptive'],
                        default='constant')

    parser.add_argument('--log-file', help='file to log measurements to')

    return parser


def train_network(dataset, hidden_layer_sizes, activation, solver, learning_rate):
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = dataset.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)

    clf = MLPClassifier(
        random_state=1,
        hidden_layer_sizes=hidden_layer_sizes,
        activation=activation,
        solver=solver,
        learning_rate=learning_rate
    ).fit(X_train, y_train)

    train_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)

    print(f'Train score: {train_score}')
    print(f'Test score: {test_score}')
    print(f'{clf.n_iter_} iterations')


if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()

    dataset = {
        'iris': datasets.load_iris,
        'digits': datasets.load_digits,
        'wine': datasets.load_wine,
        'breast_cancer': datasets.load_breast_cancer,
    }[args.dataset]()

    train_network(dataset, tuple(args.hidden_layer_sizes), args.activation, args.solver, args.learning_rate)
