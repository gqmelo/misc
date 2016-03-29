
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
XWindowAttributes gwa;
XEvent xev;

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

void CreateWindow(Colormap *cmap, XSetWindowAttributes *swa, Window *win, Display* dpy, const char* title) {
    *cmap = XCreateColormap(dpy, root, vi->visual, AllocNone);

    swa->colormap = *cmap;
    swa->event_mask = ExposureMask | KeyPressMask;

    *win = XCreateWindow(dpy, root, 0, 0, 300, 300, 0, vi->depth, InputOutput,
            vi->visual, CWColormap | CWEventMask, swa);

    XMapWindow(dpy, *win);
    XStoreName(dpy, *win, title);

    XSync(dpy, 0);
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

    CreateWindow(&cmap2, &swa2, &win2, dpy, "Second Window");
    CreateWindow(&cmap, &swa, &win, dpy, "First Window");

    glc = glXCreateContext(dpy, vi, NULL, GL_TRUE);
    glXMakeCurrent(dpy, win2, glc);
    printf("OpenGL version: %s\n", (char*)glGetString(GL_VERSION));
    glXMakeCurrent(dpy, None, NULL);
    XDestroyWindow(dpy, win2);

    glEnable(GL_DEPTH_TEST);

    while (1) {
        XNextEvent(dpy, &xev);

        if (xev.type == Expose) {
            glXMakeCurrent(dpy, win, glc);
            XGetWindowAttributes(dpy, win, &gwa);
            glViewport(0, 0, gwa.width, gwa.height);
            DrawAQuad();
            glXSwapBuffers(dpy, win);
        }

        else if (xev.type == KeyPress) {
            glXMakeCurrent(dpy, None, NULL);
            glXDestroyContext(dpy, glc);
            XDestroyWindow(dpy, win);
            XCloseDisplay(dpy);
            exit(0);
        }
    }
}
