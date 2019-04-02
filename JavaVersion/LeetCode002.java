public class LeetCode002 {

    public class ListNode {
        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
        }
    }

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        ListNode dummy = new ListNode(0);
        ListNode p = dummy;

        while (l1 != null && l2 != null) {
            p.next = new ListNode((l1.val + l2.val + carry) % 10);
            carry = (l1.val + l2.val + carry) / 10;
            l1 = l1.next;
            l2 = l2.next;
            p = p.next;
        }

        if (l2 != null) {
            while (l2 != null) {
                p.next = new ListNode((l2.val + carry) % 10);
                carry = (l2.val + carry) / 10;
                l2 = l2.next;
                p = p.next;
            }
        }

        if (l1 != null) {
            while (l1 != null) {
                p.next = new ListNode((l1.val + carry) % 10);
                carry = (l1.val + carry) / 10;
                l1 = l1.next;
                p = p.next;
            }
        }

        if (carry == 1) {
            p.next = new ListNode(1);
        }

        return dummy.next;

    }

}