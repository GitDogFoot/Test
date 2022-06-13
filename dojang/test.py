import os, re

def check_filename(filename):
    reg = re.compile("[^A-Za-z0-9_.가-힝-]")
    for s in os.path.sep, os.path.altsep:
        if s:
            filename = filename.replace(s, " ")
            filename = str(reg.sub('', '_'.join(filename.split()))).strip("._")
    return filename

print(check_filename("../../../../home/username/.bashrc"))
