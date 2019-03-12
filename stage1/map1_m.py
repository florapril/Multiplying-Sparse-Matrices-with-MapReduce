#!/usr/bin/env python
import sys

for line in sys.stdin:
  line = line.strip()
  records = line.split('\t')
  print '%s\t%s\t%s\t%s' % (record[1], 'm', record[0], record[2])
