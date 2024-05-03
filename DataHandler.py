import os
import pickle

class DataHandler:
    @staticmethod
    def save_data(data, filename):
      
        if not os.path.exists(filename):
            print(f"File '{filename}' does not exist. Creating a new file.")
            with open(filename, 'wb'):
                pass  # Create an empty file
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    @staticmethod
    def load_data(filename):
       
        if os.path.exists(filename):
            with open(filename, 'rb') as file:
                data = pickle.load(file)
            return data
        else:
            print(f"File '{filename}' does not exist. Returning None.")
            return None
