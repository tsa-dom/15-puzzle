#include<vector>
#include<string>
#include<algorithm>
#include<iostream>

using namespace std;

string puzzleToString(vector<int> puzzle) {
    string str = "";
    std::vector<int>::iterator it;
    for (it = puzzle.begin(); it != puzzle.end(); ++it) {
        if (*it < 10) str += to_string(*it);
        else if (*it == 10) str += "a";
        else if (*it == 11) str += "b";
        else if (*it == 12) str += "c";
        else if (*it == 13) str += "d";
        else if (*it == 14) str += "e";
        else if (*it == 15) str += "f";
        else str += "x";
    }
    return str;
};

bool isComplete(vector<int> puzzle) {
    for (int i = 0; i < 16; i++) {
        if (i + 1 != puzzle[i]) return false;
    }
    return true;
}

int find16(vector<int> puzzle) {
    for (int i = 0; i < 16; i++) {
        if (puzzle[i] == 16) return i;
    }
    return -1;
}

vector<int> swapPuzzle(vector<int> puzzle, int i, int j) {
    vector<int> swap;
    for (int i = 0; i < 16; i++) {
        swap.push_back(puzzle[i]);
    }
    iter_swap(swap.begin() + i, swap.begin() + j);
    return swap;
}

bool comp(vector<int> a, vector<int> b) {
    int x1 = manhattanDistance(a);
    int x2 = manhattanDistance(b);
    return x1 - x2;
};

vector<vector<int>> getSuccessors(vector<int> puzzle) {
    int x = find16(puzzle) + 1;
    int p1 = -1;
    int p2 = -1;
    int p3 = -1;
    int p4 = -1;
    vector<vector<int>> successors;
    if (x + 4 <= 16) p1 = x + 4;
    if (x - 4 >= 1) p2 = x - 4;
    if (x % 4 != 0) p3 = x + 1;
    if ((x - 1) % 4 != 0) p4 = x - 1;
    if (p1 != -1) successors.push_back(swapPuzzle(puzzle, x - 1, p1 - 1));
    if (p2 != -1) successors.push_back(swapPuzzle(puzzle, x - 1, p2 - 1));
    if (p3 != -1) successors.push_back(swapPuzzle(puzzle, x - 1, p3 - 1));
    if (p4 != -1) successors.push_back(swapPuzzle(puzzle, x - 1, p4 - 1));
    sort(successors.begin(), successors.end(), comp);
    return successors;
}