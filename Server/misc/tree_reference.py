class TreeReference:
    def __init__(self, origin, to):
        self.origin = origin
        self.to = to
        self.distance_between_trees = origin.x - to.x
        self.weight = origin.distance_to_road + self.distance_between_trees - to.distance_to_road