# -*- coding: utf-8 -*-
import gymnasium as gym
from gymnasium import spaces
import json
import os
from typing import Any, Dict, List, Optional, Tuple

from tools.base import ToolRegistry
from tasks.graders import grade_trajectory
from tasks.scenarios import SCENARIOS

class CustomerServiceEnv(gym.Env):
    """
    Modular Customer Service Environment for OpenEnv.
    """
    def __init__(self):
        super().__init__()
        self.tool_registry = ToolRegistry()
        self.tool_calls_made = []
        self.internal_state = {"ticket_open": True, "escalated": False}
        self.current_task_id = None
        self.steps = 0
        self.max_steps = 15
        
        # Defining basic action space (tool names)
        self.action_space = spaces.Discrete(len(self.tool_registry.tools))
        self.observation_space = spaces.Dict({
            "observation": spaces.Text(min_length=0, max_length=10000),
            "available_tools": spaces.Sequence(spaces.Text(min_length=1, max_length=100))
        })

    def reset(self, seed: Optional[int] = None, task_id: str = "T001") -> Dict[str, Any]:
        super().reset(seed=seed)
        self.current_task_id = task_id
        self.tool_calls_made = []
        self.steps = 0
        self.internal_state = {"ticket_open": True, "escalated": False}
        
        scenario = SCENARIOS.get(task_id, SCENARIOS["T001"])
        return {
            "observation": scenario["query"],
            "available_tools": list(self.tool_registry.tools.keys())
        }

    def step(self, action_name: str, parameters: Dict[str, Any]) -> Tuple[Dict[str, Any], float, bool, Dict[str, Any]]:
        self.steps += 1
        
        # Executing the tool
        obs_text, reward = self.tool_registry.call_tool(action_name, parameters, self.internal_state)
        
        # Recording the call for the grader
        self.tool_calls_made.append({"tool": action_name, "parameters": parameters, "output": obs_text})
        
        # Dense reward logic (Phase 4 requirement)
        # We give +0.4 for first-time partial progress on core tools
        if action_name in ["check_order_status", "get_customer_info", "get_refund_policy"]:
            if len([c for c in self.tool_calls_made if c["tool"] == action_name]) == 1:
                reward += 0.4

        done = (not self.internal_state["ticket_open"]) or (self.steps >= self.max_steps)
        info = {"task_id": self.current_task_id, "steps": self.steps}
        
        return {
            "observation": obs_text,
            "available_tools": list(self.tool_registry.tools.keys())
        }, float(reward), done, info

    def grader(self, task_id: str) -> float:
        """Deterministic grader (Phase 4 requirement)"""
        return grade_trajectory(task_id, self.tool_calls_made, self.internal_state)
