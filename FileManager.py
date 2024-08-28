import json


class FileManager:
    def load_data(self, filename):
        with open(filename, 'r') as file:
            return file.read()

    def save_data(self, filename, data):
        with open(filename, 'w') as file:
            file.write(data)

    def read_json(self, json_file_path):
        with open(json_file_path, 'r') as file:
            return json.load(file)

    def write_json(self, list_of_dicts, json_file_path):
        with open(json_file_path, 'w') as json_file:
            json.dump(list_of_dicts, json_file)

    def add_to_json(self, data, json_file_path):
        # try:
        #             existing_data = self.read_json(json_file_path)
        #         except Exception as e:
        #             print(f"Error reading {json_file_path}: {e}")
        #             existing_data = []

        #         existing_data.append(data)

        #         try:
        #             with open(json_file_path, 'w') as json_file:
        #                 json.dump(existing_data, json_file)
        #         except Exception as e:
        #             print(f"Error writing to {json_file_path}: {e}")
        existing_data = self.read_json(json_file_path)
        existing_data.append(data)
        self.write_json(existing_data, json_file_path)