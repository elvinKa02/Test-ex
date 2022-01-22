import re

import eel
import sqlite3

with sqlite3.connect('db.db') as conn:
    c = conn.cursor()


@eel.expose
def check_in_db(ser_num):
    c.execute("SELECT * FROM EQP WHERE ser_num = ?", (ser_num,))
    check = c.fetchone()
    if check is None and len(ser_num) == 10:
        if re.search(r"^[0-9A-Z]{2}[A-Z]{5}[0-9A-Z][A-Z]{2}$", ser_num):
            c.execute("INSERT or IGNORE INTO EQP VALUES(?, ?, ?)", [None, 1, ser_num])
            conn.commit()
            return 'Успешно: этот серийный номер записан к 1 типу оборудования'

        elif re.search(r"^[0-9][0-9A-Z]{2}[A-Z]{2}[0-9A-Z][-_@][0-9A-Z][a-z]{2}$", ser_num):
            c.execute("INSERT or IGNORE INTO EQP VALUES(?, ?, ?)", [None, 2, ser_num])
            conn.commit()
            return 'Успешно: этот серийный номер записан ко 2 типу оборудования'

        elif re.search(r"^[0-9][0-9A-Z]{2}[A-Z]{2}[0-9A-Z][-_@][0-9A-Z]{3}$", ser_num):
            c.execute("INSERT or IGNORE INTO EQP VALUES(?, ?, ?)", [None, 3, ser_num])
            conn.commit()
            return 'Успешно: этот серийный номер записан к 3 типу оборудования'

        else:
            return 'Предупреждение: проверьте написанное'

    else:
        return 'Ошибка: данный серийный номер уже есть или не той длины'


eel.init('web')
eel.start('web.html', size=(500, 350))
