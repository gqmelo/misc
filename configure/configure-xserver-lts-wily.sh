#!/usr/bin/env bash

ARG="$1"

OOPTION="-O2"
if [ "$ARG" == "-d" ]; then
    OOPTION="-O0"
fi


../configure --prefix=/usr/local --mandir='${prefix}/share/man' --infodir='${prefix}/share/info' --sysconfdir=/etc \
    --localstatedir=/var --build=x86_64-linux-gnu lt_cv_prog_compiler_static_works=no lt_cv_prog_compiler_static_works=no \
    --disable-silent-rules --disable-static --without-dtrace --disable-strict-compilation --disable-debug \
    --enable-unit-tests --with-int10=x86emu \
    --with-extra-module-dir=/usr/lib/x86_64-linux-gnu/xorg/extra-modules,/usr/lib/xorg/extra-modules \
    --with-os-vendor=Ubuntu --with-xkb-path=/usr/share/X11/xkb --with-xkb-output='${prefix}/var/lib/xkb' \
    --with-shared-memory-dir=/dev/shm --disable-install-libxf86config --enable-mitshm --enable-xres \
    --disable-xcsecurity --disable-tslib --enable-dbe --disable-xf86bigfont --enable-dpms --disable-config-dbus \
    --disable-config-hal --enable-config-udev --enable-xorg --disable-linux-acpi --disable-linux-apm --disable-xquartz \
    --disable-xwin --disable-xfake --disable-xfbdev --disable-install-setuid \
    --with-default-font-path=/usr/share/fonts/X11/misc,/usr/share/fonts/X11/cyrillic,/usr/share/fonts/X11/100dpi/:unscaled,/usr/share/fonts/X11/75dpi/:unscaled,/usr/share/fonts/X11/Type1,/usr/share/fonts/X11/100dpi,/usr/share/fonts/X11/75dpi,built-ins \
    --enable-aiglx --enable-glx-tls --enable-registry --enable-composite --enable-record --enable-xv --enable-xvmc \
    --enable-dga --enable-screensaver --enable-xdmcp --enable-xdm-auth-1 --enable-glx --enable-dri --enable-dri2 \
    --enable-glamor --enable-dri3 --enable-present --enable-xinerama --enable-xf86vidmode --enable-xace \
    --enable-xselinux --enable-xfree86-utils --enable-xwayland --enable-dmx --enable-xvfb --enable-xnest \
    --enable-kdrive --enable-xephyr --with-sha1=libgcrypt --enable-xcsecurity \
    PKG_CONFIG_PATH=/usr/local/lib/x86_64-linux-gnu/pkgconfig \
    CFLAGS="-g $OOPTION -fPIE -fstack-protector -Wformat -Werror=format-security" \
    CPPFLAGS="-D_FORTIFY_SOURCE=2 -DPRE_RELEASE=0" \
     CXXFLAGS="-g $OOPTION -fPIE -fstack-protector -Wformat -Werror=format-security" \
     FCFLAGS="-g $OOPTION -fPIE -fstack-protector" \
     FFLAGS="-g $OOPTION -fPIE -fstack-protector" \
     GCJFLAGS="-g $OOPTION -fPIE -fstack-protector" \
     LDFLAGS=-"Wl,-Bsymbolic-functions -fPIE -pie -Wl,-z,relro -Wl,-Bsymbolic" \
     OBJCFLAGS="-g $OOPTION -fPIE -fstack-protector -Wformat -Werror=format-security" \
     OBJCXXFLAGS="-g $OOPTION -fPIE -fstack-protector -Wformat -Werror=format-security" LIBS=
