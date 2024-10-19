from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, PositiveInt

# Pydantic model for validating inputs and error handling
class Input(BaseModel):
    x_capacity:PositiveInt
    y_capacity:PositiveInt
    z_amount_wanted:PositiveInt

app = FastAPI()

# API endpoint
@app.post("/water-jug-calculator")
def get_solution(input: Input):
    global jug1
    global jug2
    global goal
    jug1 = input.x_capacity
    jug2 = input.y_capacity
    goal = input.z_amount_wanted
    return JSONResponse(content = {"solution": water_jug_solver()})

#Helper function
def is_solved(state):
    return goal in state

#Helper function
def get_neighbors(state):
    a_to_b = min(state[0], jug2 - state[1])
    b_to_a = min(state[1], jug1 - state[0])
    return [
        ((jug1, state[1]), f'Fill bucket X'),
        ((state[0], jug2), f'Fill bucket Y'),
        ((0, state[1]), f'Empty bucket X'),
        ((state[0], 0), f'Empty bucket Y'),
        ((state[0] - a_to_b, state[1] + a_to_b),
         f'Transfer from bucket X to bucket Y'),
        ((state[0] + b_to_a, state[1] - b_to_a),
         f'Transfer from bucket Y to bucket X')
    ]

# Main algorithm
# Time complexity O(n*m)
def water_jug_solver():
    state = (0, 0)
    q = [state]
    visited = {state}
    prev = {state: None}
    action = {}

    while len(q) > 0:
            curr_state = q.pop(0)
            if is_solved(curr_state):
                    break

            for neighbor, action_description in get_neighbors(curr_state):
                    if neighbor not in visited:
                            prev[neighbor] = curr_state
                            action[neighbor] = action_description
                            visited.add(neighbor)
                            q.append(neighbor)

    if not is_solved(curr_state):
            return('No solution...')
    else:
            instructions = []

            #Construct list of dictionaries, each dictionary represents one step of the solution
            while prev[curr_state] is not None:
                curr_dict = {
                    "step": int,
                    "bucketX": curr_state[0],
                    "bucketY": curr_state[1],
                    "action" : action[curr_state]
                }
                instructions.insert(0, curr_dict)
                curr_state = prev[curr_state]

            i = 1
            for d in instructions:
                d["step"] = i
                i += 1

    return(instructions)