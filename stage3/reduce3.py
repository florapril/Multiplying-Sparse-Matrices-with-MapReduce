#!/usr/bin/env python
import sys

current_key = None
current_sum = 0
key = None

for line in sys.stdin:
  line = line.strip()
  key, value = line.split('\t')
  
  try:
    value = float(value)
  except ValueError:
    continue
    
  if current_key == key:
    current_sum += value
  else:
    if current_key:
      print '%s\t%s' % (current_key, current_sum)
    current_sum = value
    current_key = key
    
if current_key == key:
  print '%s\t%s' % (current_key, current_sum)
