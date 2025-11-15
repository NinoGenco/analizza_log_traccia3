#classe Tabella2D_RO

from copy import deepcopy

class Tabella2D_RO:

    """ Rappresenta una tabella bidimensionale ad accesso sola lettura.
    I dati vengono copiati internamente così da impedire modifiche
    esterne. Le informazioni sono mantenute sia per righe che per
    colonne per facilitare l'accesso. """

    def __init__(self, matrice: list[list[object]]):

        """ Inizializza la tabella a partire da una lista di liste.

        Parametri
        ----------
        matrice : list[list[object]]
            Matrice iniziale organizzata per righe. """

        # Copia difensiva per evitare modifiche esterne
        self._righe = deepcopy(matrice)

        # Preparazione delle colonne tramite trasposizione
        self._colonne = []
        if self._righe and len(self._righe[0]) > 0:
            numero_colonne = len(self._righe[0])
            for c in range(numero_colonne):
                colonna = [self._righe[r][c] for r in range(len(self._righe))]
                self._colonne.append(colonna)

    # ---------------------------------------------------------
    #  METODI DI DIMENSIONE
    # ---------------------------------------------------------

    def size(self) -> tuple[int, int]:
        """
        Restituisce una tupla contenente:
        (numero_righe, numero_colonne)
        """
        return len(self._righe), (len(self._righe[0]) if self._righe else 0)

    def num_rows(self) -> int:
        """
        Restituisce il numero di righe.
        Metodo compatibile con gli esercizi del docente.
        """
        return len(self._righe)

    def num_cols(self) -> int:
        """
        Restituisce il numero di colonne.
        Metodo compatibile con gli esercizi del docente.
        """
        return len(self._righe[0]) if self._righe else 0

    # ---------------------------------------------------------
    #  ACCESSO AI DATI
    # ---------------------------------------------------------

    def get_cell(self, r: int, c: int) -> object:
        """
        Ritorna il valore nella cella di coordinate (r, c).
        """
        return self._righe[r][c]

    def get(self, r: int, c: int) -> object:
        """
        Alias di get_cell(r, c).
        Introdotto per mantenere compatibilità con il codice
        che utilizza la versione originale della tabella.
        """
        return self.get_cell(r, c)

    def get_riga(self, r: int) -> list[object]:
        """
        Restituisce una copia della riga r-esima.
        """
        return list(self._righe[r])

    def get_colonna(self, c: int) -> list[object]:
        """
        Restituisce una copia della colonna c-esima.
        """
        return list(self._colonne[c])


# ---------------------------------------------------------
#  TEST
# ---------------------------------------------------------
if __name__ == "__main__":
    esempio = Tabella2D_RO([[1, 2, 3], [4, 5, 6]])
    print("Dimensioni:", esempio.size())
    print("Righe:", esempio.num_rows())
    print("Colonne:", esempio.num_cols())
    print("Cella (1,2):", esempio.get(1, 2))
    print("Riga 1:", esempio.get_riga(1))
    print("Colonna 0:", esempio.get_colonna(0))