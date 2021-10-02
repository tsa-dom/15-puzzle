#include<vector>
#include<cmath>

using namespace std;

int manhattanDistance(vector<int> puzzle) {
    int distance = 0;
    for (int i = 0; i < 16; i++) {
        int piece = puzzle[i] - 1;
        if (piece == 15) {
          continue;
        };
        distance += std::abs (piece / 4 - i / 4) + std::abs (piece % 4 - i % 4); 
    };
    return distance;
}