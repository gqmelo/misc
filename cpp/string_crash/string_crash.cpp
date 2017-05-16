#include "dummy_llvm.h"

int main(int argc, char** argv) {
    FooEngineBuilder builder;
    builder.setMCPUFromHeader();

    std::string s("foobar");
}
