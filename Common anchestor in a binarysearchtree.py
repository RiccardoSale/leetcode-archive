class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # if we have all the node requested p and q in a subtree (like all on the left)
        # the result will be the upper node so i dont need to take care of that
        # i only need to return the last valid node i found = to p or q

        # the other case if i found one in the right and one in the left in that case i need to return
        # the node that i am in in the moment
        # (because is the new common ancestor)

        # found what we want or there is nothing
        if (root == p or root == q or not root): return root

        # recursion
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root  # found common ancestor
        elif left:
            return left
        elif right:
            return right