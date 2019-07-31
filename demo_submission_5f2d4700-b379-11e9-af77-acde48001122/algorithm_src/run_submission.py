from pathlib import Path

from algorithm import iris_svm

class Submission(object):
    def run(self):
        """This is boilerplate. Delete the contents of this method and put your
        own algorithm code here. Please do not change the class name
        (Submission) or the method name (run).
        """
        train_file = Path('/')/'input'/'iris_train.csv'
        test_file = Path('/')/'input'/'iris_public_test_data.csv'
        out_file = Path('/')/'output'/'team_eyra.csv'

        iris_svm(train_file, test_file, out_file)


# Please do not change anything below
if __name__ == "__main__":
    Submission().run()
