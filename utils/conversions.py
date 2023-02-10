from pandas import DataFrame, read_csv
import json

def csv_to_dict(csv_file: str, visualize_csv=False) -> None:
    """
    Converts CSV to a dictionary in Python.
    Built-in function from Pandas to convert NaN to null (accepted in JSON) is not usable in this case.
    """
    # index_col=0 to get rid of the Unnamed column
    csv_df = read_csv(csv_file, index_col=0)
    if visualize_csv:
        print(csv_df)
    return csv_df.to_dict(orient='records')


def beautify_dict(dictionary: dict) -> None:
    dict_as_json = json.dumps(dictionary, indent=4)
    return dict_as_json 

def response_to_df(response) -> DataFrame:
    """
    Converts a response from requests to a dataframe.
    """
    response_as_json = response.json()
    response_as_dict = json.loads(response_as_json)
    df = DataFrame(response_as_dict)
    return df
