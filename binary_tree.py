class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            # Add data in left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
            # Add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

        # Visit left tree
        if self.left:
            elements += self.left.in_order_traversal()

        # Visit base mode
        elements.append(self.data)

        # Visit right tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def delete(self, val):
        if val < self.data:
            if self.left:
                self.left = self.left.delete(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.right

            min_val = self.right.find_min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self

    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            # Val might be in left subtree
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            # Val might be in right subtree
            if self.right:
                return self.right.search(val)
            else:
                return False

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34]
    countries = ["India", "Pakistan", "Germany", "USA", "China", "India", "UK", "USA"]
    initials = ["L", "E", "E", "A", "N", "N", "E", "Y", "A", "N", "G", "E", "L", "E", "S"]

    numbers_tree = build_tree(numbers)
    country_tree = build_tree(countries)
    initial_tree = build_tree(initials)

    numbers_tree.delete(20)
    initial_tree.delete("N")

    print(initial_tree.in_order_traversal())
    # print("UK is in the list?", country_tree.search("UK"))
    # print("Sweden is in the list?", country_tree.search("Sweden"))
    # print("After deleting 20",  numbers_tree.in_order_traversal())

    print("Building tree with these elements: ", initials)
    print("After deleting E in order traversal: ",  initial_tree.in_order_traversal())

