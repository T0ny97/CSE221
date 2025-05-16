def build_postorder(inorder, preorder):
    if not preorder:
        return []
    
    root = preorder[0]  
    index = inorder.index(root)  
    
    l_tree = build_postorder(inorder[:index], preorder[1:index+1])
    r_tree = build_postorder(inorder[index+1:], preorder[index+1:])
    
    return l_tree + r_tree + [root]


n = int(input())
in_arr = list(map(int, input().split()))
pre_arr = list(map(int, input().split()))


post_arr = build_postorder(in_arr,pre_arr)
# Print result
for i in post_arr:
    print(i,end=" ")
