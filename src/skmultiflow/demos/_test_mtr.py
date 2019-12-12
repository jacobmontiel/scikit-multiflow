from skmultiflow.data import RegressionGenerator
from skmultiflow.evaluation.evaluate_prequential import EvaluatePrequential
from skmultiflow.trees.isoup_tree import iSOUPTreeRegressor


def demo(output_file=None):
    """ Test iSOUP-Tree

    This demo demonstrates how to evaluate a iSOUP-Tree multi-target regressor.
    The employed dataset is 'scm1d', which is contained in the data folder.

    Parameters
    ----------
    input_file: string
        A string describing the path for the input dataset

    output_file: string
        The name of the csv output file

    """
    stream = RegressionGenerator(n_samples=5000, n_features=20,
                                 n_informative=15, random_state=1,
                                 n_targets=7)
    stream.prepare_for_use()

    classifier = iSOUPTreeRegressor(leaf_prediction='adaptive')

    # Setup the evaluator
    evaluator = EvaluatePrequential(pretrain_size=1, batch_size=1, n_wait=200,
                                    max_time=1000, output_file=output_file,
                                    show_plot=False,
                                    metrics=['average_mean_square_error',
                                             'average_mean_absolute_error',
                                             'average_root_mean_square_error'])

    # Evaluate
    evaluator.evaluate(stream=stream, model=classifier)


if __name__ == '__main__':
    # demo('mtr_test_adaptive.csv')
    demo()
