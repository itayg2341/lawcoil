from django.core.management.base import BaseCommand
from django.db import connection


class BaseImportCommand(BaseCommand):

    def clear_tables(self, cascade=False):
        "Truncate (via SQL) the tables"
        self.stdout.write('- Clearing tables')
        cursor = connection.cursor()
        statement = 'TRUNCATE %s'
        if cascade:
            statement += ' CASCADE'
        cursor.execute(statement % ','.join(self.TABLES))

    def reset_sequences(self):
        "Reset PG sequences related to the tables"
        self.stdout.write('- Resetting db sequences')
        cursor = connection.cursor()

        sql = """SELECT setval(pg_get_serial_sequence('"%s"','id'),
                 coalesce(max("id"), 1), max("id") IS NOT null)
                 FROM "%s";"""

        for t in self.TABLES:
            cursor.execute(sql % (t, t))
