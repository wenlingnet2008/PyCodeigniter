#!/usr/bin/env python
# -*- coding:utf8 -*-
__author__ = 'xiaozhang'


from codeigniter.system.core.CI_Application import CI_Application

class Index:

    def __init__(self,abc=0, *args, **kwargs):
        pass
        self.model= self.app.loader.model('IndexModel')



    def index(self):
        return "hello world"

    def search(self):
        return  self.model.search()

    def insert(self):
       return  self.model.insert()

    def upate(self):
        return  self.model.upate()

    def delete(self):
        return  self.model.delete()

