// Last updated: 19/7/2025, 2:13:56 pm
class Node {
  constructor() {
    this.childs = new Array(27).fill(null);
    this.isEnd = false;
  }
}

class Trie {
  constructor() {
    this.root = new Node();
  }

  insert(folder) {
    let node = this.root;
    for (const ch of folder) {
      let idx;
      if (ch === '/') {
        if (node.isEnd) return;
        idx = 26;
      } else {
        idx = ch.charCodeAt(0) - 'a'.charCodeAt(0);
      }
      if (!node.childs[idx]) {
        node.childs[idx] = new Node();
      }
      node = node.childs[idx];
    }
    node.isEnd = true;

    node.childs[26] = null;
  }

  getAllMainFolders(node, s, out) {
    if (node.isEnd) {
      out.push(s);
    }
    for (let i = 0; i < 26; i++) {
      if (node.childs[i]) {
        this.getAllMainFolders(node.childs[i], s + String.fromCharCode('a'.charCodeAt(0) + i), out);
      }
    }
    if (node.childs[26]) {
      this.getAllMainFolders(node.childs[26], s + '/', out);
    }
  }
}

function removeSubfolders(folders) {
  const trie = new Trie();
  for (const f of folders) {
    trie.insert(f);
  }
  const res = [];
  trie.getAllMainFolders(trie.root, "", res);
  return res;
}