# coding=utf-8
from unittest import TestCase
from wakame.html_converter import HtmlConverter

class TestHtmlConverter(TestCase):
    def test_convert_to_html(self):
        hc = HtmlConverter()
        with open('test_files/test1.html', 'r') as f:
            html = ''.join(f.readlines())
        self.assertEqual(html, hc.convert_to_html('test_files/test1.rst', '../templates/article_template.html'))
