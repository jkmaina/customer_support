def add_message(state, role, content):
    state["messages"].append({
        "role": role,
        "content": content
    })
    if role == "user":
        state["turn_count"] += 1
    return state