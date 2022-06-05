import sqlite3


class HandleDB():
    def __init__(self):
        self._con = sqlite3.connect("anime_notifications.db")
        self._cur = self._con.cursor()

    def get_data(self) -> int:
        self._cur.execute("SELECT send FROM email")
        data = self._cur.fetchone()
        return data[0]

    def update_data(self, value: int) -> None:
        self._cur.execute("UPDATE email SET send = %i WHERE send = 0 OR send = 1" % value)
        self._con.commit()

    def __del__(self):
        self._con.close()

