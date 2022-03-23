import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
import argparse
import csv
from datetime import datetime
from dataclasses import dataclass
from sklearn.datasets import make_classification


def init_argparse():
    parser = argparse.ArgumentParser(
        usage='%(prog)s [--dataset <dataset>] [--hidden-layer-sizes <hidden-layer-sizes>] [--activation <activation>] '
              '[--solver <solver>] [--learning-rate <learning-rate>] [--log-file <log-file>]',
        description='Train a multi-layer perceptron classifier and log measurements.'
    )

    parser.add_argument('--dataset',
                        help='the dataset to train on (default=iris)',
                        choices=['iris', 'digits', 'wine', 'breast_cancer', 'covertype', 'rcv1', 'lfw'],
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
                        
    parser.add_argument('--samples',
                        help='total number of samples (default=100)',
                        default=100,
                        type=int)
                        
    parser.add_argument('--features',
                        help='total number of features (default=5)',
                        default=5,
                        type=int)   

    parser.add_argument('--classes',
                        help='total number of classes (default=3)',
                        default=3,
                        type=int)   
                        
    parser.add_argument('--log-file', help='file to log measurements to')

    return parser


@dataclass
class TrainingResult:
    iterations: int
    train_score: float
    test_score: float


def train_network(hidden_layer_sizes, activation, solver, samples, features, classes ):
    X, y = make_classification(n_samples=0.6*samples, n_features=features, random_state=0, n_classes=classes, n_repeated=0.2*samples, n_redundant=0.2*samples)

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)

    clf = MLPClassifier(
        random_state=1,
        hidden_layer_sizes=hidden_layer_sizes,
        activation=activation,
        solver=solver,
    ).fit(X_train, y_train)

    train_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)

    return TrainingResult(clf.n_iter_, train_score, test_score)

if __name__ == '__main__':
    parser = init_argparse()
    args = parser.parse_args()


    res = train_network(tuple(args.hidden_layer_sizes), args.activation, args.solver, args.samples, args.features, args.classes)

    if args.log_file:
        with open(args.log_file, 'a+') as f:
            writer = csv.writer(f)

            f.seek(0)
            if not f.read(1):
                writer.writerow(['timestamp', 'n_samples', 'n_features', 'hidden_layer_sizes', 'classes',
                                 'activation', 'solver', 'iterations', 'train_score', 'test_score'])

            writer.writerow([datetime.now().isoformat(), args.samples, args.features,
                             tuple(args.hidden_layer_sizes), args.classes, args.activation, args.solver,
                             res.iterations, res.train_score, res.test_score])
