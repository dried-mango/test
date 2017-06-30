#!/usr/bin/python
import os

commit = raw_input("Commit:")
os.system('git add .')
os.system('git commit -m "(%s)"' % commit)
os.system('git push origin master')
