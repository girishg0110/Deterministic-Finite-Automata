# Calculate index of DFA. Minimal number of states needed to represent its language.
# k-equivalence classes.

import networkx as nx


class DFA():
    # DFA = (Q, \Sigma, \delta, q_0, F) --> (nodes, _, edges, start node, accepting nodes)
    #       Alphabet implicit from \delta.
    # Graph representation as MultiDiGraph.
    # Node-level features: start and accepting states.
    # Edge-level features: token
    #   Edges are (start_state, end_state, input)
    def __init__(self, states, edges, start_node, accepting_nodes):
        self.DFA = nx.MultiDiGraph()
        for s in states:
            self.DFA.add_node(s, start=(s == start_node),
                              accept=(s in accepting_nodes))
        for e in edges:
            self.DFA.add_edge(*e[:2], token=e[2])
        self.start_node = start_node

    def check_acceptance(self, string):
        current_node = self.start_node
        for i in string:
            print("---", current_node, i)
            # Find which state to transition to.
            for n in self.DFA[current_node]:
                print(
                    n, type(self.DFA.edges[current_node, n, 0]["token"]), type(i))
                if (self.DFA.edges[current_node, n, 0]["token"] == i):
                    print("match!", n)
                    current_node = n
                    break
        return (current_node, self.DFA.nodes[current_node]["accept"])

    # k-equivalence classes.
    # def k_equivalence_classes(self, k):
        # Test all k^n strings from all n nodes.

    # Regular expression conversion.
    # Index of DFA.
    # Minimal DFA.
    # accepts? function(string)
    #


if __name__ == "__main__":
    exactly_one_one = DFA(
        ["A", "B", "C"],
        [("A", "A", "0"), ("A", "B", "1"), ("B", "B", "0"),
         ("B", "C", "1"), ("C", "C", "0"), ("C", "C", "1")],
        "A",
        ["B"]
    )

    print(
        exactly_one_one.check_acceptance("010"),
        exactly_one_one.check_acceptance("011")
    )
