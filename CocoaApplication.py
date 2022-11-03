from ctypes import c_void_p

from Lib import LibMango


class CocoaApplication(object):
    def __init__(self):
        LibMango.CocoaApplication_create.argtypes = []
        LibMango.CocoaApplication_create.restype = c_void_p

        LibMango.CocoaApplication_run.argtypes = [c_void_p]
        LibMango.CocoaApplication_run.restype = c_void_p

        self.obj = LibMango.CocoaApplication_create()

    def run(self) -> None:
        LibMango.CocoaApplication_run(self.obj)
