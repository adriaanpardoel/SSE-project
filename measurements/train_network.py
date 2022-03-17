import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


def run():
    dataset = datasets.load_iris()
    X = pd.DataFrame(dataset.data, columns=dataset.feature_names)
    y = dataset.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=1)

    clf = MLPClassifier(random_state=1).fit(X_train, y_train)

    train_score = clf.score(X_train, y_train)
    test_score = clf.score(X_test, y_test)

    print(f'Train score: {train_score}')
    print(f'Test score: {test_score}')
    print(f'{clf.n_iter_} iterations')


if __name__ == '__main__':
    run()
