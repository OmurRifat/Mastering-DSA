class Node {
    constructor(value) {
        this.value = value;
        this.children = [];
    }
}

class GeneralTree {
    constructor() {
        this.root = null;
    }

    insert(value, parentValue = null) {
        const node = new Node(value);

        if (!this.root) {
            this.root = node;
            return true;
        }

        if (!parentValue) {
            return false;
        }

        const parentNode = this.search(parentValue);
        if (!parentNode) {
            return false;
        }

        parentNode.children.push(node);
        return true;
    }

    search(value) {
        const searchImpl = (value, node) => {
            if (!node) return null;

            if (node.value === value) return node;

            for (const child of node.children) {
                const result = searchImpl(value, child);
                if (result) return result;
            }

            return null;
        }

        return searchImpl(value, this.root)
    }

    remove(value) {
        if (!this.root) return false;

        if (this.root.value === value) {
            this.root = null;
            return true;
        }

        const parent = this.findParent(value, this.root);
        if (!parent) return false;

        parent.children = parent.children.filter((child) => child.value !== value);
        return true;
    }

    findParent(value, node) {
        if (!node) return null;

        for (const child of node.children) {
            if (child.value === value) return node;
        }

        for (const child of node.children) {
            const parent = this.findParent(value, child);
            if (parent) return parent;
        }

        return null;
    }

    preOrder() {
        const result = [];
        const traverse = (node) => {
            if (!node) return;
            result.push(node.value);
            for (const child of node.children) {
                traverse(child);
            }
        };

        traverse(this.root);
        return result;
    }

    inOrder() {
        const result = [];
        const traverse = (node) => {
            if (!node) return;
            for (const child of node.children) {
                traverse(child);
            }
        };

        traverse(this.root);
        return result;
    }

    postOrder() {
        const result = [];
        const traverse = (node) => {
            if (!node) return;
            for (const child of node.children) {
                traverse(child);
            }
            result.push(node.value);
        };

        traverse(this.root);
        return result;
    }

    levelOrder() {
        const result = [];
        const queue = [this.root];
        while (queue.length > 0) {
            const node = queue.shift();
            result.push(node.value);
            for (const child of node.children) {
                queue.push(child);
            }
        }
        return result;
    }
}