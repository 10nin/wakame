# coding=utf-8
import os
from pathlib import Path
from unittest import TestCase
from wakame.html_converter import HtmlConverter


class TestHtmlConverter(TestCase):
    def test_convert_to_html(self):
        hc = HtmlConverter()
        with open('test_files/test1.html', 'r') as f:
            html = ''.join(f.readlines())
        self.assertEqual(html, hc.convert_to_html('test_files/test1.rst', '../templates/article_template.html'))

    def test_save_html(self):
        hc = HtmlConverter()
        p = 'test_files/test1.html'
        html = hc.convert_to_html('test_files/test1.rst', '../templates/article_template.html')
        hc.save_html(html, p)
        self.assertTrue(Path(p).exists())
        os.remove(p)
