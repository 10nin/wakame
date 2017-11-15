# coding=utf-8
from unittest import TestCase
from wakame.file_manager import FileManager


class TestFileManager(TestCase):
    def setUp(self):
        self.fm = FileManager()
        self.test_file_path = {'test1': 'test_files/test1.rst'}

    def test_get_hash_for_test1(self):
        self.assertEqual('F7A17082FFBBFBBE6A6B4474EF7C6045B3F6D009', self.fm.get_hash(self.test_file_path['test1']))

    def test_get_hash_for_none_exists_file(self):
        with self.assertRaises(OSError):
            self.fm.get_hash('')

    def test_get_file_name_without_extension(self):
        key = 'test1'
        self.assertEqual(key, self.fm.get_basename(self.test_file_path[key]))

    def test_get_files(self):
        target_dir = 'test_files'
        ext = 'rst'
        expect = ['test1.rst', 'directive_test1.rst']
        ans = self.fm.get_files(target_dir, ext)
        for elm in ans:
            self.assertTrue(elm in expect)
