# Projeto Docker

Este projeto teve como objetivo aplicar os conceitos fundamentais de conteinerização utilizando **Docker** e **Docker compose**, integrando uma aplicação **Flask** com um banco de dados **PostgreSQL**.
A aplicação registra e mantém um contador de visitas persistente no banco de dados, demonstrando a comunicação entre containers e o uso de volumes para persistência de dados PostgreSQL.

#### Tecnologias usadas:
* `python:3.12`
* `Flask`
* `postgresql:16`
* `docker` & `docker compose` (`up`-`down`)

#### Pré-requisitos:
Antes de iniciar, certifique-se de ter o Python e o Git instalado em sua máquina Linux.
```bash
# Atualizar pacotes e instalar dependências do sistema
sudo apt update && sudo apt install -y python3-pip python3-xlib git
```
```bash
# Clone o Repositório
git clone https://github.com/ciaomah/sysops-devops

# Entrar na pasta do projeto
cd sysops-devops/f02_devops/04_containers/projeto/

# Instalar dependências locais (Opcional, para rodar sem Docker)
pip install -r requirements.txt
```
```bash
# Executar com Docker
# dentro da pasta projeto/
docker compose up -d --build
```


---
### Conceitos Praticados:
**Docker**
* Construção de imagens com Dockerfile
* Criação de containers
* Utilização de camadas
* Uso de `.dockerignore`
* Criação de usuário não previlegiado dentro do container
* Redução do tamanho da imagem removendo dependencias de compilação

**Docker compose**
* Orquestração de múltiplos containers
* Comunicação entre serviços utilizando a rede interna do Docker
* Definição de variáveis de ambiente
* Exposição de portas
* Dependencia entre serviços (`depends_on`)
* Persistência de dados utilizando volumes

**Flask** (com ajuda e pesquisa)
* Criação de uma API simples
* Definição de rotas
* Retorno de respostas em formato JSON

**PostgreSQL**
* Conexão utilizando `psycopg2`
* Criação automatica de tabelas
* Execução de comandos SQL
* Persistência de informações no banco de dados

O projeto proporcionou uma prática intensiva em busca de resolução de problemas. Durante o desenvolvimento, diversos erros foram identificados e corrigidos até seu funcionamento completo, permitindo compreender o funcionamento das ferramentas na prática e fortalecer o processo de aprendizado.

---

#### Como executar

**Construir e iniciar os containers:**
- `docker compose up --build`.

**Acessar a aplicação:**
- `http://localhost:8000`
Via terminal:
- `curl http://localhost:8000`

**retorno de resposta:**
{
    "esquadrão": "Bem vindo!",
 "status": "Online",
  "visitas": 1
  }

  A cada nova requisição, o contador é incrementado e armazenado de forma persistente no PostgreSQL.

---

Este foi um dos projetos mais desafiadores do meu processo de estudos. Embora este projeto utilizasse **Flask**, eu ainda não havia estudado o framework de forma direta. Para superar este desafio, recorri à busca de fontes de consulta para compreender sua estrutura e aplicar, assim permitindo construir o projeto e também praticando e aprendendo sobre um novo conceito.

Ao longo do desenvolvimento, diversos erros (pequenos) surgiram e precisaram ser investigados e corrigidos, exigindo persistência e aprendizado contínuo. Essa experiência reforçou a importancia da pesquisa, da resolução de problemas e da capacidade de aporender novas tecnologias durante o desenvolvimento de um projeto.

