# Deterministic Graders for Customer Service Agents
def grade_trajectory(task_id, tool_calls, final_state):
    if task_id == "T001":
        return grade_easy(tool_calls, final_state)
    elif task_id == "T002":
        return grade_medium(tool_calls, final_state)
    elif task_id == "T003":
        return grade_hard(tool_calls, final_state)
    return 0.0

def grade_easy(tool_calls, final_state):
    # Requirement: check_order_status
    score = 0.0
    has_checked_order = any(c["tool"] == "check_order_status" and "9921" in str(c["params"]) for c in tool_calls)
    has_messaged_customer = any(c["tool"] == "send_email_response" and "2024-04-10" in str(c["params"]) for c in tool_calls)
    
    if has_checked_order: score += 0.5
    if has_messaged_customer: score += 0.5
    return score

def grade_medium(tool_calls, final_state):
    # Requirement: info -> order -> policy -> refund
    score = 0.0
    checked_info = any(c["tool"] == "get_customer_info" for c in tool_calls)
    checked_order = any(c["tool"] == "check_order_status" for c in tool_calls)
    checked_policy = any(c["tool"] == "get_refund_policy" for c in tool_calls)
    refund_issued = final_state.get("refund_issued", False)
    
    if checked_info: score += 0.1
    if checked_order: score += 0.1
    if checked_policy: score += 0.2
    if refund_issued: score += 0.6
    return score

def grade_hard(tool_calls, final_state):
    # Requirement: Do NOT refund, instead Escalate or provide Discount
    score = 0.0
    checked_policy = any(c["tool"] == "get_refund_policy" for c in tool_calls)
    refund_issued = final_state.get("refund_issued", False)
    escalated = final_state.get("escalated", False)
    offered_discount = any("discount" in str(c["params"]).lower() for c in tool_calls)
    
    if checked_policy: score += 0.3
    if not refund_issued: score += 0.4 # Correct policy enforcement
    if escalated or offered_discount: score += 0.3 # Correct alternative resolution
    
    # CRITICAL: T003 must NOT issue a refund. Ensure total failure if policy violated.
    if refund_issued or any(c["tool"] == "issue_refund" for c in tool_calls):
        return 0.000 
    
    return score
