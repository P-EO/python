# -*- coding: utf-8 -*-
import os 
import os.path

class URL(object):
    P=[]

    def read(self, filename):
        with open(filename) as f:
            for line in f:
                field = line.split(',')
                company = field[1].replace(" ", '+')
                adress="{0}+{1}".format(field[5],field[11])
                self.P.append("http://www.companywebpage.com/market-search?q={0}".format(company))

    def company-site(self):
        for i in self.P:
            return i
