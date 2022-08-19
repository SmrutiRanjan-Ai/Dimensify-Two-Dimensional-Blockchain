import node
class twoDNode(node.Node):
    def __init__(self, creation_time, node_id, bandwidth, balance):
        super().__init__(creation_time, node_id, bandwidth, balance)
        self.miner_primary=False
        self.miner_2d = True