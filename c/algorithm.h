#include<iostream>
#include<vector>
#include<set>

using namespace std;

vector<vector<int>> path;
set<string> pathContent;

float search (int g, int bound) {
    vector<int> node = path[path.size() - 1];
    float f = g + manhattanDistance(node);
    if (f > bound) return f;
    if (isComplete(node)) return -1;
    float min = 10000000;
    vector<vector<int>> successors = getSuccessors(node);
    for (vector<int> puzzle : successors) {
        string puzzleStr = puzzleToString(puzzle);
        if (pathContent.find(puzzleStr) == pathContent.end()) {
            path.push_back(puzzle);
            pathContent.insert(puzzleStr);

            float result = search(g + 1, bound);
            if (result == -2) return -2;
            if (result == -1) {
                for (int i = 0; i < path.size(); i++) {
                    for (int j = 0; j < path[i].size(); j++) {
                        cout << path[i][j] << " ";
                    }
                    cout << "\n";
                }
                return -2;
            };
            if (result < min) min = result;
            pathContent.erase(puzzleStr);
            path.pop_back();
        }
    }
    return min;
}

vector<vector<int>> idaStar (vector<int> puzzle) {
    int bound = manhattanDistance(puzzle);
    path.push_back(puzzle);

    pathContent.insert(puzzleToString(puzzle));
    while (true) {
        int newBound = search(0, bound);
        if (newBound == -1 || newBound == -2) {
            return path;
        }
        bound = newBound;
    }
}