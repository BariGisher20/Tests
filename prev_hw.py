
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(doc_num):
    res = 'Данные не найдены!'
    for doc in documents:
        if doc['number'] == doc_num:
            res = doc['name']
            return res


def shelf(doc_num):
    res = 'Данные не найдены!'
    for shelf_num, pass_nums in directories.items():
        if doc_num in pass_nums:
            res = shelf_num
            return res


def list_():
    for document in documents:
        return f'passport "{document["number"]}" "{document["name"]}"'


def add_doc_to_catalog(doc_type, doc_num, name):
    is_present = True
    for document in documents:
        if document['number'] != doc_num and document['name'] != name:
            is_present = False
            documents.append({"type": doc_type, "number": doc_num, "name": name})
            return documents
        else:
            return 'Такой человек уже есть в каталоге!'


def add_doc_to_shelf(doc_num, shelf_num_income, doc_type, name):
    # номера на полках существующие
    existed_nums = []
    for doc_numbers in directories.values():
        existed_nums.extend(doc_numbers)
        # закончилась логика
    if shelf_num_income in directories:
        for shelf_num, doc_numbers in directories.items():
            existed_doc_numbers = existed_nums
            if shelf_num == shelf_num_income:
                if doc_num not in existed_doc_numbers:
                    directories.setdefault(shelf_num_income, doc_num)
                    doc_numbers.append(doc_num)
                    documents.append({"type": doc_type, "number": doc_num, "name": name})
                    return documents
    else:
        return 'Такой полки не существует'

