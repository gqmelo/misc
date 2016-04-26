import pexpect
import os
import sys
import subprocess
from PIL import Image, ImageChops 

num = sys.argv[1]

env = os.environ.copy()

env['LIBGL_ALWAYS_INDIRECT'] = 1

glx_process_1 = pexpect.spawn('./one_glxcontext_with_two_windows')

glx_process_1.expect('Press Enter to finish')

windows = subprocess.check_output(['xwininfo', '-root', '-children', '-d', ':1'])
window = [line for line in windows.splitlines() if "First Window" in line][0]
window_id = window.split()[0]

obtained_filename = 'obtained_%s.png' % num
subprocess.check_call(['import', '-display', ':1', '-window', str(window_id), obtained_filename])

expected = Image.open('expected.png')
obtained = Image.open(obtained_filename)
try:
    if ImageChops.difference(expected, obtained).getbbox() is None:
        print '%s: OK' % obtained_filename
    else:
        print '%s: ERROR' % obtained_filename
except ValueError as e:
    print '%s: ERROR - %s' % (obtained_filename, e.message)
    
glx_process_1.sendline('')
glx_process_1.expect(pexpect.EOF)
