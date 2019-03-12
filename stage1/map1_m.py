#!/usr/bin/env python
import sys

for line in sys.stdin:
  line = line.strip()
  records = line.split('\t')
  print '%s\t%s\t%s\t%s' % (records[1], 'm', records[0], records[2])
