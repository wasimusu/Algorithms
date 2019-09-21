/**
Factor of 2 approximate solution for knapsack
Space complexity : O(1)
Time complexity : O(n)
*/
#include <iostream>
#include <vector>
#include <cassert>

using namespace std;

/**
 * @brief : Finds factor of 2 approximate solution for knapsack. Not optimal.
 * @param weights : weights of each items that should be kept in the knapsack
 * @param capacity : the capacity of the knapsack
 * @return : total used capacity of the knapsack
 */
int knapsack(std::vector<int> weights, const int capacity) {
    int used_capacity = 0;
    for (int i = 0; i < weights.size(); i++) {
        if (used_capacity + weights[i] < capacity) {
            used_capacity += weights[i];
        } else if (weights[i] > used_capacity && weights[i] <= capacity) {
            used_capacity = max(used_capacity, weights[i]);
        }
    }
    return used_capacity;
}

int main() {
    // Test 1
    vector<int> weights1 = {9, 24, 14, 5, 8, 17};
    int capacity = 20;
    int packed_capacity = knapsack(weights1, capacity);
    assert(packed_capacity == 19);
    std::cout << "Knapsack packed at capacity : " << packed_capacity << std::endl;

    // Test 2
    vector<int> weights2 = {9, 24, 14, 5, 8, 20};
    capacity = 20;
    packed_capacity = knapsack(weights2, capacity);
    assert(packed_capacity == 20);
    std::cout << "Knapsack packed at capacity : " << packed_capacity << std::endl;

    // Test 3
    vector<int> weights3 = {9, 24, 14, 17};
    capacity = 20;
    packed_capacity = knapsack(weights3, capacity);
    assert(packed_capacity <= capacity && packed_capacity >= capacity / 2);

    std::cout << "Knapsack packed at capacity : " << packed_capacity << std::endl;
    return 0;
}