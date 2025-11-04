class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class LinkedListStack {
    constructor(maxSize = 10) {
        this.top = null;
        this.size = 0;
        this.maxSize = maxSize;
    }

    push(data) {
        if (this.size >= this.maxSize) {
            throw new Error("Stack overflow");
        }
        const newNode = new Node(data);
        newNode.next = this.top;
        this.top = newNode;
        this.size++;
    }

    pop() {
        if (this.isEmpty()) {
            throw new Error("Stack underflow");
        }
        const poppedValue = this.top.value;
        this.top = this.top.next;
        this.size--;
        return poppedValue;
    }

    peek() {
        if (this.isEmpty()) {
            throw new Error("Stack underflow");
        }
        return this.top.value;
    }

    isEmpty() {
        return this.size === 0;
    }

    getSize() {
        return this.size;
    }

    print() {
        let current = this.top;
        let result = '';
        while (current) {
            result += `${current.value}${current.next ? ' -> ' : ''}`;
            current = current.next;
        }
        console.log(result);
    }
}

const stack = new LinkedListStack(5);
stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);
stack.push(5);
stack.pop();
stack.print();