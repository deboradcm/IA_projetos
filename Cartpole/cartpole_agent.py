import gym

# Inicializa o ambiente Cartpole
env = gym.make('CartPole-v1')

num_episodes = 10  # Número de episódios de treinamento

for episode in range(num_episodes):
    observation = env.reset()  # Reinicia o ambiente para um novo episódio
    total_reward = 0  # Inicializa a recompensa total para este episódio
    
    done = False  # Indica se o episódio foi concluído
    
    while not done:
        env.render()  # Renderiza o ambiente (opcional, para visualização)
        
        action = env.action_space.sample()  # Escolhe uma ação aleatória
        step_result = env.step(action)  # Executa a ação no ambiente
        observation = step_result[0]  # A próxima observação
        reward = step_result[1]  # A recompensa
        done = step_result[2]  # Indicação de conclusão do episódio
        info = step_result[3]  # Informações adicionais
        
        total_reward += reward  # Adiciona a recompensa ao total
        
    print("Episódio {} concluído com recompensa total de {}".format(episode+1, total_reward))
