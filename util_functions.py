import csv
import datetime
import pandas as pd

DATA_FOLDER_PATH = "csvs_from_Befundtexte/"

def write_to_csv(df, output_filename_without_ending):
    now = datetime.datetime.now()
    output_filename = f"{now.strftime("%Y-%m-%d_%X")}_{output_filename_without_ending}.csv"

    df.to_csv(
        output_filename,
        encoding='utf-8',
        index=False,  # Prevent pandas from writing the DataFrame index as a column
        quotechar='"',  # Ensure the output uses the same quote character
        quoting=csv.QUOTE_ALL
    )

    return output_filename

def check_columns(df_list):
    first_cols_set = set(df_list[0].columns)
    all_match = all(set(df.columns) == first_cols_set for df in df_list)
    return all_match