import gym
import simple_memory_testing_env
import matplotlib.pyplot as plt 

rotate_right = 1
rotate_left = 0
forward = 2

def test_env():    
    env = gym.make(f"SimpleMemoryTestingEnv-v0")
    
    obs = env.reset()
    #env.render()

    obs = env.step(forward)
    obs = env.step(forward)
    obs = env.step(forward)

    plt.imshow(obs[0])
    plt.show()

    obs = env.step(forward)
    obs = env.step(forward)
    obs = env.step(forward)

    plt.imshow(obs[0])
    plt.show()

    obs = env.step(rotate_left)
    
    plt.imshow(obs[0])
    plt.show()

    obs = env.step(forward)
    obs = env.step(forward)

    plt.imshow(obs[0])
    plt.show()
    


if __name__ == "__main__":
    test_env()
    