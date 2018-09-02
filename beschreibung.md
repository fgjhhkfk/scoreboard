Anzeigetafel fuer einen Spielstand
Farbe der Tafel individuell einstellbar
Knopf zum hoch und herunterzaehlen
Knopf zum schreiben des Ergebnisses in eine Datenbank
    - Tore spieler 1
    - Tore Spieler 2
    - Datum + Uhrzeit
Spieler Hinzufuegen
Link zu einer Statistikseite

Datenbank:
Eine Tabelle mit Spielern zuerst erstellen
    Username text, Spielfarbe text
    Bild?
    CREATE TABLE users(userid INTEGER PRIMARY KEY,
                       username TEXT,
                       color TEXT);
Eine Tabelle mit den Ergebnissen (s.o.)
    CREATE TABLE scores(gameid INTEGER PRIMARY KEY,
                        player1 TEXT,
                        player2 TEXT,
                        goals1 INTEGER,
                        goals2 INTEGER,
                        date BLOB,
                        FOREIGN KEY (player1) REFERENCES users(userid),
                        FOREIGN KEY (player2) REFERENCES users(userid));
