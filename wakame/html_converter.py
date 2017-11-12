# coding=utf-8
from docutils import core
from jinja2 import  Template

class HtmlConverter:
    def convert_to_html(self, rst_path, template_path):
        with open(rst_path, 'r') as f:
            rst = ''.join(f.readlines())
        with open(template_path, 'r') as f:
            template_str = ''.join(f.readlines())

        d = core.publish_parts(rst, writer_name='html5')
        template = Template(template_str)
        return template.render(d)

    def save_html(self, html, save_path):
        with open(save_path, 'w') as f:
            f.writelines(html)
