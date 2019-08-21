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
    # Create the model using a local copy of the data by typing:
    # python model_creation/train.py
    root = Path(__file__).absolute().parent.parent
    submission_dir = 'demo_submission_5f2d4700-b379-11e9-af77-acde48001122'

    try:
        os.makedirs(Path(root)/submission_dir/'model')
    except FileExistsError:
        pass

    train_file = Path(root)/'data'/'iris_train.csv'
    out_file=Path(root)/submission_dir/'model'/'iris_svm_model'

    clf = train_svm(train_file)
    save_classifier(clf, out_file)