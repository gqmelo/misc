#include <iostream>
#include <memory>

struct Point {
    int x;
    int y;
    Point(int x, int y) : x(x), y(y) {}
};

int main () {
    std::unique_ptr<Point> point1 = std::make_unique<Point>(10, 15);
    std::cout << "x: " << point1->x << ", y: " << point1->y << std::endl;

    std::unique_ptr<Point> point2;
    point2 = move(point1);

    // causes seg fault, not caught by compiler
    // std::cout << "x: " << point1->x << ", y: " << point1->y << std::endl;

    std::cout << "x: " << point2->x << ", y: " << point2->y << std::endl;
}