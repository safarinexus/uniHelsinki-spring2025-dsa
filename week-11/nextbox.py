'''
You are given a collection of boxes, each with its own size. You are then given products one at a time, and you have to choose a large enough box for each product. Each box can be used only once.
Example: The box sizes are [4,4,6,8] and you are given products as follows:

The size of the product 1 is 5. You choose the box of size 6.
The size of the product 2 is 5. You choose the box of size 8.
The size of the product 3 is 4. You choose a box of size 4.
The size of the product 4 is 6. There is no box large enough.
The size of the product 5 is 1. You choose the box of size 4.

In a file nextbox.py, implement the function find_boxes that takes a list of box sizes and a list of products sizes in order of processing as parameters. The function should return a list of the box sizes chosen for each products. The box size should be -1 if no box was found for the product.
The function should be efficient even if both lists are long. The last function call in the code template tests this situation.
'''
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class TreeSet:
    def __init__(self):
        self.root = None

    def add(self, value):
        if not self.root:
            self.root = Node(value)
            return

        node = self.root
        while True:
            if node.value == value:
                return
            if node.value > value:
                if not node.left:
                    node.left = Node(value)
                    return
                node = node.left
            else:
                if not node.right:
                    node.right = Node(value)
                    return
                node = node.right

def find_boxes(boxes, products):
    avail_boxes = TreeSet()
    for i in enumerate(boxes):
        avail_boxes.add((i[1], i[0]))

    result = []
    for product in products:
        box = avail_boxes.next((product, 0))
        if box == None:
            result.append(0)
        else:
            avail_boxes.remove(box)
            result.append(box[0])
            
    return result  


if __name__ == "__main__":
    print(find_boxes([4, 4, 6, 8], [5, 5, 4, 6, 1]))
    # [6, 8, 4, -1, 4]

    print(find_boxes([1, 2, 3, 4], [1, 1, 1, 1, 1]))
    # [1, 2, 3, 4, -1]

    print(find_boxes([2, 2, 2, 2], [1, 1, 1, 1, 1, 1]))
    # [2, 2, 2, 2, -1, -1]

    print(find_boxes([1, 1, 1, 1], [2, 2]))
    # [-1, -1]

    boxes = []
    products = []
    for i in range(10**5):
        boxes.append(i % 100 + 1)
        products.append(3 * i % 97 + 1)
    result = find_boxes(boxes, products)
    print(result[42]) # 30
    print(result[1337]) # 35
    print(result[-1]) # 100