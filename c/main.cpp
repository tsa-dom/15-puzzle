#include"heuristic.h"
#include"helpers.h"
#include<iostream>
#include<vector>
#include"algorithm.h"
#include<chrono>

using namespace std;

int main() {
    
    /*vector<int> vect{2, 7, 10, 8, 14, 3, 5, 1, 11, 9, 13, 6, 12, 16, 4, 15};
    vector<int> comp{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15};
    cout << manhattanDistance(vect) << "\n";
    cout << puzzleToString(vect) << "\n";
    cout << isComplete(comp) << "\n";
    vector<int> test = swapPuzzle(vect, 1, 14);
    std::vector<int>::iterator it;
    for (it = test.begin(); it != test.end(); it++) {
        cout << *it << " ";
    };
    cout << "\n";
    vector<vector<int>> succ = getSuccessors(vect);
    for (int i = 0; i < succ.size(); i++) {
        for (int j = 0; j < succ[i].size(); j++) {
            cout << succ[i][j] << " ";
        }
        cout << "\n";
    }*/
    //vector<int> vect{1, 2, 11, 8, 6, 16, 14, 3, 5, 7, 15, 4, 9, 10, 13, 12};
    vector<int> vect{6, 1, 8, 3, 12, 4, 15, 13, 7, 14, 9, 10, 11, 2, 16, 5};
    auto start = chrono::high_resolution_clock::now();
    vector<vector<int>> result = idaStar(vect);
    auto stop = chrono::high_resolution_clock::now();
    auto duration = chrono::duration_cast<chrono::microseconds>(stop - start);
    cout << duration.count() << endl;

    return 0;
}