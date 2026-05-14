class Dynasty:
    def __init__(self):
        self.leaders = []

    def add_leader(self, leader):
        self.leaders.append({
            "name": leader.name,
            "age": leader.age,
            "children": len(leader.children)
        })
