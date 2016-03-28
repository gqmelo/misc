#!/usr/bin/env bash

../../configure --prefix=$HOME/local --mandir=\${prefix}/share/man \
     --enable-debug \
     --infodir=\${prefix}/share/info --sysconfdir=\${prefix}/etc \
     --libdir=\${prefix}/lib/x86_64-linux-gnu \
     --localstatedir=\${prefix}/var --disable-silent-rules \
     --build=x86_64-linux-gnu --enable-dri --with-dri-drivers=" nouveau i915 i965 r200 radeon" \
     --with-dri-driverdir=\${prefix}/lib/dri \
     --with-dri-searchpath='\${prefix}/lib/dri:\$${ORIGIN}/dri' \
     --disable-osmesa --enable-glx-tls --enable-shared-glapi --enable-texture-float \
     --disable-xvmc --disable-omx --enable-driglx-direct --enable-dri3 \
     --with-egl-platforms="x11 wayland drm" --enable-xa --enable-gallium-llvm \
     ac_cv_path_LLVM_CONFIG=llvm-config-3.6 \
     --with-gallium-drivers=" nouveau svga r600 r300 radeonsi swrast" \
     --enable-gles1 --enable-gles2 \
     CFLAGS="-g -O0 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -Wall" \
     CPPFLAGS="-D_FORTIFY_SOURCE=2" \
     CXXFLAGS="-g -O0 -fstack-protector --param=ssp-buffer-size=4 -Wformat -Werror=format-security -Wall" \
     FFLAGS="-g -O0 -fstack-protector --param=ssp-buffer-size=4" \
     GCJFLAGS="-g -O0 -fstack-protector --param=ssp-buffer-size=4" \
     LDFLAGS="-Wl,-Bsymbolic-functions -Wl,-z,relro"
