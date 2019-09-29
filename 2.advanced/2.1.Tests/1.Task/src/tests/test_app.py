import unittest
import json
import app
from mock import patch

documents = []
directories = {}


def setUpModule():
    with open('../fixtures/documents.json', 'r', encoding='utf-8') as out_docs:
        documents.extend(json.load(out_docs))
    with open('../fixtures/directories.json', 'r', encoding='utf-8') as out_dirs:
        directories.update(json.load(out_dirs))


@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class TestAppDocs(unittest.TestCase):

    def test_check_document_existance(self):
        user_doc_number = '2207 876234'
        app.check_document_existance(user_doc_number=user_doc_number)
        self.assertTrue(user_doc_number)

    def test_get_doc_owner_name(self):
        with patch('app.input', return_value='10006'):
            self.assertEqual(app.get_doc_owner_name(), 'Аристарх Павлов')

    def test_get_all_doc_owners_names(self):
        self.assertIsInstance(app.get_all_doc_owners_names(), set)
        self.assertEqual(len(app.get_all_doc_owners_names()), len(documents))

    def test_remove_doc_from_shelf(self):
        doc_number = '11-2'
        app.remove_doc_from_shelf(doc_number=doc_number)
        self.assertTrue(doc_number)

    def test_add_new_shelf(self):
        with patch('app.input', return_value='5') as _:
            self.assertTrue(app.add_new_shelf())

    def test_append_doc_to_shelf(self):
        doc_number = '23322'
        shelf_number = '1'
        app.append_doc_to_shelf(doc_number=doc_number, shelf_number=shelf_number)
        self.assertIn(doc_number, directories[shelf_number])

    def test_delete_doc(self):
        with patch('app.input', return_value='11-2') as _:
            self.assertTrue(app.delete_doc())

    def test_get_doc_shelf(self):
        with patch('app.input', return_value='2207 876234') as _:
            self.assertEqual(app.get_doc_shelf(), '1')

    def test_move_doc_to_shelf(self):
        with patch('app.input', return_value='2207 876234') as _:

    if __name__ == '__main__':
        unittest.main()
