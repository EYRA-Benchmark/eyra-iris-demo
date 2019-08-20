from pathlib import Path

from algorithm import iris_svm

class Submission(object):
    def run(self):
        """This is boilerplate. Delete the contents of this method and put your
        own algorithm code here. Please do not change the class name
        (Submission) or the method name (run).
        """
        # These are the default file paths (names) for input and output
        test_file = Path('/')/'data'/'input'/'test_data'
        out_file = Path('/')/'data'/'output'/'implementation_output'

        # Additional data required by the algorithm
        model_file = Path(__file__).absolute().parent/'model'/'iris_svm_model'

        iris_svm(model_file, test_file, out_file)


# Please do not change anything below
if __name__ == "__main__":
    Submission().run()
