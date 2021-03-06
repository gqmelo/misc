
// Based on https://www.opengl.org/wiki/Programming_OpenGL_in_Linux:_GLX_and_Xlib

#include<stdio.h>
#include<stdlib.h>
#include<X11/X.h>
#include<X11/Xlib.h>
#include<GL/gl.h>
#include<GL/glx.h>
#include<GL/glu.h>

Display *dpy;
Window root;
GLint att[] = { GLX_RGBA, GLX_DEPTH_SIZE, 24, GLX_DOUBLEBUFFER, None };
XVisualInfo *vi;
Colormap cmap;
Colormap cmap2;
XSetWindowAttributes swa;
XSetWindowAttributes swa2;
Window win;
Window win2;
GLXContext glc;
GLXContext glc2;
XWindowAttributes gwa;
XEvent xev;
char *user_input;
int bytes_read;
int nbytes = 100;

void DrawAQuad() {
    glClearColor(1.0, 1.0, 1.0, 1.0);
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    glOrtho(-1., 1., -1., 1., 1., 20.);

    glMatrixMode(GL_MODELVIEW);
    glLoadIdentity();
    gluLookAt(0., 0., 10., 0., 0., 0., 0., 1., 0.);

    glBegin(GL_QUADS);
    glColor3f(1., 0., 0.);
    glVertex3f(-.75, -.75, 0.);
    glColor3f(0., 1., 0.);
    glVertex3f(.75, -.75, 0.);
    glColor3f(0., 0., 1.);
    glVertex3f(.75, .75, 0.);
    glColor3f(1., 1., 0.);
    glVertex3f(-.75, .75, 0.);
    glEnd();
}

int main(int argc, char *argv[]) {

    dpy = XOpenDisplay(NULL);

    if (dpy == NULL) {
        printf("\n\tcannot connect to X server\n\n");
        exit(0);
    }

    root = DefaultRootWindow(dpy);

    vi = glXChooseVisual(dpy, 0, att);

    if (vi == NULL) {
        printf("\n\tno appropriate visual found\n\n");
        exit(0);
    } else {
        printf("\n\tvisual %p selected\n", (void *) vi->visualid); /* %p creates hexadecimal output like in glxinfo */
    }

    cmap = XCreateColormap(dpy, root, vi->visual, AllocNone);
    cmap2 = XCreateColormap(dpy, root, vi->visual, AllocNone);

    swa.colormap = cmap;
    swa.event_mask = ExposureMask | KeyPressMask;

    swa2.colormap = cmap2;
    swa2.event_mask = ExposureMask | KeyPressMask;

    win = XCreateWindow(dpy, root, 0, 0, 300, 300, 0, vi->depth, InputOutput,
            vi->visual, CWColormap | CWEventMask, &swa);
    win2 = XCreateWindow(dpy, root, 300, 300, 300, 300, 0, vi->depth, InputOutput,
            vi->visual, CWColormap | CWEventMask, &swa2);

    XMapWindow(dpy, win);
    XMapWindow(dpy, win2);
    XStoreName(dpy, win, "First Window");
    XStoreName(dpy, win2, "Second Window");

    XSync(dpy, 0);

    glc = glXCreateContext(dpy, vi, NULL, GL_TRUE);
    glc2 = glXCreateContext(dpy, vi, NULL, GL_TRUE);
    glXMakeCurrent(dpy, win2, glc2);
    printf("OpenGL version: %s\n", (char*)glGetString(GL_VERSION));
    puts("Press Enter to change context");
    bytes_read = getline(&user_input, &nbytes, stdin);
    glXMakeCurrent(dpy, win, glc);

    glEnable(GL_DEPTH_TEST);

    while (1) {
        XNextEvent(dpy, &xev);

        if (xev.type == Expose) {
            puts("Press Enter to draw");
            bytes_read = getline(&user_input, &nbytes, stdin);
            XGetWindowAttributes(dpy, win, &gwa);
            glViewport(0, 0, gwa.width, gwa.height);
            DrawAQuad();
            glXSwapBuffers(dpy, win);
            puts("Press Enter to finish");
            bytes_read = getline(&user_input, &nbytes, stdin);
            glXMakeCurrent(dpy, None, NULL);
            glXDestroyContext(dpy, glc);
            XDestroyWindow(dpy, win);
            XDestroyWindow(dpy, win2);
            XCloseDisplay(dpy);
            exit(0);
        }
    }
}
