# AWS Cloud Fundamentals

Nesta fase foram aplicados conceitos fundamentais de computação em nuvem utilizando a **AWS**. O objetivo principal foi realizar o deploy de uma aplicação conteinerizada em uma máquina virtual na nuvem, tornando o serviço acessível através da internet.

---

### Projeto
**Deploy de container Docker em EC2**

#### Arquitetura Implementada
`Usuário` ➔ `HTTP` ➔ `Security Group (AWS)` ➔ `EC2 (Amazon Linux)` ➔ `Docker Engine` ➔ `Docker Compose (Flask + PostgreSQL)`

---

### Serviços AWS Utilizados

#### Amazon EC2
Serviço utilizado para provisionar a máquina virtual na nuvem.

* **Sistema Operacional:** Amazon Linux
* **Tipo de Instância:** `t3.micro`
* **Acesso Remoto:** SSH via chave RSA (`.pem`)

#### Security Group
Atuando como firewall para a instância EC2, controlando o tráfego de entrada e saída.

| Tipo | Porta | Origem | Objetivo |
| :--- | :---: | :---: | :--- |
| **SSH** | 22 | `Meu IP` | Acesso administrativo |
| **HTTP** | 80 | `0.0.0.0/0` | Publicação da aplicação |

---

### Processo Realizado

1. **Criação da Instância EC2**
   * Provisionamento da VM utilizando Amazon Linux.
   * Conexão via SSH:
     ```bash
     ssh -i key.pem ec2-user@<IP_PUBLICO>
     ```

2. **Configuração do Ambiente**
   * Instalação e inicialização do serviço **Docker Engine**.
   * Adição do usuário `ec2-user` ao grupo `docker`.
   * Instalação do **Docker Compose**.

3. **Deploy da Aplicação**
   * Clonagem/transferência dos arquivos da aplicação (Flask + PostgreSQL).
   * Subida dos containers em modo *detached*:
     ```bash
     docker compose up -d
     ```

---

### Conceitos Aprendidos

#### EC2 & Infraestrutura
* Provisionamento de instâncias e escolha de AMI adequada.
* Gerenciamento de acessos via chaves SSH.
* Controle de ciclo de vida da instância (*Start*, *Stop*, *Terminate*).

#### Segurança
* Configuração e importância dos **Security Groups**.
* Controle refinado de portas e origens de tráfego (redes públicas vs. privadas).

#### Containers na Nuvem
* Execução de containers fora do ambiente local de desenvolvimento.
* Build de imagens em instâncias cloud.
* Exposição de portas de infraestrutura para acesso público via HTTP.
