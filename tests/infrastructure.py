import unittest

from database import run_query
from settings import DATABASE_NAME, DATABASE_USER, DATABASE_PASS


class TestDatabaseExists(unittest.TestCase):

    def test_psycopg2_is_installed(self):
        try:
            import psycopg2
        except Exception as e:
            self.fail(e)

    def test_stats_database_exists(self):
        import psycopg2
        dbname = DATABASE_NAME
        dbuser = DATABASE_USER
        dbpass = DATABASE_PASS

        try:
            conn = psycopg2.connect("dbname={} user={} password={}".format(
                dbname, dbuser, dbpass))
        except Exception as e:
            self.fail(e)

    def test_posts_table_in_stats_database_has_non_zero_count(self):
        count = int(run_query("select count(*) from posts")[0][0])
        self.assertGreater(count, 0)

class TestSklearn(unittest.TestCase):
    def test_sklearn_is_installed(self):
        import sklearn
        self.assertTrue('If it gets to here, the import worked')

class TestIpdb(unittest.TestCase):
    def test_ipdb_is_installed(self):
        import ipdb
        self.assertTrue('If it gets to here, the import worked')
