#include <set>
#include <string>

bool has_unique_chars(const std::string& input) {
    std::set<char> visited;
    for (std::string::const_iterator it = input.begin(); it != input.end(); it++){
        if(visited.find(*it) != visited.end()){
            return false;
        }
        visited.insert(*it);
    }
    return true;
}
