// Last updated: 19/7/2025, 2:13:20 pm
import java.util.*;

class Node {
    Node[] childs = new Node[27];
    boolean isEnd = false;
}

class Trie {
    Node root = new Node();

    void insert(String folder) {
        Node node = root;
        for (char ch : folder.toCharArray()) {
            int idx;
            if (ch == '/') {
                if (node.isEnd) return;
                idx = 26;
            } else {
                idx = ch - 'a';
            }
            if (node.childs[idx] == null) {
                node.childs[idx] = new Node();
            }
            node = node.childs[idx];
        }
        node.isEnd = true;

        node.childs[26] = null;
    }

    void getAllMainFolders(Node node, String path, List<String> out) {
        if (node.isEnd) {
            out.add(path);
        }
        for (int i = 0; i < 26; i++) {
            if (node.childs[i] != null) {
                getAllMainFolders(node.childs[i], path + (char)('a' + i), out);
            }
        }
        if (node.childs[26] != null) {
            getAllMainFolders(node.childs[26], path + '/', out);
        }
    }
}

public class Solution {
    public List<String> removeSubfolders(String[] folders) {
        Trie trie = new Trie();
        for (String f : folders) {
            trie.insert(f);
        }
        List<String> res = new ArrayList<>();
        trie.getAllMainFolders(trie.root, "", res);
        return res;
    }
}