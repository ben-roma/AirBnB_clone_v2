import unittest
import MySQLdb
from config import db_config


class TestCreateState(unittest.TestCase):
    def setUp(self):
        """Connect to the database and create a cursor."""
        self.db = MySQLdb.connect(host=db_config['host'],
                                  user=db_config['user'],
                                  passwd=db_config['passwd'],
                                  db=db_config['db'])
        self.cursor = self.db.cursor()

    def test_create_state(self):
        """Test adding a new state to the database."""
        # Get the number of current records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count_before = self.cursor.fetchone()[0]

        # Execute the console command or function to add a new state
        self.cursor.execute("INSERT INTO states (name) VALUES ('California')")

        # Get the new number of records in the states table
        self.cursor.execute("SELECT COUNT(*) FROM states")
        count_after = self.cursor.fetchone()[0]

        # Check if the count increased by 1
        self.assertEqual(count_after, count_before + 1,
                         "Failed to add a new state.")

    def tearDown(self):
        """Roll back any changes and close the connection."""
        self.db.rollback()
        self.cursor.close()
        self.db.close()


if __name__ == '__main__':
    unittest.main()
