# Customer Service Agents (CSA-001)

A professional-grade customer service environment for the Meta PyTorch OpenEnv Hackathon. This environment simulates complex Shopify and Zendesk workflows with logic-gated tools and deterministic graders.

## Task Overview
1. T001: Order Status Inquiry (Easy)
2. T002: Damaged Refund Processing (Medium)
3. T003: Policy Enforcement (Hard)

## Deployment Instructions
1. Build the Docker image: `docker build -t csa-env .`
2. Run the environment: `docker run -p 8000:8000 csa-env`
3. Inference: `python inference.py`

## Compliance
- Pydantic v2 Models: YES
- Dense Rewards: YES (+0.4 per sub-goal)
- Deterministic Graders: YES
- OpenEnv Core Wrapper: YES

[SUBMITTED TO META HACKATHON]
