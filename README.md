

|<p></p><p>FIAP – Pós Tech<br>Tech Challenger 02</p>|<p></p><p>Versão 1.0</p><p>Data de Criação</p><p>05/07/2024</p><p></p>|
| :-: | :- |


***DESCRIÇÃO DO PROBLEMA***

A empresa Brisanet (https://www.brisanet.com.br), é uma empresa de 

telecomunicações, considerada a maior empresa do ramo na região nordeste do 

país. No passado a empresa Brisanet, passou por um problema de alocação de técnicos para atendimento de OS (Ordem de serviço), nas cidades, por falta de controle, havia vários técnicos atendendo a mesma OS, para instalação e cancelamento de serviços.

**1.0 - Problema**:

Vários técnicos recebiam a mesma OS, tanto para instalação quanto para 

cancelamento de serviços. Fazendo com que o técnico se desloca-se para o 

endereço da OS, sem uma verificação da distância do técnico. Ou se já havia algum outro técnico atendendo aquela OS.

Os técnicos tinham que se comunicar por telefone, para saber se a OS aberta

na central, estava sendo atendida por alguém. E por muitas vezes ocorria falha de comunicação, ou sobrecarregava algum técnico que ficava responsável pela organização das OS’s.


**



***PROPOSTA DE SOLUÇÃO***

Como solução, precisamos verificar os endereços das OS, e dividir entre os 

técnicos, montando uma rota de atendimento para o técnico, de acordo com sua 

localidade.

Cada OS não pode ser atendida por mais de 1 técnico, caso o técnico esteja 

disponível e já tenha atendido as suas OS’s, será disponibilizada um conjunto de  

OS’s que ainda não foram atendidas, para esse técnico, e as rotas dessas OS’s devem ser definidas (algoritmo genético). 

Nesse caso apenas como é um MVP (Minimum Viable Product), não vamos considerar itens como o grau de urgência da OS’s e o tempo médio gasto em cada OS, o que determinaria a quantidade de OS’s atendidas diariamente por técnico.

**2.0 - Definindo as Rotas das OS’s:**

**População inicial**: Após dividir as OS’s para cada técnico, ó proposto usar as OS’s e os técnicos, para criar a **população inicial.**

**Gerações**: É proposto usar 1000 gerações como valor default.

**Mutações**: É proposto usar o valor 0.5 de mutação como default.

**Fitness**: É proposto usar a rota com a melhor solução sub ótima.

**3.0 - Valores fictícios:**

Podemos começar a desenvolver com um valor fictício de 3 técnicos e 15 

OS’s. Totalizando 5 OS’s para cada técnico e cada OS com endereços diferentes.






***ANÁLISES E RESULTADOS OBITIDOS***

A solução, proposta foi realizada com sucesso e o algoritmo genético em sua execução performou bem, dividindo as OSs de forma igualitária para todos os técnicos envolvidos e as roteirizado de acordo com a solução sub ótimas encontradas.

Para que o algoritmo pudesse alcançar o objetivo seguindo as regras propostas, tais medidas foram necessárias. Tais como, não repetir a mesma OSs para mais de um técnico, penalizando assim o algoritmo com um valor de fitness maior toda vez que indivíduos com ordens duplicadas fossem encontradas, isso tornando para o algoritmo o indivíduo menos atrativo e deixando-o de fora das próximas gerações.

Utilizou-se também, o elitismo que garante que o melhor individuo de uma geração sempre esteja na próxima geração, mantendo assim uma base histórica para as evoluções futuras.

Outra medida utilizada, é a seleção por torneio, que prioriza os melhores indivíduos para o método de cruzamento passando os melhores genes a diante.


![Aspose Words 3d1cbb84-441a-4ce1-9219-369e0580c49f 001](https://github.com/user-attachments/assets/6bb183d8-3fcb-4767-85f9-b81c36364658)

![Aspose Words 3d1cbb84-441a-4ce1-9219-369e0580c49f 002](https://github.com/user-attachments/assets/a79f22a6-fab3-4e4a-8a7f-fce049a5f583)

![Aspose Words 3d1cbb84-441a-4ce1-9219-369e0580c49f 003](https://github.com/user-attachments/assets/9ae18222-220c-41d6-a316-218f85580be2)









**4.0 – Pontos de melhoria:**

Nota-se que o algoritmo se estagna em uma solução **sub ótima** em média a cada 35 gerações, isso pode apontar para uma deficiência do algoritmo em encontrar evoluções a longo prazo, necessitando assim da implementação de melhorias futuras nó código.

![Aspose Words 3d1cbb84-441a-4ce1-9219-369e0580c49f 004](https://github.com/user-attachments/assets/7b8bef2c-0bd7-4f12-b5b9-60df357c551c)

![Aspose Words 3d1cbb84-441a-4ce1-9219-369e0580c49f 005](https://github.com/user-attachments/assets/e50d2484-f08b-4d41-b357-6e491ec03dea)

![Aspose Words 3d1cbb84-441a-4ce1-9219-369e0580c49f 006](https://github.com/user-attachments/assets/e15c60e4-f48c-4e8f-a1ba-c168c5827913)

![Aspose Words 3d1cbb84-441a-4ce1-9219-369e0580c49f 007](https://github.com/user-attachments/assets/578b6163-0413-4e2c-9e12-b3e7b300ab7c)


**5.0 – Considerações finais:**

A solução atende a necessidade proporcionando uma rota adequada para cada técnico dentro da solução sub ótima encontrada pelo algoritmo genético. Com isso o problema da empresa Brisanet é solucionado de maneira que os atendimentos sejam priorizados e a satisfação do cliente possa ser garantida.


|**Revisão**|**Data**|**Revisor/Criador**|<p>**Itens alterados**</p><p>(adicionar breve descrição da alteração)</p>|
| :-: | :-: | :-: | :-: |
|001|05/07/24|Fernando Meneses|Criação.|
|002|29/07/24|Jordan Marques|Análise e resultados obitidos.|


