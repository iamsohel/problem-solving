class ListNode {
    value: number;
    next: ListNode;
    constructor(value: number){
        this.value = value;
    }
}

class LinkedList {
    head: ListNode;
    tail: ListNode;
    size: number;

    private isEmpty(): boolean {                                 
        return this.head == null;
    }


    addLast(value: number){
        let node: ListNode = new ListNode(value);
        if(this.isEmpty()){
            this.head = this.tail = node;
        } else {
            this.tail.next = node;
            this.tail = node;
        }
    }

    addFirst(value: number){
        let node: ListNode = new ListNode(value);
        if(this.isEmpty()){
            this.head = this.tail = node;
        } else {
            node.next = this.head;
            this.head = node;
        }
    }

    reverse()  {
        // 1 -> 2-> 3 -> null
        if(this.isEmpty()) return;

        var previous = this.head;
        var current = this.head.next;
        while(current){
            let elem = current.next;
            current.next = previous;
            previous = current;
            current = elem;
        }
        this.tail = this.head;
        this.head = previous;
    }

    toArray() {
        let array = [];
        let index = 0;
        while(this.head){
            array[index] = this.head.value;
            this.head = this.head.next;
            index++;
        }
        return array;
    }

}

let list: LinkedList = new LinkedList();
list.addFirst(1)
list.addLast(2)
list.addLast(3)
list.reverse()
let arr = list.toArray();
console.log(arr)