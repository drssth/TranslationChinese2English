import os, os.path

txt = ''

for i in range(82):
    fn = 'DaoDeJing{0:03}.md'.format(i)
    if os.path.exists(fn):
        with open(fn, 'r') as f:
            txt += f.read()
            txt += '\n\n\n'
            
with open('DaoDeJing1-81.md', 'w') as f:
    f.write(txt)