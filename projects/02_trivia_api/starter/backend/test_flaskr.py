import os
import unittest
import json
# import inspect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import ProgrammingError,DBAPIError
from flaskr import create_app
from models import setup_db, Question, Category, database_path
from psycopg2.errors import UndefinedColumn


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client

        self.database_path = database_path.replace('trivia', 'trivia_test')
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            print("check tables before test", self.db.engine.table_names())
            # self.drop_all()
            self.db.create_all()
            print("check tables after test", self.db.engine.table_names())
    
    def tearDown(self):
        """Executed after reach test"""
        # self.db.session.remove()
        # self.db.drop_all()


    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_homepage(self):
        res = self.client().get('/')
        
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Hello, World!', res.data)
    def test_405_post_homepage(self):
        res = self.client().post('/', json={'question': 'Is this working?'})
        
        self.assertEqual(res.status_code, 405)
        self.assertIn(b'not allowed', res.data)

    def test_select_questions(self):
        stmt_sel_all_questions = text('select * from questions;')
        with self.app.app_context():           
            result = self.db.engine.execute(stmt_sel_all_questions)
        
        rows = [row for row in result]
        self.assertTrue(rows)
        if rows:
            self.assertEqual(rows[0][0], int(5))
    def test_column_category_name(self):
        def execute_sel_category_name():
            stmt_sel_name_categories = text('select name from categories;')
            with self.app.app_context():
                try:
                    return self.db.engine.execute(stmt_sel_name_categories)
                except DBAPIError as e:
                    if e.orig.pgcode == '42703':#source: https://www.psycopg.org/docs/errors.html#sqlstate-exception-classes
                        # raise Exception("Does not work")
                        return None
        # self.assertRaises(ProgrammingError, execute_sel_category_name())
        # self.assertRaises(UndefinedColumn, execute_sel_category_name())
        # self.assertRaises(Exception("Does not work"), execute_sel_category_name())
        self.assertIsNone(execute_sel_category_name())
        



# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()