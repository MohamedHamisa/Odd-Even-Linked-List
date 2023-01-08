class Solution:
    def oddEvenList(self, head: ListNode):          
                                                               
        if not head: return head                                
                                                                
        n1, n2, head2 = head, head.next, head.next              
                                                                
        while n2 and n2.next:                                  
            n1.next, n2.next = n1.next.next, n2.next.next          
            n1, n2 = n1.next, n2.next                           
                                                                
        
        n1.next = head2                                       
                                                                
        return head
