class LegacyRouter(object):
    """
    A router to control all database operations on models in the
    importer application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read importer models go to importer_db.
        """
        if model._meta.app_label == 'importer':
            return 'legacy'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write importer models go to legacy.
        """
        if model._meta.app_label == 'importer':
            return 'legacy'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the importer app is involved.
        """
        if (obj1._meta.app_label == 'importer' or
                obj2._meta.app_label == 'importer'):
            return True
        return None

    def allow_migrate(self, db, app_label, model=None, **hints):
        """
        Make sure the importer app only appears in the 'legacy'
        database.
        """
        if app_label == 'importer':
            return False
        return None
