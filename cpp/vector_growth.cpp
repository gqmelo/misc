#include <vector>
#include <iostream>

int main(char** argv, int argc) {
    std::vector<int> vec;

    size_t last_capacity = vec.capacity();
    for (int i = 0; i < 2 ^ 10; i++) {
        vec.push_back(i);
        if (last_capacity != vec.capacity()) {
            std::cout << vec.capacity() << std::endl;
            last_capacity = vec.capacity();
        }
    }
}
