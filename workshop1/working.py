__author__ = 'nick'


import subprocess

p = subprocess.Popen(['ls', '-l', '/home/nick'],
                     stdout=subprocess.PIPE)

q = subprocess.Popen(['tr', '[d-p]', '[D-P]'],
                     stdin=p.stdout,
                     stdout=subprocess.PIPE)

r = subprocess.Popen(['grep', '^D'],
                     stdin=q.stdout,
                     stdout=subprocess.PIPE)

for line in r.stdout:
    print '>>', line,