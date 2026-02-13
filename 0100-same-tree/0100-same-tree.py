# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            for _ in range(len(q1)):
                node_q = q1.popleft()
                node_p = q2.popleft()

                if not node_q and not node_p:
                    continue
                if node_q is None or node_p is None or node_q.val != node_p.val:
                    return False

                q1.append(node_q.left)
                q1.append(node_q.right)
                q2.append(node_p.left)
                q2.append(node_p.right)

        return True

