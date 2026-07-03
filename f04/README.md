# Docker e Conteinerização

Nesta fase foram abordados os fundamentos de Docker e conteinerização, a empacotar aplicações, criar imagens, gerenciar containers e orquestrar ambientes utilizando **Docker Compose**.
Os conceitos foram aplicados em laboratórios práticos e também trabalhamos em um projeto integrando uma aplicação **Python** com banco de dados **PostgreSQL**.

---

## Conteúdos Abordados

#### Fundamentos de Docker, Imagens e Dockerfile:

* Conceitos de imagens e containers
* Diferenças entre virtualização e conteinerização
* Ciclo de vida dos containers
* Construção de imagens
* Camadas (Layers) e cache
* Boas práticas para criação de Dockerfiles
* `.dockerignore`
* Execução de aplicações em containers

#### Gerenciamento de Containers

* Criação, inicialização, parada e remoção de containers
* Publicação de portas
* Variáveis de ambiente
* Inspeção de containers
* Análise de logs

#### Volumes e Redes

* Persistência de dados com volumes
* Bind mounts
* Comunicação entre containers
* DNS interno do Docker
* Redes personalizadas

#### Docker Compose

* Estrutura do `compose.yaml`
* Definição de serviços
* Orquestração de aplicações
* Dependência entre serviços
* Gerenciamento de ambientes com múltiplos containers

#### Projeto Prático

* Containerização de uma aplicação **Flask**
* Integração com **PostgreSQL**
* Persistência de dados utilizando volumes
* Arquitetura multi-container
* Documentação do projeto no GitHub
---

### Comandos Praticados

`docker pull` • `docker run` • `docker ps` • `docker stop` • `docker start` • `docker restart` • `docker rm` • `docker exec` • `docker logs` • `docker inspect` • `docker images` • `docker build` • `docker tag` • `docker network` • `docker volume` • `docker compose up` • `docker compose down` • `docker compose ps` • `docker compose logs`

---

#### Habilidades Desenvolvidas

Ao final da fase, fui capaz de:

* Compreender os conceitos de conteinerização e Docker
* Criar imagens personalizadas utilizando Dockerfile
* Gerenciar o ciclo de vida de containers
* Utilizar volumes para persistência de dados
* Configurar comunicação entre containers através de redes Docker
* Orquestrar aplicações com Docker Compose
* Diagnosticar problemas utilizando logs e inspeção de containers
* Integrar aplicações Python com PostgreSQL em ambiente conteinerizado
* Desenvolver e documentar projetos Docker seguindo boas práticas
* Desafios e projeto prático, aplicando os conceitos aprendidos
