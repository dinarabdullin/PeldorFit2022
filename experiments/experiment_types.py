'''
The dictionary with different experiments
'''

from experiments.experiment import Experiment
from experiments.peldor_4p_rect import Peldor_4p_rect

experiment_types = {}
experiment_types["4pELDOR-rect"] = Peldor_4p_rect