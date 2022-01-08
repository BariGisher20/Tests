from prev_hw import people, shelf, add_doc_to_catalog, add_doc_to_shelf


class TestPytest:

    def test_people(self):
        assert people("2207 876234") == 'Василий Гупкин'

    def test_shelf(self):
        assert shelf("2207 876234") == '1'

    def test_add_doc_to_catalog_already_exist(self):
        assert add_doc_to_catalog("passport", "2207 876234", "Василий Гупкин") == 'Такой человек уже есть в каталоге!'

    def test_add_doc_to_catalog_new(self):
        assert add_doc_to_catalog('pass', '22', 'Туманян') == [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'}, {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'}, {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}, {'type': 'pass', 'number': '22', 'name': 'Туманян'}]

    def test_add_doc_to_shelf_directories(self):
        assert add_doc_to_shelf('54', '3', 'pass', 'Туманян') == {'1': ['2207 876234', '11-2'], '2': ['10006'], '3': ['54']}

    def test_add_doc_to_shelf_documents(self):
        assert add_doc_to_shelf('54', '3', 'pass', 'Туманян') == [{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'}, {'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'}, {'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}, {'type': 'pass', 'number': '54', 'name': 'Туманян'}]


