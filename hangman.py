import gymnasium as gym
from ale_py import ALEInterface

# Creating env
env = gym.make("ALE/Hangman-v5", render_mode = "human")

# starting env
obs, info = env.reset()
done = False

for _ in range(100):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)

    if terminated or truncated:
        break

env.close()
print("Game Over")
