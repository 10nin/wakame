# coding=utf-8

from hashlib import sha1


class FileManager:

    def get_hash(self, file_path):
        with open(file_path, 'r') as f:
            dat = (''.join(f.readlines()))
        h = sha1()
        h.update(dat.encode('utf-8'))
        return h.hexdigest().upper()
