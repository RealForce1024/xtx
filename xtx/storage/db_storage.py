#!/usr/bin/env python
# -*- coding: utf-8  -*-

import os.path

class DbStorage(Storage):

    def __init__(self, filepath = None):
        super().__init__()

    def create(self, force = False):
        pass
