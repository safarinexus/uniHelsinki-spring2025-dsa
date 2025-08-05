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

def find_boxes(boxes, products):
    import bisect
    from collections import defaultdict
    
    box_counts = defaultdict(int)
    for box in boxes:
        box_counts[box] += 1
    
    available_sizes = sorted(box_counts.keys())
    
    result = []
    
    for product_size in products:
        idx = bisect.bisect_left(available_sizes, product_size)
        
        box_found = -1
        
        while idx < len(available_sizes):
            box_size = available_sizes[idx]
            if box_counts[box_size] > 0:
                box_found = box_size
                box_counts[box_size] -= 1
                
                break
            idx += 1
        
        if len(result) % 1000 == 0:
            available_sizes = [size for size in available_sizes if box_counts[size] > 0]
        
        result.append(box_found)
    
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