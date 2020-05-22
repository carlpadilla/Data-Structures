

# add to the back of the text buffer
# add to the front of a text buffer
# delete from the back of the text buffer
# delete from the front of a text buffer

# join text buffers together

# add to middle

# array vs DLL
# array: add to back - O(1)
# array: add to front: O(n)

# array: delete from back: O(1)
# array: delete from front: O(n)

# array: join text buffers together: O(n)

# DLL: add to the back: O(1)
# DLL: add to the back: O(1)
# DLL: join text buffers together: O(1)


from doubly_linked_list import DoublyLinkedList
import sys

sys.path.append('./doubly_linked_list')


class TextBuffer:
    def __init__(self):
        self.storage = DoublyLinkedList()

    def __str__(self):
        pass

    def join(self, other_buffer):
        pass

    def append(self, string_to_add):
        pass

    def prepend(self, string_to_add):
        pass

    def delete_from_front(self):
        pass

      def delete_from_back(self):
        pass
