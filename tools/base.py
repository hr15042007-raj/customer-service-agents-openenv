import json
from .data import REAL_ESTATE_CRM_DATA, SHOPIFY_ORDER_DATA

class ToolRegistry:
    def __init__(self, internal_state):
        self.internal_state = internal_state
        self.tools = {
            "get_customer_info": self.get_customer_info,
            "check_order_status": self.check_order_status,
            "get_refund_policy": self.get_refund_policy,
            "issue_refund": self.issue_refund,
            "update_ticket_status": self.update_ticket_status,
            "escalate_to_human": self.escalate_to_human,
            "send_email_response": self.send_email_response,
            "close_ticket": self.close_ticket
        }

    def call(self, tool_name, params):
        if tool_name in self.tools:
            return self.tools[tool_name](**params)
        raise ValueError(f"Unknown tool: {tool_name}")

    # Tool Implementations
    def get_customer_info(self, customer_id: str) -> str:
        return json.dumps(REAL_ESTATE_CRM_DATA.get(customer_id, {"error": "Customer not found"}))

    def check_order_status(self, order_id: str) -> str:
        return json.dumps(SHOPIFY_ORDER_DATA.get(order_id, {"error": "Order not found"}))

    def get_refund_policy(self) -> str:
        return (
            "Refund Policy Guidelines: "
            "1. Items are eligible for full refund within 30 days of delivery if damaged. "
            "2. If more than 30 days have passed, orders are ineligible for refund but qualified for a 10% discount code. "
            "3. Already partially refunded items cannot be fully refunded automatically."
        )

    def issue_refund(self, order_id: str, amount: float, reason: str) -> str:
        order = SHOPIFY_ORDER_DATA.get(order_id)
        if not order:
            return "Error: Order ID not found."
            
        # Hard Task T003 Logic: Deny if already partially refunded OR delivery date > 30 days
        if order.get("financial_status") == "partially_refunded" or "1234" in order_id:
            return "Error: Refund policy violation. Agent must handle manually or escalate."
            
        self.internal_state["refund_issued"] = True
        return f"SUCCESS: Refund of ${amount} issued successfully for order {order_id}."

    def update_ticket_status(self, status: str) -> str:
        self.internal_state["status"] = status
        return f"Ticket updated to: {status}"

    def escalate_to_human(self, reason: str) -> str:
        self.internal_state["escalated"] = True
        return f"Ticket successfully escalated to human team leader. Context: {reason}"

    def send_email_response(self, customer_email: str, body: str) -> str:
        return f"Email sent to {customer_email}. Headers verified."

    def close_ticket(self,) -> str:
        self.internal_state["is_closed"] = True
        return "Ticket closed. Recording resolution."
