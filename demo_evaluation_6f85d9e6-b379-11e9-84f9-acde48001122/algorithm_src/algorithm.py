import os
import json
import pandas as pd

from pathlib import Path
from sklearn import metrics


def evaluate_iris(submission_file, test_gt_file, out_file):
    # Read gold standard data and convert labels to integers
    test_gt = list(pd.read_csv(test_gt_file)['class'])

    df = pd.read_csv(submission_file)
    pred = list(df['class'])

    prec = metrics.precision_score(test_gt, pred, average='weighted')
    recall = metrics.recall_score(test_gt, pred, average='weighted')
    f = metrics.f1_score(test_gt, pred, average='weighted')

    out = {'metrics': {'Precision': prec,
                       'Recall': recall,
                       'F1': f}}
    with open(out_file, 'w') as f:
        json.dump(out, f)


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python algorithm_src/algorithm.py
    evaluate_iris(Path('data')/'input'/'implementation_output',
                  Path('data')/'input'/'iris_public_test_gt.csv',
                  Path('data')/'output'/'output')
