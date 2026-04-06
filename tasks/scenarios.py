# High-Detail Scenarios for Customer Service Agents
SCENARIOS = {
    "T001": {
        "id": "T001",
        "name": "Easy: Order Delivery Inquiry",
        "query": "Hi, I'm Alice (CUST-101). When will my order #SHP-9921 arrive?",
        "customer_id": "CUST-101",
        "order_id": "SHP-9921",
        "difficulty": "easy",
        "success_criteria": "Agent correctly identifies the estimated delivery date (2024-04-10) and communicates it to the customer via email/message."
    },
    "T002": {
        "id": "T002",
        "name": "Medium: Damaged Item Refund",
        "query": "I am Bob (CUST-305). My order #SHP-5520 was delivered today but it's broken. I need a refund.",
        "customer_id": "CUST-305",
        "order_id": "SHP-5520",
        "difficulty": "medium",
        "success_criteria": "Agent checks customer info, verifies delivery date, reads refund policy, and issues a full refund."
    },
    "T003": {
        "id": "T003",
        "name": "Hard: Out-of-Window Refund with Partial Credit",
        "query": "Charlie Brown here (#CUST-999). I bought a coffee maker (order #SHP-1234) and it failed. I want a full refund. I know I already got a $25 credit, but I want the rest back.",
        "customer_id": "CUST-999",
        "order_id": "SHP-1234",
        "difficulty": "hard",
        "success_criteria": "Agent MUST refuse the refund based on two policies: 1) Delivered >30 days ago and 2) Already partially refunded. Agent should offer 10% discount or escalate."
    }
}
