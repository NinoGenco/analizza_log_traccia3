#caricamento JSON + validazione + Tabella2D_RO

import json
from utilities.griglia_liste_RO import Tabella2D_RO


def load_logs_as_table(path: str) -> Tabella2D_RO:

    """ Carica un file JSON contenente una lista di log (ognuno con 8 campi)
    e restituisce una Tabella2D_RO basata sui dati caricati.

    Parametri:
        path: percorso del file JSON di input.

    Ritorno:
        Tabella2D_RO contenente i log.

    Eccezioni:
        FileNotFoundError se il file non esiste.
        JSONDecodeError se il contenuto non è un JSON valido.
        ValueError se il JSON non contiene una lista. """

    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if not isinstance(data, list):
            raise ValueError("Il file JSON deve contenere una lista di log.")

        return Tabella2D_RO(data)

    except FileNotFoundError:
        print(f"Errore: il file '{path}' non è stato trovato.")
        raise
    except json.JSONDecodeError:
        print("Errore: il file JSON è malformato.")
        raise