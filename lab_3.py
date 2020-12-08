from itertools import chain

# graph = {'0': {'in': ['5'], 'out': ['1']}, '1': {'in': ['0'], 'out': ['2']}, '2': {'in': ['1'], 'out': ['3']},
#          '3': {'in': ['2'], 'out': ['4', '5']}, '4': {'in': ['3'], 'out': ['5']}, '5': {'in': ['3', '4'], 'out': ['0']}}

# D = 5


graph = {'1': {'in': ['4'], 'out': ['2', '3']}, '2': {'in': ['1'], 'out': ['4']},
        '3': {'in': ['1'], 'out': ['4']}, '4': {'in': ['2', '3'], 'out': ['1']}}

D = 3

class Site:

    def __init__(self, ID: str):

        self.ID = ID
        # self.inc = set(self.ID)
        # self.ninc = set()
        self.rec = dict()
        self.sent = 0
        self.out = []

    def get_min_rec(self):
        return min(self.rec.values())

    def check_if_decided(self):
        return True if max(self.rec.values()) == D and self.sent == D else False

    def check_if_expandable(self):
        if self.get_min_rec() >= self.sent and self.sent < D:
            return True
        else:
            return False

    def __str__(self):
        return 'Rec = %s\n' % self.rec + 'Self = %d\n' % self.sent

def parse_graph(graph: dict):

    sites = []
    for (key, params) in graph.items():
        site = Site(key)
        site.rec = {k: 0 for k in params['in']}
        site.out = params['out']
        sites.append(site)
    return sites

def find_by_id(sites, ID):
    return next((site for site in sites if site.ID == ID), None)



def phase_algorithm(sites, iniID : str):
    iniSite = find_by_id(sites, iniID)
    siteQueue = iter([iniSite])
    prevSite = next(siteQueue)
    while True:
        # siteQueue = iter([find_by_id(sites, outID) for outID in prevSite.out] + siteQueue)
        if prevSite.check_if_expandable():
            siteQueue = chain(iter([find_by_id(sites, outID) for outID in prevSite.out]), siteQueue)
            prevSite.sent += 1
        site = next(siteQueue)
        if prevSite.check_if_decided():
            print('Site #%s decided!\n' % prevSite.ID)
            break
        if len(site.rec) == 1:
            site.rec[list(site.rec.keys())[0]] += 1
        else:
            site.rec[prevSite.ID] += 1

        prevSite = site


if __name__ == "__main__":
    sites = parse_graph(graph)
    phase_algorithm(sites, '1')
    for site in sites:
        print(str(site))