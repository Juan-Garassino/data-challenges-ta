import os

print(os.path.dirname(__file__))

root_directory = os.path.dirname(os.path.dirname(__file__))

data_directory = os.path.join(root_directory, "data", "csv")

print(root_directory)

file_names = [f for f in data_directory if f.endswith(".csv")]

print(file_names)