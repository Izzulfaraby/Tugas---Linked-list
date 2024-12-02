class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Menambahkan node ke akhir linked list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    # Mencetak semua elemen dalam linked list
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

    # Menghapus node pertama
    def delete_first(self):
        if self.head is None:
            print("Linked List is empty.")
            return
        self.head = self.head.next

# Membuat linked list dan melakukan beberapa operasi
llist = LinkedList()
llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)
llist.append(50)

print("Linked List setelah penambahan elemen:")
llist.print_list()

# Menghapus elemen pertama
llist.delete_first()
print("Linked List setelah penghapusan elemen pertama:")
llist.print_list()
