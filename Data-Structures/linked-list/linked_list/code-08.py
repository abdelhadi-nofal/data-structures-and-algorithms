from linked_list import Node , linked_list



def zip(ll1,ll2):
    # ll1 = linked_list.LinkedList()
    # ll2 = linked_list.LinkedList()

    current1=ll1.head
    current2=ll2.head

    while current1:
        current1.next = current2
        current1 = current1.next
        current2 = current2.next

    return ll1


if __name__=="__main__":
    ll1= linked_list.LinkedList()
    ll1.append(4)
    
    ll1.append(-1)
    ll1.append('s')
    ll1.insertBefore(4, 5)
    ll1.insertBefore(-1, 9)
    ll1.insertAfter(4, 8)
    ll1.insertAfter(-1, 98)

    print(ll1)







