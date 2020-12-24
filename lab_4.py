GRAPH = {
    "1": ["2", "3"],
    "2": ["1", "3", "4", "5", "6"],
    "3": ["1", "2", "7", "8"],
    "4": ["2", "5"],
    "5": ["2", "4"],
    "6": ["2", "7"],
    "7": ["3", "6"],
    "8": ["3"],
}


class Site:
    def __init__(self, ID):
        self.ID = ID
        self.out = set()

    def __repr__(self):
        return "Site: %s" % self.ID


def parse_graph(graph: dict):

    sites = []

    for site_id in graph.keys():
        tmp_site = Site(site_id)
        tmp_site.out = set(graph[site_id])
        sites.append(tmp_site)

    return sites


def find_by_id(sites, ID):
    return next((site for site in sites if site.ID == ID), None)


def wave_algorithm_lee(sites, init_site_id):
    queue = [find_by_id(sites, init_site_id)]
    bfs = []
    while len(bfs) != len(sites):
        current_site = queue.pop(0)
        bfs.append(current_site)
        queue.extend(
            [
                find_by_id(sites, site_id)
                for site_id in current_site.out
                if find_by_id(sites, site_id) not in queue
                and find_by_id(sites, site_id) not in bfs
            ]
        )
    print("All sites are visited!")
    print("Order:\n")
    for site in bfs:
        print("Site ID: %s" % site.ID)


if __name__ == "__main__":
    sites = parse_graph(GRAPH)
    wave_algorithm_lee(sites, "1")