from skmultiflow.trees import HoeffdingTreeClassifier
from skmultiflow.meta import LeverageBaggingClassifier
from skmultiflow.data import WaveformGenerator
from skmultiflow.evaluation import EvaluatePrequential


def demo(output_file=None, instances=40000):
    """ _test_prequential_bagging
    
    This demo shows the evaluation process of a LeverageBaggingClassifier,
    initialized with different base estimators.
    
    Parameters
    ----------
    output_file: string
        The name of the csv output file
    
    instances: int
        The evaluation's max number of instances
    
    """
    # Setup the File Stream
    # stream = FileStream("../data/datasets/sea_big.csv", -1, 1)
    #stream = SEAGenerator(classification_function=2, noise_percentage=0.0)
    #stream.prepare_for_use()
    stream = WaveformGenerator()
    stream.prepare_for_use()

    # Setup the classifier
    #classifier = OzaBaggingADWINClassifier(base_estimator=KNNClassifier(n_neighbors=8, max_window_size=2000,
    #                                                                    leaf_size=30))
    #classifier = LeverageBaggingClassifier(base_estimator=KNNClassifier(n_neighbors=8, max_window_size=2000,
    #                                                                    leaf_size=30),
    #                                       n_estimators=1)
    pipe = LeverageBaggingClassifier(base_estimator=HoeffdingTreeClassifier(), n_estimators=2)

    # Setup the pipeline
    #pipe = Pipeline([('Classifier', classifier)])

    # Setup the evaluator
    evaluator = EvaluatePrequential(pretrain_size=2000, max_samples=instances, output_file=output_file, show_plot=False)

    # Evaluate
    evaluator.evaluate(stream=stream, model=pipe)


if __name__ == '__main__':
    demo('test_prequential_bagging.csv', 20000)
