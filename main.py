import os.path
import sqlite3
import notifications as ntf


if not os.path.exists('p_database.db'):
    ntf.n_warning("Database not detected. Creating...")

    conn = sqlite3.connect('p_database.db')

    ntf.n_success("Database created.")

else:
    ntf.n_success("Database detected.")
