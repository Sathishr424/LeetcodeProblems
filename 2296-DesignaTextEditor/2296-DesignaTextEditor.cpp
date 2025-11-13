// Last updated: 13/11/2025, 6:15:57 pm
#include <cmath>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class TextEditor {
public:
    vector<char> left;
    deque<char> right;
    TextEditor() {
    }

    void addText(string text) {
        for (char c: text) {
            left.push_back(c);
        }
    }

    int deleteText(int k) {
        int old = left.size();
        while (left.size() && k) {
            left.pop_back();
            k--;
        }
        return old - left.size();
    }

    string cursorLeft(int k) {
        while (left.size() && k) {
            right.push_front(left.back());
            left.pop_back();
            k--;
        }
        string ret;
        for (int i=max(0, static_cast<int>(left.size()) - 10); i<left.size(); i++) {
            ret.push_back(left[i]);
        }
        return ret;
    }

    string cursorRight(int k) {
        while (right.size() && k) {
            left.push_back(right.front());
            right.pop_front();
            k--;
        }
        string ret;
        for (int i=max(0, static_cast<int>(left.size()) - 10); i<left.size(); i++) {
            ret.push_back(left[i]);
        }
        return ret;
    }
};

/**
 * Your TextEditor object will be instantiated and called as such:
 * TextEditor* obj = new TextEditor();
 * obj->addText(text);
 * int param_2 = obj->deleteText(k);
 * string param_3 = obj->cursorLeft(k);
 * string param_4 = obj->cursorRight(k);
 */