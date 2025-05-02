import sys
import os
import unittest
import datetime

# Fixes errors on vscode when it comes to running from current working directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.db_util import database_init, add_user, get_info, connection_init, delete_user, get_id, update_info

class Test_DB_Utils(unittest.TestCase):
    def test_01_database_init(self):
        self.assertIn(database_init(), [True, False])
    
    def test_02_add_user(self):
        id = add_user("email.com", "password", "Gordon A. Ramsay", "2012-05-19")
        self.assertIsNotNone(get_info(id, "email"))
        
    def test_03_get_id(self):
        self.assertIsNotNone(get_id("email.com"))
    
    def test_04_get_info(self):
        id = get_id("email.com")
        self.assertDictEqual(get_info(id, "email"), {"email": "email.com"})
    
    def test_05_update_info(self):
        id = get_id("email.com")
        update_info(id, name="Gordon", birthdate="2012-05-20", hash="hello")
        self.assertDictEqual(get_info(id, "name", "birthdate", "hash"), {"name": "Gordon", "birthdate": datetime.date(2012, 5, 20), "hash": "hello"})
    
    def test_06_delete_user(self):
        id = get_id("email.com")
        delete_user(id)
        self.assertIsNone(get_info(id, "email"))
        

if __name__ == "__main__":
    cnx = connection_init()
    cursor = cnx.cursor()
    unittest.main(verbosity=2)
    cursor.close()
    cnx.cmd_quit()