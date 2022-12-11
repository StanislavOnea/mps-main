import csv
from global_binarization_data import GlobalBinarizationData
from os import listdir
from os.path import isfile, join


class CsvReader:
    MPS_GLOBAL_DIRECTORY_PATH = "../input/mps-global"
    MPS_LOCAL_DIRECTORY_PATH = "../input/mps-local"

    def __init__(self, mode):
        if (mode != "GLOBAL" and mode != "LOCAL"):
            print("Invalid mode! Please choose between 'GLOBAL' and 'LOCAL' mode.")
            exit(1)

        self.mode = mode

    def get_global_binarization_data_list(self):
        global_binarization_data_list = []
        directory_path = self.MPS_GLOBAL_DIRECTORY_PATH if self.mode == "GLOBAL" else self.MPS_LOCAL_DIRECTORY_PATH
        file_paths = self.__get_csv_file_paths(directory_path)

        for file_path in file_paths:
            global_binarization_data = self.__get_global_binarization_data(
                file_path)
            global_binarization_data_list.append(global_binarization_data)

        return global_binarization_data_list

    def __get_csv_file_paths(self, directory_path):
        file_paths = []

        files = [f for f in listdir(directory_path)
                 if isfile(join(directory_path, f))]
        for file_name in files:
            file_path = '{}/{}'.format(directory_path, file_name)
            file_paths.append(file_path)

        return file_paths

    def __get_global_binarization_data(self, csv_file_path):
        rows = []
        file = open(csv_file_path, "r")
        csv_reader = csv.reader(file)

        for row in csv_reader:
            rows.append(row)

        ideal_threshold = float(rows[0][0])
        algorithm_threshold_list = []
        f_measure_list = []

        for i in range(1, 16):
            algorithm_threshold_list.append(float(rows[0][i]))

        for i in range(0, 256):
            f_measure_list.append(float(rows[1][i]))
        
        global_binarization_data = GlobalBinarizationData(
            ideal_threshold, algorithm_threshold_list, f_measure_list)

        file.close()

        return global_binarization_data
