class Node {
    constructor(value) {
        this.value = value
        this.next = null
    }
}

const linkedListToArray = (head) => {
    const result = [];
    while (head) {
        result.push(head.val);
        head = head.next;
    }
    return result;
}

class LinkList {
    constructor() {
        this.head = null
    }

    append(value) {
        const newNode = new Node(value)
        if (!this.head) {
            this.head = newNode
            return
        }

        let current = this.head;
        while (current.next) {
            current = current.next
        }

        current.next = newNode
    }

    prepend(value) {
        const newNode = new Node(value)
        if (!this.head) {
            this.head = newNode
            return
        }

        newNode.next = this.head
        this.head = newNode
    }

    delete(value) {
        if (!this.head) return
        else if (this.head.value === value) {
            this.head = this.head.next
            return this
        }

        let current = this.head
        while (current.next && current.next.value !== value) {
            current = current.next
        }

        if (current.next && current.next.value === value) {
            current.next = current.next?.next
        }

        return this
    }

    sort() {
        let fNode = this.head
        while (fNode !== null) {
            let current = this.head;
            while (current.next !== null) {
                if (current.value > current.next.value) {
                    let temp = current.value;
                    current.value = current.next.value;
                    current.next.value = temp;
                }
                current = current.next;
            }
            fNode = fNode.next
        }
    }

    reverse(){
        let current = this.head;
        let pre = new Node(current.value);
        current = current.next;
        while(current){
            let newNode = new Node(current.value);
            newNode.next = pre;
            pre = newNode;
            current = current.next
        }
        this.head = pre
        return this
        // console.log("CURRENT", current);
        // console.log("PREVIOUS", pre);
        // console.log("NEXT", next);
    }


    printList() {
        let current = this.head;
        while (current) {
            console.log(current.value);
            current = current.next
        }
    }
}



let testList = new LinkList();

// testList.prepend(0)
testList.append(1)
testList.append(4)
testList.append(2)
testList.append(3)
// testList.delete(0)
// testList.sort()
testList.reverse()
testList.printList()
console.log(testList);