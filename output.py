import csv


def generate_csv(file_path, data):
    # create CSV file and write data to it
    with open(file_path, mode='w', newline='') as file:
        fieldnames = data[0].keys()  # get the keys from the first dictionary in the list
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()  # write the header row
        
        # write each dictionary in the list as a row in the CSV file
        for row in data:
            writer.writerow(row)
