import numpy as np

csv = np.genfromtxt('data.csv', delimiter=',', skip_header=1)
data, labels = csv[:, 1:], csv[:, 0].astype(int)

classes = np.unique(labels)
unique_measurements, unique_data_counts = np.unique(data, return_counts=True)

most_frequent_index = np.argmax(unique_data_counts)
most_frequent_measurement = unique_measurements[most_frequent_index]

if __name__ == "__main__":
    print(f"Classes encontradas:\n{classes}")
    print(f"\nContagens de cada valor único:\n{unique_data_counts}")
    print(f"\nÍndice do valor mais comum:\n{most_frequent_index}")
    print(f"\nMedição mais frequente (Moda):\n{most_frequent_measurement}")

