""" ----- DIE FOLGENDEN VARIABLEN MÜSSEN ANGEPASST WERDEN ----- """
""" A) Definition der exportierten Tabellen """
EXPORTED_DATA_FOLDER_PATH = "data_to_filter"
IMPORT_FILETYPE_IS_XLSX = False  # Falls False, wird CSV angenommen
IMPORT_SEPARATOR = ","  # Separator-Zeichen der exportierten CSVs
IMPORT_ENCODING = "utf-8"  # Encoding der exportierten CSVs

# Name der Spalte, in der die Befundtexte liegen:
COLNAME_BEFUNDTEXT = "CONTENT"

"""
Falls die Befundtexte auf mehrere Spalten aufgeteilt sind, muss
    1. CONTENT_IN_MULTIPLE_COLUMNS auf True gesetzt werden
    2. Bei MULTIPLE_CONTENT_COLS_PREFIX der Präfix der Spalten genannt werden
"""

# True, wenn die Befundtexte auf mehrere Spalten aufgeteilt sind:
CONTENT_IN_MULTIPLE_COLUMNS = True

# Allgemeiner Name der Spalten, die Teile des Befundtextes enthalten:
MULTIPLE_CONTENT_COLS_PREFIX = "Teil_"

# Name der Spalte, in der die Prozedur benannt ist
# (nur bei wenigen Befunden vorhanden):
COLNAME_PROZEDUR = "ZBEFALL04B"

# Entscheidet, ob das Ergebnis als CSV exportiert werden soll:
WRITE_TO_CSV = True

# Dateiname und Pfad der Ergebnis-CSV - ohne Dateiendung!
OUTPUT_FILENAME = "xlsx_test"
OUTPUT_FOLDER_PATH = "outputs"

# Spaltennamen, die in der exportierten CSV enthalten sein sollen:
COLUMNS_IN_OUTPUT = [
    "FALNR",
    "Jahr",
    "ORGFA",
    "ORGPF",
    "DOKNR",
    # "DOKVR",
    # "DOKTL",
    "ZBEFALL04B",
    # "ZBEFALL04D",
    # "DODAT",
    # "ERDAT",
    # "UPDAT",
    COLNAME_BEFUNDTEXT,
    "assessment"
]
