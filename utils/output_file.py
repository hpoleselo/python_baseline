import os
import json
from io import StringIO

def join_output_folder_with_file_path(file_path):
    OUTPUT_FOLDER = 'generated_files'
    if not os.path.exists(OUTPUT_FOLDER):
        os.makedirs(OUTPUT_FOLDER)
    return os.path.join(OUTPUT_FOLDER, file_path)

def save_dict_to_json(dictionary: dict, file_path: str = "json_file.json") -> None:
    """
    Saves dictionary into a JSON file.
    """
    # TODO: Add granular exception handling.
    try:
        with open(file_path, "w") as output_json_file:
            json.dump(dictionary, output_json_file)
            print(f"Wrote file to: {file_path}.")
    except Exception as e:
        print(f"Could not write file to path: {file_path}.")

def dict_to_new_delimited_json(dictionary: dict, file_path: str = "new_delimited.json") -> None:
    """
    
    """
    in_json = StringIO("""[{
        "key01": "value01",
        "key02": "value02",

        "keyN": "valueN"
    },
    {
        "key01": "value01",
        "key02": "value02",

        "keyN": "valueN"
    },
    {
        "key01": "value01",
        "key02": "value02",

        "keyN": "valueN"
    }
    ]""")
    # TODO: Implement the conversion from byte streams to dict so that this function can be used
    return [json.dumps(record) for record in json.load(in_json)]