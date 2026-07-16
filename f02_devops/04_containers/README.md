# Docker e Conteinerização
[Diário Docker - Resumo](https://github.com/mayaracsoares/sysops-devops/blob/main/f02_devops/04_containers/diario_docker.md)

### Estrutura:
O módulo está dividido em dois projetos principais com objetivos distintos.

 1- **Projeto Mural App:** Uma aplicação desenvolvida em **Python** integrada a um banco de dados **PostgreSQL**.

* Foi praticado a criação de imagens, configuração de redes internas do Docker, persistência de dados com volume e orquestração multi-container.

* Tecnologias: `Python`, `PostgreSQL`, `Flask`, `Dockerfile`, `Docker compose`.

[Ver instruções de execução - Mural App](https://github.com/ciaomah/sysops-devops/blob/main/f02_devops/04_containers/projeto/README.md)

2- **Projeto Site:** Um ambiente conteinerizado para servir uma página web estática.

* Foi praticado a utilização de imagens prontas, mapeamento de portas e montagem de volumes do tipo `bind mount` para desenvolvimento local.

* Tecnologias: `HTML`, `Nginx`.

[Ver instruções de execução - Site](https://github.com/ciaomah/sysops-devops/blob/main/f02_devops/04_containers/site/README.md)

#### Pré-requisitos:
Para executar qualquer um dos projetos desse módulo, é necessário ter o ambiente do Docker devidamente instalado na sua máquina.

```bash
# Certifique-se que seu usuário atual pertence ao grupo `docker` para evitar a necessidade de rodar comandos com `sudo`
sudo usermod -aG docker $USER && newgrp docker
```
---
## Resumo do Módulo

Nesta fase foram abordados os fundamentos de Docker e conteinerização, a empacotar aplicações, criar imagens, gerenciar containers e orquestrar ambientes utilizando **Docker Compose**.

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
