import pytest
from search_algorithms import *

# -------------------------------
# SimpleProblem for testing basic search
# -------------------------------
class SimpleProblem(Problem):
    def __init__(self):
        super().__init__(initial=(0,), goal=(2,))

    def actions(self, state):
        # return possible actions as tuples
        return [(1,), (2,)]

    def result(self, state, action):
        # add action tuple to state tuple
        return (state[0] + action[0],)

    def h(self, node):
        # heuristic for A* / greedy
        return self.goal[0] - node.state[0]

@pytest.fixture
def simple_problem():
    return SimpleProblem()

def test_node_expand():
    problem = SimpleProblem()
    node = Node((0,))
    children = node.expand(problem)
    assert all(isinstance(child, Node) for child in children)

def test_bfs(simple_problem):
    node, explored = breadth_first_graph_search(simple_problem)
    assert node.state == simple_problem.goal

def test_dfs(simple_problem):
    node, explored = depth_first_graph_search(simple_problem)
    assert node.state == simple_problem.goal

def test_astar(simple_problem):
    node, explored = astar_search(simple_problem)
    assert node.state == simple_problem.goal

def test_uniform_cost(simple_problem):
    node, explored = uniform_cost_search(simple_problem)
    assert node.state == simple_problem.goal

def test_greedy_best_first(simple_problem):
    node, explored = greedy_best_first_graph_search(simple_problem)
    assert node.state == simple_problem.goal

# -------------------------------
# GraphProblem tests
# -------------------------------
@pytest.fixture
def sample_graph():
    graph_dict = {'A': {'B': 1, 'C': 2}, 'B': {'D': 3}, 'C': {'D': 1}, 'D': {}}
    g = GraphProblem('A', 'D', Graph(graph_dict))
    return g

def test_bfs_graph(sample_graph):
    node, explored = breadth_first_graph_search(sample_graph)
    assert node.state == sample_graph.goal

def test_dfs_graph(sample_graph):
    node, explored = depth_first_graph_search(sample_graph)
    assert node.state == sample_graph.goal

def test_astar_graph(sample_graph):
    node, explored = astar_search(sample_graph)
    assert node.state == sample_graph.goal

def test_uniform_cost_graph(sample_graph):
    node, explored = uniform_cost_search(sample_graph)
    assert node.state == sample_graph.goal

def test_greedy_best_first_graph(sample_graph):
    node, explored = greedy_best_first_graph_search(sample_graph)
    assert node.state == sample_graph.goal

# -------------------------------
# PeakFindingProblem tests
# -------------------------------
@pytest.fixture
def peak_problem():
    grid = [
        [1, 2],
        [3, 4]
    ]
    return PeakFindingProblem((0, 0), grid)

def test_peak_actions(peak_problem):
    actions = peak_problem.actions((0,0))
    # make sure the allowed actions are valid
    for a in actions:
        assert a in peak_problem.defined_actions

def test_peak_result(peak_problem):
    # check result returns correct next state
    result = peak_problem.result((0,0), 'E')
    assert result == (1,0)  # 'E' moves x + 1
