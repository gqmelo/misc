#!/bin/sh

../configure --prefix=$HOME/local --mandir='${prefix}/share/man' --infodir='${prefix}/share/info' \
    --sysconfdir=/etc --localstatedir=/var --build=x86_64-linux-gnu lt_cv_prog_compiler_static_works=no \
    lt_cv_prog_compiler_static_works=no --disable-silent-rules --disable-static --without-dtrace \
    --disable-strict-compilation --disable-debug --enable-unit-tests --with-int10=x86emu \
    --with-extra-module-dir=/usr/lib/x86_64-linux-gnu/xorg/extra-modules,/usr/lib/xorg/extra-modules \
    --with-os-vendor=Ubuntu \
    --with-xkb-path=/usr/share/X11/xkb --with-xkb-output='${prefix}/var/lib/xkb' --disable-install-libxf86config \
    --enable-mitshm --enable-xres --disable-xcsecurity --disable-tslib --enable-dbe --disable-xf86bigfont \
    --enable-dpms --disable-config-dbus --disable-config-hal --enable-config-udev --enable-xorg --disable-linux-acpi \
    --disable-linux-apm --disable-xquartz --disable-xwin --disable-xfake --disable-xfbdev --disable-install-setuid \
    --with-default-font-path=/usr/share/fonts/X11/misc,/usr/share/fonts/X11/cyrillic,/usr/share/fonts/X11/100dpi/:unscaled,/usr/share/fonts/X11/75dpi/:unscaled,/usr/share/fonts/X11/Type1,/usr/share/fonts/X11/100dpi,/usr/share/fonts/X11/75dpi,built-ins \
    --enable-aiglx --enable-glx-tls --enable-registry --enable-composite --enable-record --enable-xv \
    --enable-xvmc --enable-dga --enable-screensaver --enable-xdmcp --enable-xdm-auth-1 --enable-glx --enable-dri \
    --enable-dri2 --enable-dri3 --enable-present --enable-xinerama --enable-xf86vidmode --enable-xace --enable-xselinux \
    --enable-xfree86-utils --enable-dmx --enable-xvfb --enable-xnest --enable-kdrive --enable-xephyr \
    --enable-xmir --with-sha1=libgcrypt --enable-xcsecurity \
    PKG_CONFIG_PATH=$HOME/local/lib/x86_64-linux-gnu/pkgconfig \
    CFLAGS="-g -O0 -fPIE -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security" \
    CPPFLAGS="-D_FORTIFY_SOURCE=2 -DPRE_RELEASE=0" \
    CXXFLAGS="-g -O0 -fPIE -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security" \
    FFLAGS="-g -O0 -fPIE -fstack-protector --param=ssp-buffer-size=4" \
    GCJFLAGS="-g -O0 -fPIE -fstack-protector --param=ssp-buffer-size=4" \
    LDFLAGS="-Wl,-Bsymbolic-functions -fPIE -pie -Wl,-z,relro -Wl,-Bsymbolic" \
    LIBS=
