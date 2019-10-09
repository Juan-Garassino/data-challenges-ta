# pylint: disable-all

import unittest
from bs4 import BeautifulSoup

class Users(unittest.TestCase):

#1 in the good folders

#2 should have a survey table
    def test_surveys_table_exists(self):
        with open('surveys.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('surveys' in t, True)

#2' should have user_id, foreign_key?
    def test_surveys_should_have_the_correct_fields(self):
        with open('surveys.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "surveys"})
        for row in table[0].find_all('row'):
            self.assertEqual(row.get('name') in ['user_id', 'title', 'id'], True)

#3 should have a question table
    def test_questions_table_exists(self):
        with open('surveys.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('questions' in t, True)

#3' should have survey_id, foreign_key
    def test_questions_should_have_the_correct_fields(self):
        with open('surveys.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "questions"})
        for row in table[0].find_all('row'):
            self.assertEqual(row.get('name') in ['survey_id', 'text', 'id'], True)

#4 should have an anwser table
    def test_answers_table_exists(self):
        with open('surveys.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('answers' in t, True)

#4' should have anwser_id, foreign_key
    def test_answers_should_have_the_correct_fields(self):
        with open('surveys.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "answers"})
        for row in table[0].find_all('row'):
            self.assertEqual(row.get('name') in ['question_id', 'text', 'id'], True)

#5 should havee a user table
    def test_users_table_exists(self):
        with open('surveys.xml', 'r') as file:
          data = file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        tables = soup.find_all('table')
        t = []
        for table in tables:
           t.append(table['name'])
        self.assertEqual('users' in t, True)

    def test_users_should_have_the_correct_fields(self):
        with open('surveys.xml', 'r') as file:
            data= file.read().replace('\n', '')
        soup = BeautifulSoup(data, 'xml')
        table = soup.find_all('table', attrs={"name": "users"})
        for row in table[0].find_all('row'):
            self.assertEqual(row.get('name') in ['id'], True)




