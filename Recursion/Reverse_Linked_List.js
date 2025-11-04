/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var reverseList = function(head) {
    if(!head) return head;
    let current = head;
    let previous = null;
    while(current){ // 1, 2, 3
        /* For node 1 */
        // let newNode = current.next // newNode = Node(2)
        // current.next = previous; // Node(1).next = null | current = 1 -> null
        // previous = current; // previous = 1 -> null
        // current = newNode; // current = Node(2)

        // /* For node 2 */
        // let newNode = current.next // newNode = Node(3)
        // current.next = previous; // Node(2).next = 1 -> null | current = 2 -> 1 -> null
        // previous = current; // previous = 2 -> 1 -> null
        // current = newNode; // current = Node(2)

        /* For node 3 */
        let newNode = current.next // newNode = Node(null)
        current.next = previous; // Node(3).next = 2 -> 1 -> null | current = 3 -> 2 -> 1 -> null
        previous = current; // previous = 3 -> 2 -> 1 -> null
        current = newNode; // current = Node(null)
    }
    head = previous;
    return head;
};

// Node class
class ListNode {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

// Create linked list from array
function arrayToList(arr) {
    if (arr.length === 0) return null;
    let head = new ListNode(arr[0]);
    let current = head;
    for (let i = 1; i < arr.length; i++) {
        current.next = new ListNode(arr[i]);
        current = current.next;
    }
    return head;
}

// Convert linked list back to array
function listToArray(head) {
    let arr = [];
    while (head) {
        arr.push(head.val);
        head = head.next;
    }
    return arr;
}

var reverseList = function(head) {
    if (!head || !head.next) return head;

    let newHead = reverseList(head.next);
    head.next.next = head;
    head.next = null;

    return newHead;
}


// Example 1
let head1 = arrayToList([1, 2, 3, 4, 5]);
let reversed1 = reverseList(head1);
console.log(listToArray(reversed1));  // Output: [5, 4, 3, 2, 1]

// Example 2
let head2 = arrayToList([1, 2]);
let reversed2 = reverseList(head2);
console.log(listToArray(reversed2));  // Output: [2, 1]

// Example 3
let head3 = arrayToList([]);
let reversed3 = reverseList(head3);
console.log(listToArray(reversed3));  // Output: []
