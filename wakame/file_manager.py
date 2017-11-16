# coding=utf-8

from hashlib import sha1
from os import path
from pathlib import Path

class FileManager:

    def get_files(self, target_dir, ext):
        return [str(e) for e in Path(target_dir).glob('*.' + ext)]

    def get_hash(self, file_path):
        with open(file_path, 'r') as f:
            h = sha1()
            h.update(''.join(f.readlines()).encode('utf-8'))
        return h.hexdigest().upper()

    def get_basename(self, file_path):
        p = path.basename(file_path)
        for e in Path(p).suffixes:
            p = p.replace(e, '')
        return p
