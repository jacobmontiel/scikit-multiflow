import numpy as np
from skmultiflow.trees import LabelCombinationHoeffdingTree
from skmultiflow.data import MultilabelGenerator


def test_label_combination_hoeffding_tree_mc(test_path):
    stream = MultilabelGenerator(n_samples=10000, n_features=15, n_targets=3, n_labels=4, random_state=112)

    stream.prepare_for_use()

    learner = LabelCombinationHoeffdingTree(n_labels=3, leaf_prediction='mc')

    cnt = 0
    max_samples = 5000
    predictions = []
    proba_predictions = []
    wait_samples = 100

    while cnt < max_samples:
        X, y = stream.next_sample()
        # Test every n samples
        learner.partial_fit(X, y)
        if cnt % wait_samples == 0 and (cnt != 0):
            predictions.append(learner.predict(X)[0].tolist())
            proba_predictions.append(learner.predict_proba(X)[0])
        cnt += 1

    print(predictions)
    expected_predictions = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]

    assert np.alltrue(predictions == expected_predictions)
    assert type(learner.predict(X)) == np.ndarray
    assert type(learner.predict_proba(X)) == np.ndarray

    expected_info = "LabelCombinationHoeffdingTree(binary_split=False, grace_period=200, leaf_prediction='mc', " \
                    "max_byte_size=33554432, memory_estimate_period=1000000, n_labels=3, nb_threshold=0, " \
                    "no_preprune=False, nominal_attributes=None, remove_poor_atts=False, split_confidence=1e-07, " \
                    "split_criterion='info_gain', stop_mem_management=False, tie_threshold=0.05)"
    info = " ".join([line.strip() for line in learner.get_info().split()])
    assert info == expected_info


def test_label_combination_hoeffding_tree_nb(test_path):
    stream = MultilabelGenerator(n_samples=10000, n_features=15, n_targets=3, n_labels=4, random_state=112)

    stream.prepare_for_use()

    learner = LabelCombinationHoeffdingTree(n_labels=3, leaf_prediction='nb')

    cnt = 0
    max_samples = 5000
    predictions = []
    proba_predictions = []
    wait_samples = 100

    while cnt < max_samples:
        X, y = stream.next_sample()
        # Test every n samples
        learner.partial_fit(X, y)
        if cnt % wait_samples == 0 and (cnt != 0):
            predictions.append(learner.predict(X)[0].tolist())
            proba_predictions.append(learner.predict_proba(X)[0])
        cnt += 1

    print(predictions)
    expected_predictions = [[0, 0, 1], [1, 1, 1], [0, 1, 1], [0, 1, 1], [1, 1, 1], [0, 1, 1],
                            [1, 1, 0], [1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 1, 0],
                            [1, 0, 0], [1, 0, 1], [1, 1, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1],
                            [0, 0, 0], [1, 1, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1], [0, 0, 1],
                            [1, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 1, 1], [0, 0, 1],
                            [1, 1, 1], [0, 0, 0], [0, 1, 0], [1, 1, 1], [0, 1, 1], [1, 1, 0],
                            [0, 0, 1], [0, 0, 0], [1, 1, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1],
                            [1, 1, 1], [1, 1, 1], [0, 1, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1],
                            [1, 1, 1]]

    assert np.alltrue(predictions == expected_predictions)
    assert type(learner.predict(X)) == np.ndarray
    assert type(learner.predict_proba(X)) == np.ndarray

    expected_info = "LabelCombinationHoeffdingTree(binary_split=False, grace_period=200, leaf_prediction='nb', " \
                    "max_byte_size=33554432, memory_estimate_period=1000000, n_labels=3, nb_threshold=0, " \
                    "no_preprune=False, nominal_attributes=None, remove_poor_atts=False, split_confidence=1e-07, " \
                    "split_criterion='info_gain', stop_mem_management=False, tie_threshold=0.05)"
    info = " ".join([line.strip() for line in learner.get_info().split()])
    assert info == expected_info


def test_label_combination_hoeffding_tree_nba(test_path):
    stream = MultilabelGenerator(n_samples=10000, n_features=15, n_targets=3, n_labels=4, random_state=112)

    stream.prepare_for_use()

    learner = LabelCombinationHoeffdingTree(n_labels=3)

    cnt = 0
    max_samples = 5000
    predictions = []
    proba_predictions = []
    wait_samples = 100

    while cnt < max_samples:
        X, y = stream.next_sample()
        # Test every n samples
        learner.partial_fit(X, y)
        if cnt % wait_samples == 0 and (cnt != 0):
            predictions.append(learner.predict(X)[0].tolist())
            proba_predictions.append(learner.predict_proba(X)[0])
        cnt += 1

    print(predictions)
    expected_predictions = [[0, 0, 1], [1, 1, 1], [0, 1, 1], [0, 1, 1], [1, 1, 1], [0, 1, 1], [1, 1, 0], [1, 1, 1],
                           [1, 1, 1], [1, 1, 1], [0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1], [1, 1, 1],
                           [0, 1, 1], [1, 1, 1], [0, 0, 0], [1, 1, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1], [0, 0, 1],
                           [1, 0, 1], [1, 1, 1], [1, 0, 0], [1, 1, 1], [1, 1, 1], [0, 0, 1], [1, 1, 1], [0, 0, 0],
                           [0, 1, 0], [1, 1, 1], [0, 1, 1], [1, 1, 0], [0, 0, 1], [0, 0, 0], [1, 1, 1], [1, 1, 1],
                           [1, 0, 1], [0, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 0], [0, 1, 0], [1, 1, 1], [1, 1, 1],
                           [1, 1, 1]]

    assert np.alltrue(predictions == expected_predictions)
    assert type(learner.predict(X)) == np.ndarray
    assert type(learner.predict_proba(X)) == np.ndarray

    expected_info = "LabelCombinationHoeffdingTree(binary_split=False, grace_period=200, leaf_prediction='nba', " \
                    "max_byte_size=33554432, memory_estimate_period=1000000, n_labels=3, nb_threshold=0, " \
                    "no_preprune=False, nominal_attributes=None, remove_poor_atts=False, split_confidence=1e-07, " \
                    "split_criterion='info_gain', stop_mem_management=False, tie_threshold=0.05)"
    info = " ".join([line.strip() for line in learner.get_info().split()])
    assert info == expected_info