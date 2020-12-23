from itertools import chain

# graph = {'0': {'in': ['1'], 'out': ['2']}, '1': {'in': ['3'], 'out': ['0', '2']},
#         '2': {'in': ['0', '1'], 'out': ['4']}, '3': {'in': ['4'], 'out': ['1']},
#         '4': {'in': ['2'], 'out': ['3']}}


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

    def check_for_change(self, inc_message, ninc_message):
        new_inc = set.union(self.inc, inc_message)
        new_ninc = set.union(self.ninc, ninc_message)

        if (len(new_inc) != len(self.inc)) or (len(new_ninc) != len(self.ninc)):
            self.inc = new_inc
            self.ninc = new_ninc
            return True
        
        return False


def parse_graph(graph: dict):

    sites = []

    for site_id in graph.keys():
        tmp_site = Site(site_id)
        tmp_site.out = set(graph[site_id]["out"])
        tmp_site.inp = {k: False for k in graph[site_id]["in"]}
        sites.append(tmp_site)


def find_by_id(sites, ID):
    return next((site for site in sites if site.ID == ID), None)


def finn_algorithm(sites, init_site_id: str):
    init_site = find_by_id(
        sites, init_site_id
    )
    init_flag = True
    site_queue = iter([init_site])
    current_site = next(site_queue)
    while True:
        # TODO: Сделать заполнение очереди через изменение сайта
        pass
    pass


if __name__ == "__main__":

    parse_graph(graph)