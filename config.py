""" ----- DIE FOLGENDEN VARIABLEN MÜSSEN ANGEPASST WERDEN ----- """
RAD_REPORTS_FILENAMES = [
    # Hier die Dateinamen bzw. -pfade der exportierten CSV-Dateien auflisten:
    # "datei-1.csv",
    # "datei-2.csv"
]
IMPORT_SEPERATOR = "," # Separator-Zeichen der zu importierenden CSVs
IMPORT_ENCODING = "utf_8" # Encoding der zu importierenden CSVs

COLNAME_BEFUNDTEXT = "" # Name der Spalte, in der die Befundtexte liegen
COLNAME_PROZEDUR = "" # Name der Spalte, in der die Prozedur benannt ist (nur bei wenigen Befunden vorhanden).

WRITE_TO_CSV = True # True, if the final dataframe should be written to CSV
OUTPUT_FILENAME = "PMD_RAD_Befunde_2022_filtered" # output filename; file ending and timestamp will be added automatically
COLUMNS_IN_OUTPUT = [ # Defines the columns that should be included in output
    # 'FALNR',
    # 'Jahr',
    # 'ORGFA',
    # 'ORGPF',
    # 'DOKNR',
    # 'DOKVR',
    # 'DOKTL',
    # 'ZBEFALL04B',
    # 'ZBEFALL04D',
    # 'DODAT',
    # 'ERDAT',
    # 'UPDAT',
    # 'CONTENT',
    'assessment'
]