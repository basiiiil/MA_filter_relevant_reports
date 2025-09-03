"""
In dieser Datei:
1. Die exportierten Daten werden in ein Pandas dataframe umgewandelt.
2. Die Daten werden nach relevanten Prozeduren gefiltert.
    a. Alle Tuple, deren Prozedurentitel (COLNAME_PROZEDUR) nicht in relevant_ZBEFALL.csv enthalten ist,
       werden entfernt.
       Tuple mit leerem Prozedurentitel werden dabei nicht entfernt.
    b. Alle Befundtexte werden nach Schlüsselwörtern durchsucht (nur die ersten 6 nicht-leeren Zeilen).
       Es werden nur diejenigen Tupel beibehalten, die mindestens eines der Schlüsselwörter (case-insensitive)
       aus jeder der folgenden Listen enthalten:
        1. 'ct', 'computertomographie', 'computertomografie', 'spiral', 'polytrauma'
        2. 'km', 'kontrastmittel', 'PET'
        3. 'thorax', 'koerperstamm', 'körperstamm', 'pulm', 'lunge', 'aorta', 'spiral', 'polytrauma', 'PET'
3. Der Text in COLNAME_BEFUNDTEXT wird bei „Beurteilung:“ geteilt und der zweite Teil
   wird in eine neue Spalte „assessment“ eingefügt.
4. Die endgültige Tabelle wird optional als CSV exportiert.
"""

import pandas as pd
import numpy as np
import re

from config import COLNAME_PROZEDUR, EXPORTED_DATA_FOLDER_PATH, IMPORT_SEPARATOR, IMPORT_ENCODING, WRITE_TO_CSV, \
    COLUMNS_IN_OUTPUT, OUTPUT_FILENAME, CONTENT_IN_MULTIPLE_COLUMNS, MULTIPLE_CONTENT_COLS_PREFIX, \
    COLNAME_BEFUNDTEXT, IMPORT_FILETYPE_IS_XLSX, OUTPUT_FOLDER_PATH
from filterParams import KEYWORD_LISTS
from util_functions import write_to_csv, merge_csv_files, merge_xlsx_files


def check_for_keywords(text):
    """
    Checks if all specified keywords are present in the text (case-insensitive).
    Handles NaN/empty strings by treating them as not containing the keywords.
    """
    if pd.isna(text) or not str(text).strip():  # Check for NaN or empty string after stripping whitespace
        return False
    text_str = str(text)

    for sublist in KEYWORD_LISTS:
        found_in_sublist = False
        for keyword in sublist:
            if re.search(re.escape(keyword), text_str, re.IGNORECASE):
                found_in_sublist = True
                break
        if not found_in_sublist:
            return False
    return True


# Apply the check for 'Report' column (first 4 lines)
def check_report_for_keywords(text):
    if pd.isna(text):
        return False
    lines = str(text).splitlines()
    non_empty_lines = [line for line in lines if line.strip()]
    search_string = "\n".join(non_empty_lines[:6])  # Take at most the first 6 lines
    return check_for_keywords(search_string)


def get_relevant_reports(df):
    df_relevant_procedures = pd.read_csv("relevant_ZBEFALL.csv", dtype=np.str_)

    df_unfiltered = df.copy()

    # 2a. check if title of procedure (COLNAME_PROZEDUR) is in list of relevant procedures.
    # Write as boolean to new column:
    df_unfiltered['has_relevant_procedure'] = df_unfiltered[COLNAME_PROZEDUR].str.lower().isin(
        df_relevant_procedures[COLNAME_PROZEDUR].str.lower()
    )

    # check if title of procedure (COLNAME_PROZEDUR) has relevant keywords. Write as boolean to new column:
    df_unfiltered['has_keyword_in_procedure_title'] = df_unfiltered[COLNAME_PROZEDUR].apply(
        lambda x: check_for_keywords(x)
    )

    # 2b. check if first 6 non-empty lines have relevant keywords. Write as boolean to new column:
    if COLNAME_BEFUNDTEXT not in df_unfiltered.columns and not CONTENT_IN_MULTIPLE_COLUMNS:
        raise Exception(f"""Spalte '{COLNAME_BEFUNDTEXT}' exisitiert nicht,
        aber CONTENT_IN_MULTIPLE_COLUMNS ist in config.py auch nicht True.
        Spaltennamen prüfen oder CONTENT_IN_MULTIPLE_COLUMNS auf True setzen.""")
    if CONTENT_IN_MULTIPLE_COLUMNS:
        columns_to_concat = [col for col in df_unfiltered.columns if col.startswith(MULTIPLE_CONTENT_COLS_PREFIX)]
        if len(columns_to_concat) == 0:
            raise Exception(
                f"CONTENT_IN_MULTIPLE_COLUMNS ist True, aber es existiert"
                + " keine Spalte mit '{MULTIPLE_CONTENT_COLS_PREFIX}'\n."
                + "Wert in config.py für MULTIPLE_CONTENT_COLS_PREFIX prüfen."
            )

        df_unfiltered[COLNAME_BEFUNDTEXT] = df_unfiltered[columns_to_concat].fillna("").agg("".join, axis=1).str.strip()

    df_unfiltered['has_keywords_in_befundtext'] = df_unfiltered[COLNAME_BEFUNDTEXT].apply(
        lambda x: check_report_for_keywords(x)
    )

    df_result = df_unfiltered[
        df_unfiltered['has_relevant_procedure']
        | df_unfiltered['has_keyword_in_procedure_title']
        | df_unfiltered['has_keywords_in_befundtext']
    ]

    return df_result


def main():
    # 1a. Import data
    if IMPORT_FILETYPE_IS_XLSX:
        df_all = merge_xlsx_files(EXPORTED_DATA_FOLDER_PATH)
    else:
        df_all = merge_csv_files(EXPORTED_DATA_FOLDER_PATH, IMPORT_SEPARATOR, IMPORT_ENCODING)

    # 2. filter for relevant tuples
    df_all_relevant = get_relevant_reports(df_all)
    print(f"There are {len(df_all)} unique reports per case. {len(df_all_relevant)} are relevant.")

    # 3. extract assessment part from CONTENT, by splitting at word 'Beurteilung:'
    df_all_relevant['has_assessment'] = np.where(
        df_all_relevant[COLNAME_BEFUNDTEXT].str.contains("Beurteilung:", na=False), 1, 0
    )
    df_all_relevant['assessment'] = np.where(
        df_all_relevant['has_assessment'] == 1,
        df_all_relevant[COLNAME_BEFUNDTEXT].str.split("Beurteilung:", n=1).str.get(1).str.strip(),
        ""
    )

    print(
        f"{df_all_relevant['has_assessment'].sum()} / {len(df_all_relevant)} ("
        + f"{round(df_all_relevant['has_assessment'].sum() * 100 / len(df_all_relevant), 1)}%)"
        + " cases with 'Beurteilung:' in CONTENT."
    )

    # 4. write relevant cases to csv
    if WRITE_TO_CSV:
        output_file = write_to_csv(
            df_all_relevant.filter(items=COLUMNS_IN_OUTPUT),
            OUTPUT_FILENAME,
            OUTPUT_FOLDER_PATH
        )
        print(f"Successfully written the output to '{output_file}'.")

if __name__ == "__main__":
    main()
