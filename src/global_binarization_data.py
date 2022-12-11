class GlobalBinarizationData:

    def __init__(self, ideal_threshold, algorithm_threshold_list, f_measure_list):
        self.ideal_threshold = ideal_threshold
        self.algorithm_threshold_list = algorithm_threshold_list
        self.f_measure_list = f_measure_list
