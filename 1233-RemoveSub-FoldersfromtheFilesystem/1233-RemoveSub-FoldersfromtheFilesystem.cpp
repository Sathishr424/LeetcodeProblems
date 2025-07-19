// Last updated: 19/7/2025, 2:10:46 pm
#include <bits/stdc++.h>
using namespace std;

struct Node {
    Node* childs[27];
    bool is_end;
    Node() {
        for (int i = 0; i < 27; i++) childs[i] = nullptr;
        is_end = false;
    }
};

class Trie {
public:
    Node* root;
    Trie() {
        root = new Node();
    }
    
    void insert(const string& folder) {
        Node* node = root;
        for (char ch : folder) {
            int idx;
            if (ch == '/') {
                if (node->is_end) return; // Already a main folder
                idx = 26;
            } else {
                idx = ch - 'a';
            }
            if (!node->childs[idx]) {
                node->childs[idx] = new Node();
            }
            node = node->childs[idx];
        }
        node->is_end = true;
        // Clear children beyond this folder
        node->childs[26] = nullptr;
    }
    
    void getAllMainFolders(Node* node, string current, vector<string>& result) {
        if (node->is_end) {
            result.push_back(current);
        }
        for (int i = 0; i < 26; i++) {
            if (node->childs[i]) {
                getAllMainFolders(node->childs[i], current + char('a' + i), result);
            }
        }
        if (node->childs[26]) {
            getAllMainFolders(node->childs[26], current + '/', result);
        }
    }
};

class Solution {
public:
    vector<string> removeSubfolders(vector<string>& folders) {
        Trie trie;
        for (const string& folder : folders) {
            trie.insert(folder);
        }
        vector<string> result;
        trie.getAllMainFolders(trie.root, "", result);
        return result;
    }
};
