from itertools import chain

graph = {
    "1": {"in": ["4"], "out": ["2", "3"]},
    "2": {"in": ["1"], "out": ["4"]},
    "3": {"in": ["1"], "out": ["4"]},
    "4": {"in": ["2", "3"], "out": ["1"]},
}


class Site:
    def __init__(self, ID):
        self.ID = ID
        self.out = set()
        self.inc = {self.ID}
        self.ninc = set()
        self.inp = dict()

    def check_for_change(self, prev_site):
        new_inc = set.union(self.inc, prev_site.inc)
        new_ninc = set.union(self.ninc, prev_site.ninc)

        self.inp[prev_site.ID] = True

        if (len(new_inc) != len(self.inc)) or (len(new_ninc) != len(self.ninc)):
            self.inc = new_inc
            self.ninc = new_ninc
            return True

        return False

    def check_if_decided(self):
        return True if self.inc == self.ninc else False

    def check_neighbours(self):
        if all(self.inp.values()):
            self.ninc.add(self.ID)
            self.inp = {k: False for k in self.inp.keys()}


def parse_graph(graph: dict):

    sites = []

    for site_id in graph.keys():
        tmp_site = Site(site_id)
        tmp_site.out = set(graph[site_id]["out"])
        tmp_site.inp = {k: False for k in graph[site_id]["in"]}
        sites.append(tmp_site)

    return sites


def find_by_id(sites, ID):
    return next((site for site in sites if site.ID == ID), None)


def finn_algorithm(sites, init_site_id: str):
    init_site = find_by_id(sites, init_site_id)
    init_flag = True
    site_queue = iter([init_site])
    current_site = next(site_queue)
    while True:
        current_site.check_neighbours()
        site_queue = chain(
            iter(
                [
                    find_by_id(sites, out_id)
                    for out_id in current_site.out
                    if find_by_id(sites, out_id).check_for_change(current_site)
                ]
            ),
            site_queue,
        )

        if current_site.check_if_decided():
            print("Site %s decided!" % current_site.ID)
            break
        else:
            current_site = next(site_queue)

    pass


if __name__ == "__main__":

    sites = parse_graph(graph)
    finn_algorithm(sites, "1")