Zur Nutzung dieses Projekts einfach
1. `config_template.py` duplizieren und zu `config.py` umbenennen (wird via `.gitignore` gefiltert).
2. In der `config.py` die relevanten Konstanten, insbesondere die Pfade zu den CSVs, befüllen.
    
    ⚠️ **WICHTIG!** Falls die Befundtexte auf mehrere Spalten aufgeteilt sind, muss in `config.py`:
   1. der Wert für `CONTENT_IN_MULTIPLE_COLUMNS = True` sein
   2. das Präfix der Befundtextspalten in `MULTIPLE_CONTENT_COLS_PREFIX` genannt werden.
2. die Datei `filterForRelevantProcedures.py` ausführen.