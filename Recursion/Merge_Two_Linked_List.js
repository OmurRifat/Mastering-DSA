/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
/* var mergeTwoLists = function(list1, list2) {
    let dummy = new ListNode(0);  // dummy node to simplify merging
    let current = dummy;

    while (list1 !== null && list2 !== null) {
        if (list1.val <= list2.val) {
            current.next = list1;
            list1 = list1.next;
        } else {
            current.next = list2;
            list2 = list2.next;
        }
        current = current.next;
    }

    // Attach remaining nodes (if any)
    current.next = list1 !== null ? list1 : list2;

    return dummy.next;  // return merged list starting from the real head
}; */

var mergeTwoLists = function (list1, list2) {
    if (!list1) return list2;     // If list1 is null, return list2
    if (!list2) return list1;     // If list2 is null, return list1

    if (list1.val < list2.val) {
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    } else {
        list2.next = mergeTwoLists(list1, list2.next);
        return list2;
    }
};