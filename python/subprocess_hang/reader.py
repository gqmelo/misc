import subprocess
from subprocess import Popen, PIPE

import sys

# sys.stdout.write('-' * 80)
# sys.stdout.write('\n')
# sys.stdout.write('\n')
# output = subprocess.check_output('ls alkshdls; exit 0', shell=True,
#                                  stderr=subprocess.STDOUT)
# sys.stderr.flush()
# print(output)
# print('-' * 80)

print('-' * 80)
output = subprocess.check_output(['python', 'writer.py'],
                                 stderr=subprocess.STDOUT)
# print(output)
print('-' * 80)

# THIS HANGS

# print('-' * 80)
# output = subprocess.check_call(['python', 'writer.py'],
#                                  stderr=subprocess.PIPE)
# print('-' * 80)


# THIS HANGS

# p = Popen(['python', 'writer.py'], stdout=PIPE, stderr=PIPE)
# print(p.wait())


# THIS DOES NOT HANG

# p = Popen(['python', 'writer.py'], stdout=PIPE, stderr=PIPE)
# out, err = p.communicate()
# print out, err
