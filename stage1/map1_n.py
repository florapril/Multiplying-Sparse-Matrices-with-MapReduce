#!/usr/bin/env python
import sys

for line in sys.stdin:
  line = line.strip()
  records = line.split('\t')
  print '%s\t%s\t%s\t%s' % (records[0], 'n', records[1], records[2])
