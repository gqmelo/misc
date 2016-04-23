import pexpect
import os

env = os.environ.copy()
env['LIBGL_ALWAYS_INDIRECT'] = 1

glx_process_1 = pexpect.spawn('./quad')
glx_process_2 = pexpect.spawn('./quad')

glx_process_1.expect('Press Enter to change context')
glx_process_2.expect('Press Enter to change context')

glx_process_2.sendline('')
glx_process_2.expect('Press Enter to draw')

glx_process_1.sendline('')
glx_process_1.expect('Press Enter to draw')

glx_process_2.sendline('')
glx_process_2.expect('Press Enter to finish')

glx_process_1.sendline('')
glx_process_1.expect('Press Enter to finish')

glx_process_1.sendline('')
glx_process_1.expect(pexpect.EOF)

glx_process_2.sendline('')
glx_process_2.expect(pexpect.EOF)
