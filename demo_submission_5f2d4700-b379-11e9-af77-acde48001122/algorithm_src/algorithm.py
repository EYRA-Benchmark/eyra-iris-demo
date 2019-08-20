import pandas as pd

from pathlib import Path
from joblib import load

from sklearn import svm


def predict(clf, test_data_file):
    test = pd.read_csv(test_data_file)

    return clf.predict(test.values)


def iris_svm(model_file, test_file, out_file):
    # Load classifier
    clf = load(model_file)

    # Predict
    pred = predict(clf, test_file)

    # Write the output to file
    output = pd.DataFrame()
    output['class'] = pred
    output.to_csv(out_file)


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python algorithm_scr/algorithm.py
    model_file = Path(__file__).absolute().parent/'model'/'iris_svm_model'
    test_file = Path('data')/'input'/'test_data'
    out_file = Path('data')/'output'/'implementation_output'

    iris_svm(model_file, test_file, out_file)
