# import gymnasium as gym
# import gymnasium_robotics

# gym.register_envs(gymnasium_robotics)

# env = gym.make('FetchReach-v3', max_episode_steps=100)
# env.reset()
# obs, reward, terminated, truncated, info = env.step(env.action_space.sample())

# env = env.unwrapped

# # The following always has to hold:
# assert reward == env.compute_reward(obs["achieved_goal"], obs["desired_goal"], info)
# assert truncated == env.compute_truncated(obs["achieved_goal"], obs["desired_goal"], info)
# assert terminated == env.compute_terminated(obs["achieved_goal"], obs["desired_goal"], info)

# # However goals can also be substituted:
# substitute_goal = obs["achieved_goal"].copy()
# substitute_reward = env.compute_reward(obs["achieved_goal"], substitute_goal, info)
# substitute_terminated = env.compute_terminated(obs["achieved_goal"], substitute_goal, info)
# substitute_truncated = env.compute_truncated(obs["achieved_goal"], substitute_goal, info)

import gymnasium as gym
import gymnasium_robotics

# 환경 생성
env = gym.make('FetchReach-v3', max_episode_steps=100, render_mode="human")

# 환경 초기화
obs, info = env.reset()

# 렌더링
env.render()

# 환경 실행
done = False
while not done:
    action = env.action_space.sample()  # 무작위 행동
    obs, reward, done, truncated, info = env.step(action)
    env.render()  # 각 스텝마다 렌더링

# 렌더링 종료
env.close()