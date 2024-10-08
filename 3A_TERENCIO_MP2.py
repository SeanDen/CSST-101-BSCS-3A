# -*- coding: utf-8 -*-
"""3A_TERENCIO_MP2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19YXKq_lXUhcc_9_qpVa9JKVCfo2T5xF5

# 1. Basic Operations
"""

def and_operation(p, q):
    """Logical conjunction (AND)."""
    return p and q

def or_operation(p, q):
    """Logical disjunction (OR)."""
    return p or q

def not_operation(p):
    """Logical negation (NOT)."""
    return not p

def implies_operation(p, q):
    """Logical implication (IMPLIES)."""
    return not p or q

"""# 2. Evaluate Logical Statements
We can create a function that parses a string representation of the logical expression and evaluates it based on the provided truth values.
"""

def evaluate(statement, values):
    statement = statement.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')

    try:
        return eval(statement, {}, values)
    except NameError as e:
        raise ValueError(f"Unknown token in statement: {e}")

"""# Example Usage
The function first replaces logical operators in the string (AND, OR, NOT) with their Python equivalents (and, or, not).

The eval() function then evaluates the logical expression using the provided truth values (variables) from the values dictionary.
"""

def evaluate(statement, values):
    statement = statement.replace('AND', 'and').replace('OR', 'or').replace('NOT', 'not')

    try:
        return eval(statement, {}, values)
    except NameError as e:
        raise ValueError(f"Unknown token in statement: {e}")

"""# Predicate Logic with Quantifiers
1. Universal Quantifier (∀)
The forall function checks if a given predicate holds true for all elements in a specified domain.
2. Existential Quantifier (∃)
The exists function checks if there is at least one element in the specified domain for which the predicate holds true.
Implementation
Here’s how you can implement these functions in Python:
"""

def forall(predicate, domain):
    """Evaluate the universal quantifier (FOR ALL)."""
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    """Evaluate the existential quantifier (EXISTS)."""
    return any(predicate(x) for x in domain)

"""# Example Usage of Quantifiers"""

def is_even(x):
    return x % 2 == 0

def is_positive(x):
    return x > 0

def forall(predicate, domain):
    return all(predicate(x) for x in domain)

def exists(predicate, domain):
    return any(predicate(x) for x in domain)

domain = range(-5, 6)

all_even = forall(is_even, domain)
print(f"All numbers are even: {all_even}")

any_even = exists(is_even, domain)
print(f"Any number is even: {any_even}")

all_positive = forall(is_positive, domain)
print(f"All numbers are positive: {all_positive}")

any_positive = exists(is_positive, domain)
print(f"Any number is positive: {any_positive}")

"""#**AI Agent Development**
a game scenario where the agent decides the best move based on certain conditions. For this example, imagine a game where the agent can choose between three actions: "move left," "move right," and "stay put." The decision is based on the following conditions

#is_close_to_target: Checks if the current position is close enough to the target position.

#is_obstacle_near: Checks if there are any obstacles near the current position.

#decide_move: Determines the best move based on the current position, target position, and obstacles:

If the agent is close to the target, it stays put.
If there are no obstacles, it moves towards the target.
If obstacles are near, it chooses a move that avoids obstacles while trying to get closer to the target.
"""

def is_close_to_target(current_position, target_position, threshold=1):
    return abs(current_position - target_position) <= threshold

def is_obstacle_near(current_position, obstacles, threshold=1):
    return any(abs(current_position - obs) <= threshold for obs in obstacles)

def decide_move(current_position, target_position, obstacles):
    if is_close_to_target(current_position, target_position):
        return "stay put"

    if not is_obstacle_near(current_position, obstacles):
        if current_position < target_position:
            return "move right"
        else:
            return "move left"

    # If there are obstacles near, make a safe move
    if current_position < target_position:
        return "move right"
    else:
        return "move left"

# Define the scenario
current_position = 5
target_position = 10
obstacles = [7, 8]

# Get the decision
move = decide_move(current_position, target_position, obstacles)
print(f"The agent decides to: {move}")
