import os
import sys


class MsgOutput:
    init = False

    @classmethod
    def file_init(cls, file_path):
        if not os.path.exists(file_path):
            with open(file_path, 'w'):
                ...
            cls.init = True

    @classmethod
    def output(cls, msg, mode='a', path=None, filename='test_tool_opt.txt', enc='utf-8'):
        """
        msg: message to output
        mode: mode to open txt file
        path: path to create txt file
        filename: name of txt file, make sure it's not a existed file name
        enc: encoding for open
        """
        if path is None:
            path = os.getcwd()

        ttl_path = os.path.join(path, filename)

        if not cls.init:
            cls.file_init(ttl_path)

        with open(ttl_path, mode, encoding=enc) as f:
            print(msg, file=f)


opt = MsgOutput.output
