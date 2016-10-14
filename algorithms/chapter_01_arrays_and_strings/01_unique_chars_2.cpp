#include <algorithm>
#include <string>

using std::string;

bool has_unique_chars(const string& input) {
    string sorted = input;
    std::sort(sorted.begin(), sorted.end());
    string::const_iterator it;
    char previous = 0;
    for (it = sorted.begin(); it != sorted.end(); it++) {
        if (*it == previous) {
            return false;
        }
        previous = *it;
    }
    return true;
}
