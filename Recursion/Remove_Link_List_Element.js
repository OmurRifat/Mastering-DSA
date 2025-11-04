/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} val
 * @return {ListNode}
 */

 function ListNode(val, next) {
     this.val = (val===undefined ? 0 : val)
     this.next = (next===undefined ? null : next)
 }
/* var removeElements = function(head, val) {
    let dummy = new ListNode(0)
    dummy.next = head

    let current = dummy
    while(current){
        if(current.next.val === val){
            current.next = current.next.next
        } else{
            current = current.next
        }
    }
    return dummy.next
}; */

var removeElements = function(head, val) {
    if(!head) return null;
    head.next = removeElements(head.next, val);
    return head.val === val ? head.next : head;
};

// HELPER FUNCTION: Array -> Linklist
const arrayToLinkedList = (arr) =>{
    let dummy = new ListNode(0)
    let current = dummy
    for(let singleValue of arr){
        current.next = new ListNode(singleValue)
        current = current.next
    }
    return dummy.next
}

// HELPER FUNCTION: Linklist -> Array
const linkedListToArray = (head) =>{
    const result = [];
    while (head) {
        result.push(head.val);
        head = head.next;
    }
    return result;
}

const head1 = arrayToLinkedList([1, 2, 6, 3, 4, 5, 6]);
const newHead1 = removeElements(head1, 6);
console.log(linkedListToArray(newHead1));