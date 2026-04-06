# Deep Detail Mock Data for Shopify/Zendesk simulation
REAL_ESTATE_CRM_DATA = {
    "CUST-101": {
        "id": "CUST-101",
        "name": "Alice Smith",
        "email": "alice.smith@example.com",
        "membership": "Gold",
        "total_spent": 1250.50,
        "customer_since": "2022-01-15",
        "tags": ["high_value", "verified"]
    },
    "CUST-305": {
        "id": "CUST-305",
        "name": "Bob Jones",
        "email": "bob.jones@example.com",
        "membership": "Silver",
        "total_spent": 450.00,
        "customer_since": "2023-05-10",
        "tags": ["subscription_active"]
    },
    "CUST-999": {
        "id": "CUST-999",
        "name": "Charlie Brown",
        "email": "charlie.brown@example.com",
        "membership": "Standard",
        "total_spent": 25.00,
        "customer_since": "2024-03-01",
        "tags": ["new_user"]
    }
}

SHOPIFY_ORDER_DATA = {
    "SHP-9921": {
        "order_id": "SHP-9921",
        "status": "in_transit",
        "financial_status": "paid",
        "fulfillment_status": "fulfilled",
        "shipping_address": {"city": "New York", "zip": "10001"},
        "tracking_events": [
            {"date": "2024-04-01", "status": "order_placed"},
            {"date": "2024-04-03", "status": "shipped", "carrier": "FedEx"}
        ],
        "estimated_delivery": "2024-04-10",
        "total_price": 150.00
    },
    "SHP-5520": {
        "order_id": "SHP-5520",
        "status": "delivered",
        "financial_status": "paid",
        "fulfillment_status": "fulfilled",
        "delivered_at": "2024-04-04",
        "line_items": [{"id": 1, "title": "Headphones", "price": 200.00}],
        "refund_history": [],
        "total_price": 200.00
    },
    "SHP-1234": {
        "order_id": "SHP-1234",
        "status": "delivered",
        "financial_status": "partially_refunded",
        "fulfillment_status": "fulfilled",
        "delivered_at": "2024-02-25", # Delivered over 30 days ago
        "line_items": [{"id": 2, "title": "Coffee Maker", "price": 100.00}],
        "refund_history": [{"id": "REF-001", "amount": 25.00, "date": "2024-03-05"}],
        "total_price": 100.00
    }
}
