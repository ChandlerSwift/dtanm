import filecmp
import time


def are_dirs_same(a, b, ignore=None):
    if ignore is None:
        ignore = []
    r = filecmp.dircmp(a, b, ignore)
    return r.right_only == r.left_only == r.diff_files == []


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, *args):
        self.end = time.perf_counter()
        self.interval = self.end - self.start
