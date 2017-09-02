#!/usr/bin/env bash

# BUNDLED_LIBSTDCXX_DIR=DIR_TO_BUNDLED_LIBSTDCXX

print_info() {
    echo "$1" >&2
}

print_info "Looking for libstdc++ ..."
SYSTEM_LIBSTDCXX="`/sbin/ldconfig -p | grep x86-64 | grep libstdc++ | awk '{print $4}'`"
BUNDLED_LIBSTDCXX="$BUNDLED_LIBSTDCXX_DIR/libstdc++.so.6"

get_version () {
    # http://stackoverflow.com/a/10356740
    readelf -sV "$1" | sed -n 's/.*@@GLIBCXX_//p' | sort -u -V | tail -1
}

get_newer_version () {
    echo "`tr '.' ' ' | sort -nu -t ' ' -k 1 -k 2 -k 3 | tr ' ' '.' | tail -1`"
}

SYSTEM_LIBSTDCXX_VERSION="`get_version $SYSTEM_LIBSTDCXX`"
BUNDLED_LIBSTDCXX_VERSION="`get_version $BUNDLED_LIBSTDCXX`"

print_info "System:
 - version: $SYSTEM_LIBSTDCXX_VERSION
 - path: $SYSTEM_LIBSTDCXX

Bundled:
 - version: $BUNDLED_LIBSTDCXX_VERSION
 - path: $BUNDLED_LIBSTDCXX
"

NEWER_LIBSTDCXX_VERSION="`printf \"$BUNDLED_LIBSTDCXX_VERSION\n$SYSTEM_LIBSTDCXX_VERSION\" | get_newer_version`"

if [ "$NEWER_LIBSTDCXX_VERSION" = "$BUNDLED_LIBSTDCXX_VERSION" ]; then
    print_info "Choosing bundled libstdc++"
    export LD_LIBRARY_PATH="$BUNDLED_LIBSTDCXX_DIR:$LD_LIBRARY_PATH"
#    export LD_PRELOAD="libstdc++.so.6 $LD_PRELOAD"
elif [ "$NEWER_LIBSTDCXX_VERSION" = "$SYSTEM_LIBSTDCXX_VERSION" ]; then
    print_info "Choosing system libstdc++"
fi

# exec PROGRAM_TO_RUN
