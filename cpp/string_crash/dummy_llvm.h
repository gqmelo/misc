#ifndef CPP_STRING_CRASH_DUMMY_LLVM_H_
#define CPP_STRING_CRASH_DUMMY_LLVM_H_

#include <cstdio>
#include <string>


class FooEngineBuilder {
public:
  std::string MCPU;
  /// Default constructor for FooEngineBuilder.
  FooEngineBuilder();

  /// setMCPU - Target a specific cpu type.
  FooEngineBuilder &setMCPUFromHeader() {
    printf("########################\n");
    printf("FooEngineBuilder::setMCPUFromHeader\n");
    std::string mymcpu;
    mymcpu = "my_mcpu";
    printf("mymcpu: %s\n", mymcpu.c_str());
    printf("MCPU: %s\n", MCPU.c_str());
    printf("MCPU.length: %i\n", (int)MCPU.length());
    printf("MCPU.c_str: %p\n", MCPU.c_str());
//    MCPU.assign(mcpu.begin(), mcpu.end());
//    MArch.assign(mymcpu.begin(), mymcpu.end());
    MCPU.assign(mymcpu.begin(), mymcpu.end());
    printf("FooEngineBuilder::setMCPUFromHeader end\n");
    printf("########################\n");
    return *this;
  }

  FooEngineBuilder &setMCPUFromSource();
};


#endif /* CPP_STRING_CRASH_DUMMY_LLVM_H_ */
