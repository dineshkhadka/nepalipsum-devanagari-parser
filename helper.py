#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys,re

infile, outfile = sys.argv[1], sys.argv[2]

def parseNepali(inputFile = infile, outputFile = outfile):
    output = open(inputFile, 'r', encoding='utf8')
    content = output.read()
    output.close()
    content = re.sub(r''' । |।|[०१२३४५६७८९:;,."'()]|(   )''', '', content)
    content = str(content.split())
    new = open(outfile, 'w', encoding='utf8')
    new.write(content)
    new.close()
    # return content
parseNepali()
