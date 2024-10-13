#include <iostream>
#include <vector>
#include <algorithm>


std::vector<int> graphysort(const std::vector<int>& arr) {
    std::vector<int> sorted_arr;
    int max_val = *std::max_element(arr.begin(), arr.end());
    

    std::vector<std::pair<int, int>> points;
    for (int val : arr) {
        points.push_back({val, val}); 
    }


    for (int y = 1; y <= max_val; ++y) {
        for (auto& point : points) {
            if (point.second == y) { 
                sorted_arr.push_back(point.first); 
                break; 
            }
        }
    }

    return sorted_arr;
}

int main() {

    std::vector<int> array = {345, 32, 65, 1, 73, 2, 12, 8, 83};


    std::cout << "Original array: ";
    for (const int& val : array) {
        std::cout << val << " ";
    }
    std::cout << std::endl;


    std::vector<int> sorted_array = graphysort(array);


    std::cout << "Sorted array: ";
    for (const int& val : sorted_array) {
        std::cout << val << " ";
    }
    std::cout << std::endl;

    return 0;
}
