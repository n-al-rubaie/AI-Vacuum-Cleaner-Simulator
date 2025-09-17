import pytest
from unittest.mock import Mock, MagicMock
from vacuum_cleaner_main import VacuumPlanning, agent_label, is_agent_label, XYSearchAgent, searchTypes

# -------------------------
# Tests for agent_label and is_agent_label
# -------------------------
def test_agent_label_direction():
    agent = Mock()
    agent.direction = 'UP'
    assert agent_label(agent) == '^'
    agent.direction = 'DOWN'
    assert agent_label(agent) == 'v'
    agent.direction = 'LEFT'
    assert agent_label(agent) == '<'
    agent.direction = 'RIGHT'
    assert agent_label(agent) == '>'

def test_is_agent_label():
    assert is_agent_label('^')
    assert is_agent_label('v')
    assert is_agent_label('<')
    assert is_agent_label('>')
    assert not is_agent_label('X')
    assert not is_agent_label('')

# -------------------------
# Tests for XYSearchAgent
# -------------------------
def test_xy_search_agent_init():
    agent = XYSearchAgent(program=None, loc=(0, 0))
    assert agent.location == (0, 0)
    assert agent.direction is not None
    assert agent.stepCount == 0
    assert agent.searchType == searchTypes[0]

# -------------------------
# Tests for VacuumPlanning
# -------------------------
def test_vacuum_planning_init():
    mock_env = Mock()
    mock_env.agent.location = (1, 1)
    mock_env.things = {}
    mock_env.turnCostOn = False
    planner = VacuumPlanning(mock_env, 'BFS')
    assert planner.state == (1, 1)
    assert planner.env == mock_env
    assert planner.agent == mock_env.agent
    assert planner.searchType == 'BFS'

def test_vacuum_planning_result():
    mock_env = Mock()
    mock_env.agent.location = (1, 1)
    planner = VacuumPlanning(mock_env, 'BFS')
    # Test moving in each direction
    assert planner.result((1, 1), 'UP') == [1, 2]
    assert planner.result((1, 1), 'DOWN') == [1, 0]
    assert planner.result((1, 1), 'LEFT') == [0, 1]
    assert planner.result((1, 1), 'RIGHT') == [2, 1]

def test_vacuum_planning_goal_test():
    mock_env = Mock()
    mock_env.agent.location = (0, 0)
    mock_env.some_things_at.return_value = True
    planner = VacuumPlanning(mock_env, 'BFS')
    assert planner.goal_test((0, 0)) is True
    mock_env.some_things_at.return_value = False
    assert planner.goal_test((0, 0)) is False

def test_compute_turn_cost():
    mock_env = Mock()
    mock_env.agent.location = (0, 0)
    planner = VacuumPlanning(mock_env, 'BFS')
    # No turn
    assert planner.computeTurnCost('UP', 'UP') == 0
    # 180-degree turn
    assert planner.computeTurnCost('UP', 'DOWN') == 1
    # 90-degree turn
    assert planner.computeTurnCost('UP', 'LEFT') == 0.5
    assert planner.computeTurnCost('LEFT', 'UP') == 0.5

def test_find_min_manhattan_dist():
    mock_env = Mock()
    mock_env.agent.location = (0, 0)
    mock_env.dirtyRooms = [(1, 2), (3, 3)]
    planner = VacuumPlanning(mock_env, 'BFS')
    assert planner.findMinManhattanDist((0, 0)) == 3
    assert planner.findMinManhattanDist((2, 2)) == 1

def test_h_function_returns_min_distance():
    mock_env = Mock()
    mock_env.agent.location = (0, 0)
    mock_env.dirtyRooms = [(1, 2), (3, 3)]
    planner = VacuumPlanning(mock_env, 'BFS')
    node = Mock()
    node.state = (0, 0)
    assert planner.h(node) == 3
