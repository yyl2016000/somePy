class Node:
    def __init__(self,value = None, lchild = None, rchild = None):
        self.value = value
        self.lchild = lchild
        self.rchild = rchild

def PreTraverse(root: Node):
    if root == None:
        return
    print(root.value, end=' ')
    PreTraverse(root.lchild)
    PreTraverse(root.rchild)

def MidTraverse(root: Node):
    if root == None:
        return
    MidTraverse(root.lchild)
    print(root.value, end=' ')
    MidTraverse(root.rchild)

def AfterTraverse(root: Node):
    if root == None:
        return
    AfterTraverse(root.lchild)
    AfterTraverse(root.rchild)
    print(root.value, end=' ')

def main():
    root = Node('D',Node('B',Node('A'),Node('C')),Node('E',rchild=Node('G',Node('F'))))
    PreTraverse(root)
    print('\n')
    MidTraverse(root)
    print('\n')
    AfterTraverse(root)

if __name__ == '__main__':
    main()