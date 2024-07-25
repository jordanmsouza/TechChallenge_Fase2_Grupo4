import numpy as np
import random
import pygame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

# Inicializando Pygame
pygame.init()
LARGURA, ALTURA = 1200, 600
CONFIGPYGAME = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Algoritmo Genético - Roteirização de Técnicos")

# Constantes de cores paygame
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERMELHO = '#FF0000'
VERDE = '#00FF00'
AZUL = '#0000FF'
CORES = [VERMELHO, VERDE, AZUL, PRETO]

# Distância euclidiana entre dois pontos
def distancia_euclidiana(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Função de avaliação (fitness)
def fitness(solucao, matriz_distancia, penalidade=10000):
    total_distancia = 0
    todos_servicos = []
    for rota_tecnico in solucao:
        rota_distancia = 0
        for i in range(len(rota_tecnico) - 1):
            rota_distancia += matriz_distancia[rota_tecnico[i]][rota_tecnico[i + 1]]
        total_distancia += rota_distancia
        todos_servicos.extend(rota_tecnico)
    
    # Penalidade por ordens duplicadas
    duplicados = len(todos_servicos) - len(set(todos_servicos))
    return total_distancia + penalidade * duplicados

# Geração inicial de soluções
def gerar_populacao_inicial(num_tecnicos, num_servicos, tamanho_populacao):
    if num_servicos % num_tecnicos != 0:
        raise ValueError("O número de ordens de serviço deve ser divisível pelo número de técnicos.")
    
    populacao = []
    todos_servicos = list(range(num_servicos))
    servicos_por_tecnico = num_servicos // num_tecnicos

    for _ in range(tamanho_populacao):
        random.shuffle(todos_servicos)
        solucao = []
        for i in range(num_tecnicos):
            rota_tecnico = todos_servicos[i * servicos_por_tecnico:(i + 1) * servicos_por_tecnico]
            solucao.append(rota_tecnico)
        populacao.append(solucao)
    return populacao

# Seleção por torneio
def selecao_por_torneio(populacao, fitnesses, k=3):
    selecao = random.sample(list(zip(populacao, fitnesses)), k)
    selecao = sorted(selecao, key=lambda x: x[1])
    return selecao[0][0]

# Operador de cruzamento
def cruzamento(pai1, pai2, num_servicos):
    filho1, filho2 = [], []
    for i in range(len(pai1)):
        split = len(pai1[i]) // 2
        filho1_rota_tecnico = pai1[i][:split] + [s for s in pai2[i] if s not in pai1[i][:split]]
        filho2_rota_tecnico = pai2[i][:split] + [s for s in pai1[i] if s not in pai2[i][:split]]
        filho1.append(filho1_rota_tecnico)
        filho2.append(filho2_rota_tecnico)
    
    # Corrige duplicações e faltas
    for filho in [filho1, filho2]:
        todos_servicos = set(range(num_servicos))
        servicos_selecionados = [s for tecnico in filho for s in tecnico]
        servicos_duplicados = [s for s in servicos_selecionados if servicos_selecionados.count(s) > 1]
        servicos_restantes = list(todos_servicos - set(servicos_selecionados))
        
        while servicos_duplicados and servicos_restantes:
            dupe = servicos_duplicados.pop(0)
            for tecnico in filho:
                if dupe in tecnico:
                    tecnico[tecnico.index(dupe)] = servicos_restantes.pop(0)
                    break

    return filho1, filho2

# Operador de mutação
def mutacao(solucao, range_mutacao=0.05):  # Aumentar taxa de mutação
    for rota_tecnico in solucao:
        if random.random() < range_mutacao:
            idx1, idx2 = random.sample(range(len(rota_tecnico)), 2)
            rota_tecnico[idx1], rota_tecnico[idx2] = rota_tecnico[idx2], rota_tecnico[idx1]

# Função para desenhar as rotas e o gráfico de fitness
def visualizacao(solucao, pontos, historico_fitness, geracao, fig, eixo1, eixo2):
    eixo1.clear()
    eixo2.clear()

    # Desenha as rotas
    eixo1.set_title('Rotas dos Técnicos')
    eixo1.set_xlim(0, LARGURA / 2)
    eixo1.set_ylim(0, ALTURA)
    eixo1.set_xticks([])
    eixo1.set_yticks([])
    for idx, rota in enumerate(solucao):
        color = CORES[idx % len(CORES)]
        for i in range(len(rota) - 1):
            eixo1.plot([pontos[rota[i]][0], pontos[rota[i + 1]][0]], [pontos[rota[i]][1], pontos[rota[i + 1]][1]], color=color)
        for point in rota:
            eixo1.plot(pontos[point][0], pontos[point][1], 'o', color=color)
    
    # Desenha o gráfico de fitness
    eixo2.set_title(f'Fitness ao longo das Gerações - Geração {geracao}')
    eixo2.plot(historico_fitness, color='red')
    eixo2.set_xlabel('Gerações')
    eixo2.set_ylabel('Fitness')

    # Renderiza a figura no canvas do Pygame
    render_pygame = FigureCanvas(fig)
    render_pygame.draw()
    dado_inicial = render_pygame.buffer_rgba().tobytes()
    tamanho = render_pygame.get_width_height()

    # Convertendo o gráfico em uma superfície do Pygame
    surf = pygame.image.fromstring(dado_inicial, tamanho, "RGBA")
    CONFIGPYGAME.blit(surf, (0, 0))

    pygame.display.update()

# Algoritmo genético principal
def algoritimo_genetico(matriz_distancia, num_tecnicos, num_servicos, pontos, tamanho_populacao=100, geracoes=1000, range_mutacao=0.25, eletismo=True, limite_sem_melhoria=100):
    populacao = gerar_populacao_inicial(num_tecnicos, num_servicos, tamanho_populacao)
    historico_fitness = []
    melhor_solucao = None
    melhor_fitness = float('inf')
    geracao_sem_melhoria = 0  # Contador de gerações sem melhoria
    
    fig, (eixo1, eixo2) = plt.subplots(1, 2, figsize=(12, 6))

    for gen in range(geracoes):
        fitnesses = [fitness(solucao, matriz_distancia) for solucao in populacao]
        
        if eletismo:
            melhor_gen_idx = np.argmin(fitnesses)
            melhor_gen_solucao = populacao[melhor_gen_idx]

        nova_populacao = []
        for _ in range(tamanho_populacao // 2):
            pai1 = selecao_por_torneio(populacao, fitnesses)
            pai2 = selecao_por_torneio(populacao, fitnesses)
            filho1, filho2 = cruzamento(pai1, pai2, num_servicos)
            mutacao(filho1, range_mutacao)
            mutacao(filho2, range_mutacao)
            nova_populacao.extend([filho1, filho2])
        
        if eletismo:
            nova_populacao[random.randint(0, tamanho_populacao - 1)] = melhor_gen_solucao

        populacao = nova_populacao

        melhor_fitness_atual = min(fitnesses)
        if melhor_fitness_atual < melhor_fitness:
            melhor_fitness = melhor_fitness_atual
            melhor_solucao = populacao[fitnesses.index(melhor_fitness)]
            geracao_sem_melhoria = 0  # Reseta contador de gerações sem melhoria
        else:
            geracao_sem_melhoria += 1  # Incrementa contador de gerações sem melhoria

        historico_fitness.append(melhor_fitness)
        print(f"Geração {gen}: Melhor Fitness = {melhor_fitness}")

        # Atualiza visualização
        visualizacao(melhor_solucao, pontos, historico_fitness, gen, fig, eixo1, eixo2)
        
        # Condição de parada
        if geracao_sem_melhoria >= limite_sem_melhoria:
            print(f"Parando a execução após {limite_sem_melhoria} gerações sem melhoria.")
            break

    return melhor_solucao, melhor_fitness, historico_fitness

# Chamada inicial
num_tecnicos = 3
num_servicos = 15
pontos = np.random.rand(num_servicos, 2) * [LARGURA / 2, ALTURA]  # Gerando pontos aleatórios
matriz_distancia = np.array([[distancia_euclidiana(p1, p2) for p2 in pontos] for p1 in pontos])

melhor_solucao, melhor_fitness, historico_fitness = algoritimo_genetico(matriz_distancia, num_tecnicos, num_servicos, pontos)

print("Melhor Solução:", melhor_solucao)
print("Melhor Fitness:", melhor_fitness)

# Mantendo a janela aberta
execucao = True
while execucao:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            execucao = False
pygame.quit()
