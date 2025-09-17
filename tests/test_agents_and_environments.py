# tests/test_agents_and_environments.py

import pytest
from agents_and_environments import Agent, VacuumEnvironment, Dirt, Wall, Direction, XYEnvironment, Obstacle

# --------------------------
# Environment Tests
# --------------------------

def test_vacuum_environment_initialisation():
    """Test that the VacuumEnvironment initialises correctly with given width and height."""
    env = VacuumEnvironment(width=5, height=5)
    assert env.width == 5
    assert env.height == 5
    # Check that walls have been added around the perimeter
    wall_count = sum(1 for t in env.things if isinstance(t, Wall))
    assert wall_count > 0, "Walls should be placed around the environment"

def test_add_agent_to_environment():
    """Test adding an agent to the environment sets its location and includes it in agents list."""
    env = VacuumEnvironment(5, 5)
    agent = Agent()
    env.add_thing(agent, location=(2, 2))
    assert agent in env.agents
    assert agent.location == (2, 2)

# --------------------------
# Dirt and Cleaning Tests
# --------------------------

def test_agent_can_suck_dirt():
    """Test that an agent cleaning dirt increases performance and removes the dirt."""
    env = VacuumEnvironment(5, 5)
    agent = Agent()
    env.add_thing(agent, location=(2, 2))
    dirt = Dirt()
    env.add_thing(dirt, location=(2, 2))
    
    # Dirt is present
    assert env.some_things_at((2, 2), Dirt)
    
    # Agent executes Suck action
    env.execute_action(agent, 'Suck')
    
    # Dirt should be removed
    assert not env.some_things_at((2, 2), Dirt)
    # Performance should increase by 100 minus 1 for the action
    assert agent.performance == 99

# --------------------------
# Agent Movement Tests
# --------------------------

def test_agent_movement_and_bump():
    """Test that agent bumps into obstacle and location remains the same."""
    env = VacuumEnvironment(5, 5)
    agent = Agent()
    agent.direction = Direction(Direction.R)  # Facing right
    env.add_thing(agent, location=(1, 1))
    env.add_thing(Wall(), location=(2, 1))  # Obstacle directly in front
    
    # Attempt to move forward into wall
    env.execute_action(agent, 'Forward')
    
    # Agent should detect bump
    assert agent.bump is True
    # Location should remain unchanged
    assert agent.location == (1, 1)

def test_agent_can_move_forward_free_space():
    """Test agent moves forward successfully when no obstacle."""
    env = VacuumEnvironment(5, 5)
    agent = Agent()
    agent.direction = Direction(Direction.R)  # Facing right
    env.add_thing(agent, location=(1, 1))
    
    # Move forward into empty space
    env.execute_action(agent, 'Forward')
    
    # Location should update
    assert agent.location == (2, 1)
    # No bump
    assert agent.bump is False

# --------------------------
# Direction Class Tests
# --------------------------

def test_direction_addition_turns():
    """Test that Direction correctly updates when turning left or right."""
    d = Direction(Direction.R)  # Initially facing right
    d_left = d + Direction.L
    d_right = d + Direction.R
    assert d_left.direction == Direction.U, "Turning left from right should face up"
    assert d_right.direction == Direction.D, "Turning right from right should face down"

def test_direction_move_forward():
    """Test that move_forward updates position correctly."""
    d = Direction(Direction.U)  # Facing up
    new_pos = d.move_forward((2, 2))
    assert new_pos == (2, 3), "Moving up should increase y-coordinate by 1"

# --------------------------
# XYEnvironment Tests
# --------------------------

def test_things_near_returns_correct_things():
    """Test that things_near returns only things within perceptible distance."""
    env = XYEnvironment(width=5, height=5)
    agent = Agent()
    env.add_thing(agent, location=(2, 2))
    obj_near = Dirt()
    obj_far = Dirt()
    env.add_thing(obj_near, location=(2, 3))  # Within radius 1
    env.add_thing(obj_far, location=(4, 4))   # Outside radius 1
    
    nearby = env.things_near((2, 2))
    # Only obj_near should be in results
    nearby_things = [thing for thing, _ in nearby]
    assert obj_near in nearby_things
    assert obj_far not in nearby_things

# --------------------------
# Obstacle Interaction Tests
# --------------------------

def test_move_to_with_obstacle():
    """Test that move_to returns True if an obstacle blocks the agent."""
    env = XYEnvironment(5,5)
    agent = Agent()
    env.add_thing(agent, location=(1,1))
    obstacle = Obstacle()
    env.add_thing(obstacle, location=(2,1))
    
    bumped = env.move_to(agent, (2,1))
    assert bumped is True
    # Location should not change
    assert agent.location == (1,1)
