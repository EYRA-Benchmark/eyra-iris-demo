import os
import pandas as pd

from pathlib import Path
from sklearn import metrics


def evaluate_iris(submission_file, test_gt_file, out_file):
    # Read gold standard data and convert labels to integers
    test_gt = list(pd.read_csv(test_gt_file)['class'])

    df = pd.read_csv(submission_file)
    pred = list(df['class'])

    f = metrics.f1_score(test_gt, pred, average='weighted')
    prec = metrics.precision_score(test_gt, pred, average='weighted')
    recall = metrics.recall_score(test_gt, pred, average='weighted')

    out = pd.DataFrame([{'F1': f, 'Precision': prec, 'Recall': recall}])
    print(out)
    out.to_csv(out_file, index=None)


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python algorithm_src/algorithm.py
    evaluate_iris(Path('data')/'input'/'team_eyra.csv',
                  Path('data')/'input'/'iris_public_test_gt.csv',
                  Path('data')/'output'/'iris_leaderboard.csv')
