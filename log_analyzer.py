#funzioni di anilisi del log

def extract_unique_users(table) -> list:

    """ Estrae tutti gli utenti unici dalla tabella dei log.

    Parametri:
        table: Tabella2D_RO contenente i log.

    Ritorno:
        Una lista ordinata degli utenti unici. """

    users = set()

    for r in range(table.num_rows()):
        user = table.get(r, 1)  # colonna 1: identificativo utente
        users.add(user)

    return sorted(users)


def extract_unique_events(table) -> list:

    """ Estrae tutti gli eventi diversi presenti nei log.

    Parametri:
        table: Tabella2D_RO contenente i log.

    Ritorno:
        Lista ordinata degli eventi unici. """

    events = set()

    for r in range(table.num_rows()):
        event = table.get(r, 4)  # colonna 4: evento
        events.add(event)

    return sorted(events)


def count_events(table) -> dict:

    """ Conta quante volte compare ciascun evento.

    Parametri:
        table: Tabella2D_RO contenente i log.

    Ritorno:
        Dizionario {evento: conteggio}. """

    counts = {}

    for r in range(table.num_rows()):
        event = table.get(r, 4)
        counts[event] = counts.get(event, 0) + 1

    return counts