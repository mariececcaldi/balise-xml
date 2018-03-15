#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

import re
import os, sys

#./extract_xml_tags <Fichier.xml>

def extract_xml_tags(file_in):
    file_out = '%s_tags.xml' %re.sub('\.xml', "", file_in)
    f = open(file_in, "r")
    d = open('output.xml','w')
    for line in f:
        line2 = re.sub('>',        "> \n", line)
        line3 = re.sub('</',       "\n</", line2)
        line4 = re.sub(' ',        "",     line3)
        print >>d, line4
    f.close()
    d.close()
    
    f1 = open('output.xml','r')
    d1 = open(file_out,'w')
    
    for line in f1:
        if  re.search('<', line):
            print >>d1, line
    f1.close()
    d1.close()
    os.remove('output.xml')
    

if len(sys.argv) == 2:
    if os.path.isfile(sys.argv[1]):
        extract_xml_tags(sys.argv[1])
    else:
        print 'le fichier xml n''existe pas'
else:
     print 'utilisation du script: python extract_xml_tags.py <Fichier.xml>'


