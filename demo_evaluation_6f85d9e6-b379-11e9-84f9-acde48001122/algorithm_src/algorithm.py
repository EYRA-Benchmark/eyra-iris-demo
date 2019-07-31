import os
import pandas as pd

from pathlib import Path
from sklearn import metrics


def evaluate_iris(submission_file, test_gt_file, out_file):
    # Read gold standard data and convert labels to integers
    test_gt = list(pd.read_csv(test_gt_file)['class'])

    df = pd.read_csv(submission_file)

    f = metrics.f1_score(test_gt, list(df['class']), average='weighted')
    print(f)

    out = pd.DataFrame()
    out['F1'] = [f]
    print(out)
    out.to_csv(out_file, index=None)


if __name__ == "__main__":
    # Run the algorithm on your local copy of the data by typing:
    # python algorithm_src/algorithm.py
    evaluate_iris(Path('data')/'input'/'team_eyra.csv',
                  Path('data')/'input'/'iris_public_test_gt.csv',
                  Path('data')/'output'/'iris_leaderboard.csv')
