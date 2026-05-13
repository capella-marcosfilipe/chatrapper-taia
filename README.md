[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/E7ukNRDi)
# Atividade Avaliativa 03 - Construção de Chatbot com LangGraph

Estudantes:

- Elcio José Ferreira da Silva
- Elynne Silva de Lima
- Marcos Filipe Gonçalves Capella
- Maria Gabrielle Silva de Melo

Prof. Iago Richard Rodrigues Silva

Universidade Católica de Pernambuco

### Descrição da Atividade

Nesta atividade, deverá ser desenvolvida uma aplicação capaz de responder perguntas em linguagem natural a partir de uma base de conhecimento definida pela própria equipe. Pontuação: 1,5 pontos na média (não é extra).

A proposta é evoluir a ideia da atividade anterior de busca por similaridade. Antes, o foco estava em encontrar os trechos mais próximos semanticamente de uma consulta. Agora, a proposta é construir um chatbot simples com interface web.

### Requisitos

- uma interface web simples de chatbot;
- um back-end em Python;
- um fluxo de RAG implementado utilizando LangGraph na sua orquestração;
- uma base de conhecimento com conteúdo de um domínio específico;
- uso de uma LLM externa apenas na etapa de geração da resposta.

### Restrições

- Não deve ser utilizada API pronta de chatbot, aqui as equipes irão construir suas próprias APIs para tal.
- A ideia da atividade é construir o chatbot utilizando **RAG**, e não apenas consumir um chatbot já existente.
- É permitido utilizar uma LLM externa para a geração da resposta final, por exemplo:
  - Hugging Face
  - NVIDIA
  - Gemini
  - OpenAI
  - DeepSeek
  - ou outras equivalentes

### Base de Conhecimento

Cada equipe deverá escolher um domínio específico para o chatbot.

Exemplos:
- universidade
- jogos
- futebol
- legislação
- tecnologia
- saúde
- filmes
- atendimento ao cliente
- turismo
- documentação técnica
- etc.

Além disso, a atividade exige uma quantidade maior de conteúdo em relação à atividade anterior. A base não deve ser composta por poucos textos isolados. É esperado que a equipe reúna um volume mais significativo de dados dentro do domínio escolhido. (e.g. dezenas/centenas de páginas web, dezenas/centenas de PDFs, etc.).

A base pode ser montada a partir de diferentes fontes, como:
- arquivos PDF;
- arquivos TXT;
- páginas obtidas por web scraping;
- textos extraídos de sites;
- documentação técnica;
- artigos ou conteúdos públicos relacionados ao domínio.

### Pipeline Sugerido

A solução deve seguir, de forma geral, o seguinte fluxo:

1. Coleta de conteúdo do domínio escolhido;
2. Limpeza e organização dos textos;
3. Quebra do conteúdo em chunks;
4. Geração de embeddings;
5. Armazenamento dos embeddings em um índice vetorial;
6. Recebimento da pergunta do usuário pela interface;
7. Recuperação dos chunks mais relevantes;
8. Montagem do contexto para a LLM utilizando chunks buscados e de mensagens anteriores do chatbot;
9. Geração da resposta final;
10. Exibição da resposta no chat.

### Uso do LangGraph

O fluxo principal da aplicação deve ser organizado com LangGraph.

Espera-se que a equipe utilize a ferramenta para estruturar pelo menos as etapas centrais do processo, como:
- entrada da pergunta;
- recuperação de contexto;
- montagem do prompt;
- chamada da LLM;
- retorno da resposta.

### Interface

A interface não precisa ser sofisticada, mas deve funcionar como um chatbot web.

Espera-se pelo menos:
- campo para digitação da pergunta;
- envio da mensagem;
- exibição da resposta do sistema;
- comunicação com o back-end da aplicação.

A interface pode ser feita com qualquer abordagem simples para web, desde que esteja integrada ao back-end do chatbot.

### Entrega

A atividade deverá ser desenvolvida em equipe.

A entrega será feita por meio do GitHub Classroom no link abaixo:

O repositório deve conter:
- código-fonte completo;
- instruções de execução no `INSTRUCTIONS.md`;
- indicação da base de conhecimento utilizada;
- dependências do projeto;
- qualquer arquivo necessário para executar a aplicação.

Prazo de entrega: 10/042026 às 23h59min.

Atenção: o GitHub Classroom não aceita entregas após o prazo.
