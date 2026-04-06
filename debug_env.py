import sys
import os

# Add current directory to path
sys.path.append(os.getcwd())

try:
    from customer_service_env import CustomerServiceEnv, Action
    from tasks.scenarios import SCENARIOS
    
    print("--- Diagnostic Start ---")
    env = CustomerServiceEnv()
    
    for task_id in ["T001", "T002", "T003"]:
        print(f"\nTesting Task: {task_id}")
        obs = env.reset(task_id)
        print(f"Initial Obs: {obs.observation[:50]}...")
        
        # Test a valid tool call
        action = Action(tool="get_refund_policy", parameters={}, thought="Checking policy")
        obs, reward, done, info = env.step(action)
        print(f"Step Result: Reward={reward.value}, Details={reward.details}")
        
        # Test grader
        score = env.grader(task_id)
        print(f"Initial Grader Result: {score}")

    print("\n--- Diagnostic Success ---")

except Exception as e:
    print(f"\n--- Diagnostic FAILED ---")
    print(f"Error: {str(e)}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
