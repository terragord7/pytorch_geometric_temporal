from typing import Union, Tuple
from torch_geometric_temporal.data.discrete.static_graph_discrete_signal import StaticGraphDiscreteSignal


def discrete_train_test_split(data_iterator, train_ratio: float=0.8) -> Tuple[StaticGraphDiscreteSignal, StaticGraphDiscreteSignal]:
    """
    Sampling nodes randomly proportional to the normalized pagerank score.

    Arg types:
        * **graph** *(NetworkX or NetworKit graph)* - The graph to be sampled from.

    Return types:
        * **new_graph** *(NetworkX or NetworKit graph)* - The graph of sampled nodes.
    """
    train_snapshots = int(train_ratio*len(data_iterator.features))

    if type(data_iterator) == StaticGraphDiscreteSignal:
        train_iterator = StaticGraphDiscreteSignal(data_iterator.edge_index,
                                                   data_iterator.edge_weight,
                                                   data_iterator.features[0:train_snapshots],
                                                   data_iterator.targets[0:train_snapshots])

        test_iterator = StaticGraphDiscreteSignal(data_iterator.edge_index,
                                                  data_iterator.edge_weight,
                                                  data_iterator.features[train_snapshots:],
                                                  data_iterator.targets[train_snapshots:])
    return train_iterator, test_iterator
