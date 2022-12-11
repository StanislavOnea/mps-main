import treelib
from tree_factory import TreeFactory
from csv_reader import CsvReader

def global_binarization():
    csv_reader = CsvReader("GLOBAL")
    global_binarization_data_list = csv_reader.get_global_binarization_data_list()

    # Train
    train_array = []
    train_step = int((len(global_binarization_data_list) * 70) / 100)
    for i in range(1000):
        temp_tree = TreeFactory()
        score = 0
        for i in range(0, train_step):
            temp_tree.populate_tree(global_binarization_data_list[i].algorithm_threshold_list)
            treshhold = temp_tree.compute_operations()
            ideal_value = abs(global_binarization_data_list[i].ideal_threshold)
            score += abs(abs(ideal_value) - abs(treshhold))
        
        # Daca sunt la fel ce facem?
        temp_tree.score = score
        if len(train_array) < 2:
            train_array.append(temp_tree)
        elif train_array[0].score > temp_tree.score:
            train_array[1] = train_array[0]
            train_array[0] = temp_tree
        elif train_array[1].score > temp_tree.score:
            train_array[1] = temp_tree


    # Din 1000 de arbori trebuie sa alegem cei mai buni si sa alegem operatiile cele mai optime pt. alg.
    # Validation
    validation_array = []
    validation_array = train_array
    for i in range(500):
        temp_tree = TreeFactory()
        score = 0

        validation_step = int((len(global_binarization_data_list) * 95) / 100)
        for i in range(train_step, validation_step):
            temp_tree.populate_tree(global_binarization_data_list[i].algorithm_threshold_list)
            treshhold = temp_tree.compute_operations()
            ideal_value = abs(global_binarization_data_list[i].ideal_threshold)
            score += abs(abs(ideal_value) - abs(treshhold))
        
        # Daca sunt la fel ce facem?
        temp_tree.score = score
        if validation_array[0].score > temp_tree.score:
            validation_array[1] = validation_array[0]
            validation_array[0] = temp_tree
        elif validation_array[1].score > temp_tree.score:
            validation_array[1] = temp_tree

    # Test
    test_array = train_array + validation_array
    best_tree = None
    for i in range(len(test_array)):
        temp_tree = test_array[i]
        score = 0

        for i in range(validation_step, len(global_binarization_data_list)):
            temp_tree.populate_tree(global_binarization_data_list[i].algorithm_threshold_list)
            treshhold = temp_tree.compute_operations()
            ideal_value = abs(global_binarization_data_list[i].ideal_threshold)
            score += abs(abs(ideal_value) - abs(treshhold))
        
        # Daca sunt la fel ce facem?
        temp_tree.score = score
        if best_tree == None:
            best_tree = temp_tree
        elif best_tree.score > temp_tree.score:
            best_tree = temp_tree

    best_tree.show()

def main():   
    global_binarization()

if __name__ == "__main__":
    main()
