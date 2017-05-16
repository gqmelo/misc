#include "dummy_llvm.h"


FooEngineBuilder::FooEngineBuilder() {
    printf("########################\n");
    printf("FooEngineBuilder::FooEngineBuilder()\n");
    std::string mymcpu;
//    mymcpu = "my_mcpu";
    printf("mymcpu: %s\n", mymcpu.c_str());
    printf("MCPU: %s\n", MCPU.c_str());
    printf("MCPU.length: %i\n", (int)MCPU.length());
    printf("MCPU.c_str: %p\n", MCPU.c_str());
//    MCPU.assign(mymcpu.begin(), mymcpu.end());
    printf("FooEngineBuilder::FooEngineBuilder() end\n");
    printf("########################\n");
}


FooEngineBuilder &FooEngineBuilder::setMCPUFromSource() {
  printf("########################\n");
  printf("FooEngineBuilder::setMCPUFromSource\n");
  std::string mymcpu;
  mymcpu = "my_mcpu";
  printf("mymcpu: %s\n", mymcpu.c_str());
  printf("MCPU: %s\n", MCPU.c_str());
  printf("MCPU.length: %i\n", MCPU.length());
  printf("MCPU.c_str: %x\n", MCPU.c_str());
//    MCPU.assign(mcpu.begin(), mcpu.end());
//    MArch.assign(mymcpu.begin(), mymcpu.end());
  MCPU.assign(mymcpu.begin(), mymcpu.end());
  printf("FooEngineBuilder::setMCPUFromSource end\n");
  printf("########################\n");
  return *this;
}
