# coding: utf8

from unittest import TestCase
from unittest.mock import patch

from monorequire.filelock import FileLock


class FileLockTest(TestCase):
    def test_should_set_lock_path_at_resource_dir_default(self):
        filelock = FileLock(
            "/home/yyx/test/resource.file", None, None,
            None, None, None, 1, 0.01, "."
        )
        self.assertEqual(filelock.lock, "/home/yyx/test/.resource.file.lock")

    @patch("monorequire.filelock.path")
    def test_should_set_lock_path_at_resource_dir_default_use_relative_path(
            self, path_mock
    ):
        path_mock.dirname.return_value = "/home/yyx/test/"

        filelock = FileLock(
            "resource.file", None, None,
            None, None, None, 1, 0.01, "."
        )
        self.assertEqual(filelock.get_lock_path("."), "/home/yyx/test/")
