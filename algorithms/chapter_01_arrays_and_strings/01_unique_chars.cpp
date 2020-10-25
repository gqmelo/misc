#include <set>
#include <string>

bool has_unique_chars(const std::string& input) {
    std::set<char> visited;
    for (auto& c: input){
        if(visited.find(c) != visited.end()){
            return false;
        }
        visited.insert(c);
    }
    return true;
}
