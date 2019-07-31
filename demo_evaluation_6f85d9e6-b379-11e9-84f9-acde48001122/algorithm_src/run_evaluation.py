from pathlib import Path

from algorithm import evaluate_iris

class Evaluation(object):
    def run(self):
        """This is boilerplate. Delete the contents of this method and put your
        own algorithm code here. Please do not change the class name
        (Evaluation) or the method name (run).
        """
        submission_file = Path('/')/'input'/'team_eyra.csv'
        test_gt_file = Path('/')/'input'/'iris_public_test_gt.csv'
        out_file = Path('/')/'output'/'iris_leaderboard.csv'

        evaluate_iris(submission_file, test_gt_file, out_file)


# Please do not change anything below
if __name__ == "__main__":
    Evaluation().run()
