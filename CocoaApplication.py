import ctypes

from Lib import LibMango


class CocoaApplication(object):
    def __init__(self):
        LibMango.CocoaApplication_create.argtypes = []
        LibMango.CocoaApplication_create.restype = ctypes.c_void_p

        LibMango.CocoaApplication_run.argtypes = [ctypes.c_void_p]
        LibMango.CocoaApplication_run.restype = ctypes.c_void_p

        self.obj = LibMango.CocoaApplication_create()

    def run(self) -> None:
        LibMango.CocoaApplication_run(self.obj)
