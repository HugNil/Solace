import unittest
from log_writer import Log_writer  # type: ignore
import os
import datetime


class TestLog_writer(unittest.TestCase):
    def setUp(self):
        self.log_writer = Log_writer()

    def test_init(self):
        self.assertEqual(self.log_writer.log_file, 'log.txt')
        self.assertTrue(os.path.exists('log.txt'))

    def test_init_file_not_exists(self):
        os.remove('log.txt')
        self.log_writer = Log_writer()
        self.assertTrue(os.path.exists('log.txt'))

    def test_log(self):
        self.log_writer.log('test')
        with open('log.txt', 'r') as log:
            lines = log.readlines()
            self.assertTrue(lines[-1].startswith(
                datetime.datetime.now().strftime("%m-%d %H:%M:%S")))

    def test_clear_log(self):
        self.log_writer.clear_log()
        with open('log.txt', 'r') as log:
            lines = log.readlines()
            self.assertEqual(len(lines), 0)
