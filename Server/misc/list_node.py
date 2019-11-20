class ListNode:
    def __init__(self):
        self.busy = False
        self.target = None
        self.restrictions = []
        self.back_time = 0
    
    def set_target(self, target):
        self.target = target
        self.busy = True
    
    def set_back_time(self, tree, index):
        self.back_time = index + tree.total_distance
        return self.back_time