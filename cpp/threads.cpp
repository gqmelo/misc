#include <atomic>
#include <chrono>
#include <iostream>
#include <mutex>
#include <thread>

std::mutex cout_mutex;
thread_local uint count_thread_local = 0;
std::atomic_uint count_global(0);

void increment() {
    using namespace std::chrono_literals;
    for (uint i = 0; i < 5; i++) {
        count_thread_local++;
        count_global++;
        {
            std::lock_guard<std::mutex> lock(cout_mutex);
            std::cout << "thread " << std::this_thread::get_id() << ": " << count_thread_local << " " << count_global << std::endl;
        }
        std::this_thread::sleep_for(1s);
    }
}

int main() {
    std::thread a(increment);
    std::thread b(increment);

    {
        std::lock_guard<std::mutex> lock(cout_mutex);
        std::cout << "thread " << std::this_thread::get_id() << ": " << count_thread_local << std::endl;
    }

    a.join();
    b.join();
}
