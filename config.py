""" ----- DIE FOLGENDEN VARIABLEN MÜSSEN ANGEPASST WERDEN ----- """
""" A) Definition der exportierten Tabellen """
EXPORTED_DATA_FILENAMES = [
    # Hier die Dateinamen bzw. -pfade der exportierten CSV-Dateien auflisten:
    # "datei-1.csv",
    # "datei-2.csv"
    "PMD_RAD_Befunde_2021.csv"
]
IMPORT_SEPERATOR = "," # Separator-Zeichen der exportierten CSVs
IMPORT_ENCODING = "utf_8" # Encoding der exportierten CSVs

COLNAME_BEFUNDTEXT = "CONTENT" # Name der Spalte, in der die Befundtexte liegen

"""
Falls die Befundtexte auf mehrere Spalten aufgeteilt sind, muss
    1. CONTENT_IN_MULTIPLE_COLUMNS auf True gesetzt werden
    2. Bei MULTIPLE_CONTENT_COLS_PREFIX der Präfix der Spalten genannt werden
"""
CONTENT_IN_MULTIPLE_COLUMNS = True # Auf True stellen, wenn die Befundtexte auf mehrere Spalten aufgeteilt sind
MULTIPLE_CONTENT_COLS_PREFIX = "Teil_" # Allgemeiner Name der Spalten, die Teile des Befundtextes enthalten
COLNAME_PROZEDUR = "ZBEFALL04B" # Vermutlich ZBEFALL04B - Name der Spalte, in der die Prozedur benannt ist (nur bei wenigen Befunden vorhanden).

KEYWORD_LISTS = [
    ["ct", "computertomographie", "computertomografie", "spiral", "polytrauma", "PET", "positronenemission"],
    ["km", "kontrastmittel", "PET", "positronenemission"],
    ["thorax", "koerperstamm", "körperstamm", "pulm", "lunge", "aorta", "spiral", "polytrauma", "PET", "positronenemission"]
]

WRITE_TO_CSV = True # Entscheidet, ob das Ergebnis als CSV exportiert werden soll
OUTPUT_FILENAME = "PMD_RAD_Befunde_2022_filtered" # Dateiname der Ergebnis-CSV - ohne Dateiendung!
COLUMNS_IN_OUTPUT = [ # Spaltennamen, die in der exportierten CSV enthalten sein sollen
    'FALNR',
    'Jahr',
    'ORGFA',
    'ORGPF',
    'DOKNR',
    # 'DOKVR',
    # 'DOKTL',
    'ZBEFALL04B',
    # 'ZBEFALL04D',
    # 'DODAT',
    # 'ERDAT',
    # 'UPDAT',
    COLNAME_BEFUNDTEXT,
    'assessment'
]