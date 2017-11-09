# coding=utf-8
from unittest import TestCase
from wakame.file_manager import FileManager


class TestFileManager(TestCase):
    def test_get_hash_for_test1(self):
        fm = FileManager()
        self.assertEqual('F7A17082FFBBFBBE6A6B4474EF7C6045B3F6D009', fm.get_hash('test_files/test1.rst'))
