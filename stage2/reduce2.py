#!/usr/bin/env python
import sys

current_key = None
current_m_list = []
current_n_list = []
key = None

for line in sys.stdin:
  line = line.strip()
  key, tag, index, value = line.split('\t')
  
  try:
    value = float(value)
  except ValueError:
    continue
    
  if current_key == key:
  
    if tag == 'm':
      current_m_list.append((index, value))
    else:
      current_n_list.append((index, value))
      
  else:
  
    if len(current_m_list) > 0 and len(current_n_list) > 0:
      for m in current_m_list:
        for n in current_n_list:
          print '%s,%s\t%s' % (m[0],n[0],m[1]*n[1])
      current_m_list = []
      current_n_list = []
     
    current_key = key
    if tag == 'm':
      current_m_list = [(index, value)]
    else:
      current_n_list = [(index, value)]
      
if current_key == key:
  if len(current_m_list) > 0 and len(current_n_list) > 0:
      for m in current_m_list:
        for n in current_n_list:
          print '%s,%s\t%s' % (m[0],n[0],m[1]*n[1])
