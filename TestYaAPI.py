import unittest
import YaAPI


class TestYaAPI(unittest.TestCase):

    def test_create_directory_not_exist(self):
        self.assertEqual(YaAPI.create_directory('New'), {'href': 'https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2FNew', 'method': 'GET', 'templated': False})

    def test_create_directory_exist(self):
        self.assertEqual(YaAPI.create_directory('New'), {'message': 'По указанному пути "New" уже существует папка с таким именем.', 'description': 'Specified path "New" points to existent directory.', 'error': 'DiskPathPointsToExistentDirectoryError'})
