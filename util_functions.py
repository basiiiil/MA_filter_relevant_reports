import os
import csv
import datetime
import pandas as pd

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


def merge_csv_files(folder_path, csv_sep=",", csv_encoding="utf-8"):
    """
    Merges all CSV files in a specified folder into a single pandas DataFrame,
    but only if they all have the exact same columns.

    Args:
        folder_path (str): The path to the folder containing the CSV files.
        csv_sep (str): The CSV separator to use.
        csv_encoding (str): The CSV encoding.

    Returns:
        pd.DataFrame: A single DataFrame containing all merged data, or None
                      if no CSV files are found.

    Raises:
        ValueError: If the columns of the CSV files are not identical.
    """
    # Create a list to store DataFrames
    dfs = []

    # Get a list of all CSV files in the folder
    csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

    # If no CSV files are found, return None
    if not csv_files:
        print(f"No CSV files found in '{folder_path}'.")
        return None

    # Read the first file to establish the reference columns
    first_file = os.path.join(folder_path, csv_files[0])
    try:
        reference_df = pd.read_csv(
            first_file,
            dtype="str",
            sep=csv_sep,
            encoding=csv_encoding,
            quotechar='"',
            on_bad_lines="warn",
            keep_default_na=False
        )
        reference_cols = list(reference_df.columns)
        dfs.append(reference_df)
    except Exception as e:
        print(f"Error reading first file '{first_file}': {e}")
        return None

    # Iterate through the rest of the files
    for csv_file in csv_files[1:]:
        file_path = os.path.join(folder_path, csv_file)
        try:
            current_df = pd.read_csv(
                file_path,
                dtype="str",
                sep=csv_sep,
                encoding=csv_encoding,
                quotechar='"',
                on_bad_lines="warn",
                keep_default_na=False
            )
            current_cols = list(current_df.columns)

            # Check if columns are exactly the same as the reference
            if current_cols != reference_cols:
                raise ValueError(
                    f"Column mismatch! '{csv_file}' has columns {current_cols}, "
                    f"but expected columns are {reference_cols}."
                )

            # If columns match, append the DataFrame to the list
            dfs.append(current_df)
        except Exception as e:
            print(f"Error processing file '{file_path}': {e}")
            raise  # Re-raise the exception after printing the error

    # Concatenate all DataFrames in the list
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df