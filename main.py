#script principale

import json
from log_reader import load_logs_as_table
from log_analyzer import (
    extract_unique_users,
    extract_unique_events,
    count_events
)

def main():
    print("=== Analizzatore di log anonimizzati ===")

    # Input da utente con valori di default richiesti dalla specifica
    path_in = input("Percorso file JSON di input [default: logs.json]: ").strip()
    if path_in == "":
        path_in = "logs.json"

    path_out = input("Percorso file JSON di output [default: report.json]: ").strip()
    if path_out == "":
        path_out = "report.json"

    # Caricamento log nella Tabella2D_RO (BONUS)
    table = load_logs_as_table(path_in)

    # Stampa riassunto
    num_utenti = len(extract_unique_users(table))
    num_eventi = len(extract_unique_events(table))
    num_log = table.num_rows()

    print("\n=== STATISTICHE INIZIALI ===")
    print(f"* Utenti unici: {num_utenti}")
    print(f"* Eventi unici: {num_eventi}")
    print(f"* Log totali analizzati: {num_log}")
    print("============================\n")

    # Elaborazioni richieste
    utenti = extract_unique_users(table)
    eventi = extract_unique_events(table)
    conteggi = count_events(table)

    # Dizionario del report da salvare
    report = {
        "users": utenti,
        "events": eventi,
        "event_counts": conteggi
    }

    # Salvataggio su file JSON
    try:
        with open(path_out, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=4, ensure_ascii=False)
        print(f"Report generato correttamente in: {path_out}")

    except Exception as e:
        print("Errore durante il salvataggio del file di output:", str(e))


if __name__ == "__main__":
    main()