import os

import pandas as pd

from pathlib import Path
from joblib import dump

from sklearn import svm


def train_svm(in_file):
    """Train Support Vector Machines for the EYRA Demo Benchmark.
    """

    # Read the training file
    train = pd.read_csv(in_file)

    train_data = train[['sepal_length', 'sepal_width', 'petal_length',
                        'petal_width']].values
    train_targets = list(train['class'])

    # Train the classifier
    clf = svm.SVC(gamma=0.001, C=100.)
    clf.fit(train_data, train_targets)

    return clf


def save_classifier(clf, path):
    dump(clf, path)


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python algorithm_scr/train.py
    try:
        os.makedirs(Path('algorithm_src')/'model')
    except FileExistsError:
        pass

    train_file = Path('data')/'input'/'iris_train.csv'
    test_file = Path('data')/'input'/'iris_public_test_data.csv'
    out_file = Path('algorithm_src')/'model'/'iris_svm_model'

    clf = train_svm(train_file)
    save_classifier(clf, out_file)