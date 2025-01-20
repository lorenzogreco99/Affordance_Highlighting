import pickle


def load_data(file_path):
    # Open and load file
    with open(file_path, "rb") as file:
        data = pickle.load(file)
    print(f"Type: {type(data)}")
    return data