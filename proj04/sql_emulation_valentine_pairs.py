import sqlite3
def get_crushes(database_filename):
    conn = sqlite3.connect(database_filename)
    c = conn.cursor()
    return_list = []
    for row in c.execute("""SELECT crusher_name, name FROM (SELECT name AS crusher_name, crushed_on FROM names
                     LEFT OUTER JOIN crushed
                     ON id = crusher) INNER JOIN names WHERE crushed_on = id
                    UNION SELECT name, NULL FROM names WHERE id NOT IN (SELECT crusher FROM crushed)
                    ORDER BY crusher_name, name;
"""):
        if row[1] is None:
            return_list.append(row[0] + ' has a crush on nobody')
        else:
            return_list.append(row[0] + ' has a crush on ' + row[1])
    conn.commit()
    conn.close()
    return return_list