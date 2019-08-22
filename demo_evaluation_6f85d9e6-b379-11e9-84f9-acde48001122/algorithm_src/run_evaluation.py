from pathlib import Path

from algorithm import evaluate_iris

class Evaluation(object):
    def run(self):
        """This is boilerplate. Delete the contents of this method and put your
        own algorithm code here. Please do not change the class name
        (Evaluation) or the method name (run).
        """
        # These are the default file paths (names) for input and output
        submission_file = Path('/')/'data'/'input'/'implementation_output'
        test_gt_file = Path('/')/'data'/'input'/'ground_truth'
        out_file = Path('/')/'data'/'output'

        evaluate_iris(submission_file, test_gt_file, out_file)


# Please do not change anything below
if __name__ == "__main__":
    Evaluation().run()
