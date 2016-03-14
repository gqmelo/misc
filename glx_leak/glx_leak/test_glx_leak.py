from Xlib import X, display
from OpenGL import GL, GLX
from OpenGL.raw._GLX import struct__XDisplay
from ctypes import *

def draw_square(display, window):
    # some python-opengl code....
    GL.glShadeModel(GL.GL_FLAT)
    GL.glClearColor(0.5, 0.5, 0.5, 1.0)

    GL.glViewport(0, 0, 200, 200)
    GL.glMatrixMode(GL.GL_PROJECTION)
    GL.glLoadIdentity()
    GL.glOrtho(-1.0, 1.0, -1.0, 1.0, -1.0, 1.0)

    GL.glClear(GL.GL_COLOR_BUFFER_BIT)
    GL.glColor3f(1.0, 1.0, 0.0)
    GL.glRectf(-0.8, -0.8, 0.8, 0.8)

    # assume we got a double buffered fbConfig and show what we drew
    GLX.glXSwapBuffers(display, window)

# some python-xlib code...
pd = display.Display()
pw = pd.screen().root.create_window(0, 0, 200, 200, 0,
                                    pd.screen().root_depth,
                                    X.InputOutput, X.CopyFromParent)
pw.map()

pw2 = pd.screen().root.create_window(50, 50, 200, 200, 0,
                                    pd.screen().root_depth,
                                    X.InputOutput, X.CopyFromParent)
pw2.map()

# ensure that the XID is valid on the server
pd.sync()

# get the window XID
xid = pw.__resource__()
xid2 = pw2.__resource__()

# a separate ctypes Display object for OpenGL.GLX
xlib = cdll.LoadLibrary('libX11.so')
xlib.XOpenDisplay.argtypes = [c_char_p]
xlib.XOpenDisplay.restype = POINTER(struct__XDisplay)
d = xlib.XOpenDisplay("")
# d2 = xlib.XOpenDisplay("")

# use GLX to create an OpenGL context on the same window XID
elements = c_int()
configs = GLX.glXChooseFBConfig(d, 0, None, byref(elements))
print d, configs[0], c_ulong(xid), None
w = GLX.glXCreateWindow(d, configs[0], c_ulong(xid), None)
context = GLX.glXCreateNewContext(d, configs[0], GLX.GLX_RGBA_TYPE, None, True)
GLX.glXMakeContextCurrent(d, w, w, context)
GLX.glXMakeCurrent(d, w, context)
raw_input('Press any key to draw')
draw_square(d, w)

# elements2 = c_int()
# configs2 = GLX.glXChooseFBConfig(d2, 0, None, byref(elements2))
# print d2, configs2[0], c_ulong(xid2), None
# w2 = GLX.glXCreateWindow(d2, configs2[0], c_ulong(xid2), None)
# context2 = GLX.glXCreateNewContext(d2, configs2[0], GLX.GLX_RGBA_TYPE, None, True)
# GLX.glXMakeContextCurrent(d2, w2, w2, context2)
# draw_square(d2, w2)


# GLX.glXMakeCurrent(d, w2, context2)
# GLX.glXMakeCurrent(d, w2, context2)
# GLX.glXMakeCurrent(d, w, context)

# a terrible end to a terrible piece of code...
raw_input()
