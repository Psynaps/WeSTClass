import csv

# File paths
movies_train_path = 'movies/movies_train.txt'
movies_train_labels_path = 'movies/movies_train_labels.txt'
output_csv_path = 'movies/dataset.csv'

# Read the documents from movies_train.txt
with open(movies_train_path, 'r', encoding='utf-8') as file:
    documents = [line.strip() for line in file]

# Read the labels from movies_train_labels.txt
with open(movies_train_labels_path, 'r', encoding='utf-8') as file:
    labels = [line.strip() for line in file]

# Check that the number of documents and labels are the same
if len(documents) != len(labels):
    raise ValueError("The number of documents and labels must be the same")

# Write to dataset.csv
with open(output_csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL)
    for label, document in zip(labels, documents):
        writer.writerow([label, document])
