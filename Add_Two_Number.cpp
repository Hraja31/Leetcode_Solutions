/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    {
        int carry = 0;
        ListNode* head = new ListNode();
        ListNode* headh = head;
        while(l1!=NULL || l2!= NULL)
        {
            head->next = new ListNode(0);
            head = head->next;
            int n = 0;
            if(l1!=NULL && l2!=NULL){
                n = (l1->val)+(l2->val);
                l1=l1->next;
                l2=l2->next;}
            else if(l1!=NULL){
                n = l1->val;
                l1=l1->next;}
            else{
                n = l2->val;
                l2=l2->next;}
            
            int newn = carry + n;
            if (newn <= 9){
                head->val = newn;
                carry = 0;
                }
            else{
                head->val = newn%10;
                carry = 1;
                }    
        }
        if (carry == 1)
            head->next = new ListNode(1);
        
        return headh->next;
    }
};
