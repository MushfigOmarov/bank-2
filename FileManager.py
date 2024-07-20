import json

class FileManager:
    def load_data(self, filename):
        pass
        # TODO:
        # Implement a process that reads the contents of the `filename` file 
        # and returns the text.
        with open(filename, 'r') as file:
            return file.read()

    def save_data(self, filename, data):
        pass
        # TODO:
        # Implement a process that writes the contents of `data` to the file `filename`
        with open(filename, 'w') as file:
            file.write(data)

    def read_json(self, json_file_path):
        pass
        # TODO:
        # Implement a process that reads the contents of a file whose path is stored in the `json_file_path` variable 
        # and returns a list of dictionaries
        with open(json_file_path, 'r') as file:
            return json.load(file)
        
    def write_json(self, list_of_dicts, json_file_path):
        pass
        # TODO:
        # Implement a process that writes a list of dictionaries from list_of_dicts to the `json_file_path` file
        with open(json_file_path, 'w') as json_file:
            json.dump(list_of_dicts, json_file)

    def add_to_json(self, data, json_file_path):
        pass
        # TODO:
        # Implement a process that gets the dictionary in the data variable and adds it to the JSON `json_file_path`
        try:
            existing_data = self.read_json(json_file_path)
        except Exception as e:
            print(f"Error reading {json_file_path}: {e}")
            existing_data = []

        existing_data.append(data)

        try:
            with open(json_file_path, 'w') as json_file:
                json.dump(existing_data, json_file)
        except Exception as e:
            print(f"Error writing to {json_file_path}: {e}")

    

            