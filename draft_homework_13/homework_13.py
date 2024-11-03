import json
import os
import logging

def read_csv(file_name):
    with open(file_name, 'r') as csv_file:
        data = csv_file.readlines()
    return data
def write_csv(file_name, lines):
    with open(file_name, 'w') as csv_file:
        csv_file.writelines(lines)

file1_data = read_csv('random-michaels.csv')
file2_data = read_csv('random.csv')
all_data = file1_data + file2_data
sort_by_unique_data = list(set(all_data))

write_csv('unique_result.csv', sort_by_unique_data)

logging.basicConfig(
    filename='valid_json.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def is_valid_json(file_path):

    try:
        with open(file_path, 'r') as f:
            json.load(f)
        return True
    except (json.JSONDecodeError, IOError) as e:
        logging.error(f"Invalid JSON in file: {file_path} - {e}")
        return False

def check_all_json_files(directory_path):

    for filename in os.listdir(directory_path):
        file_path = os.path.join(directory_path, filename)
        if filename.endswith('.json'):
            is_valid_json(file_path)

directory_path = os.path.join(os.getcwd(), 'json_example')
check_all_json_files(directory_path)
# print(os.path.join(os.getcwd(), 'json_example'))