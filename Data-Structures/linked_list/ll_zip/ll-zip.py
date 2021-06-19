from linked_list.linked_list import LinkedList,Node


def zipLists(ll1, ll2):

        current1 = ll1.head
        current2 = ll2.head
        while current1:
            if current2:
                save1 = current1.next
                current1.next = current2
                
                if save1:
                    save2 = current2.next
                    current2.next = save1
                     
                if not save2:
                    break
                
                current1 = save1
                current2 = save2
        return ll1


if __name__=="__main__":
    ll1= LinkedList()
    ll1.append('T')
    ll1.append('A')
    ll1.append('0')
    ll1.append('A')
    ll1.append('T')
    
    print(ll1)
    
    ll2= LinkedList()
    ll2.append(7)
    ll2.append(-8)

    ll2.insertAfter(7, 8)
    print(ll2)

    zip_ll = zipLists(ll2,ll1)
    print(zip_ll)    

