# Redes

Nesta fase do treinamento foram estudados os conceitos fundamentais de redes de computadores, comunicação entre dispositivos, protocolos de rede, diagnóstico de conectividade e princípios de reconhecimento de redes de forma ética e segura.

---

## Conteúdos Abordados:

#### Redes de Computadores e Endereçamento de Rede
* Conceitos de LAN, WAN e Intranet.
* Diferença entre Cliente e Servidor.
* Funcionamento da comunicação em redes.
* Endereços IP e MAC.
* IPv4 e IPv6.
* IP público e IP privado.
* NAT e comunicação entre redes.

#### Modelo TCP/IP
* Camadas de Aplicação, Transporte, Internet e Acesso à Rede.
* Fluxo dos dados através das camadas.
* Papel dos protocolos em cada camada.

#### Portas e Protocolos
* Conceito de portas de comunicação.
* Portas mais utilizadas:
  * 22 (SSH)
  * 53 (DNS)
  * 80 (HTTP)
  * 443 (HTTPS)
* Diferença entre TCP e UDP.

#### DNS

* Resolução de nomes para IP.
* Tipos de registros:
  * A
  * AAAA
  * CNAME
  * MX
  * TXT
* Utilização de `dig`.

### HTTP e HTTPS

* Estrutura de Requests e Responses.
* Headers HTTP.
* Métodos HTTP:
  * GET
  * POST
  * PUT
  * PATCH
  * DELETE

* Status Codes:
  * 2xx
  * 3xx
  * 4xx
  * 5xx
* TLS, certificados digitais e criptografia HTTPS.

#### Ferramentas de Diagnóstico

* `ping` • `traceroute` / `tracert` • `curl` • `dig` • `nc` (netcat) • `ss` / `netstat` • `tcpdump`

#### Análise de Tráfego
* Conceitos de captura de pacotes.
* Utilização do Wireshark.
* Filtros de análise.
* Follow TCP Stream.
* Uso do `tshark` para análise via terminal.

#### Reconhecimento com Nmap
* Descoberta de hosts.
* Identificação de portas abertas.
* Detecção de serviços e versões.
* Banner Grabbing.
* Scripts NSE.
* Reconhecimento de superfícies de ataque.
* Técnicas de enumeração de serviços.
---

## Habilidades Desenvolvidas
Ao final desta fase, fui capaz de:

* Entender a comunicação entre dispositivos em redes.
* Leitura e interpretação de protocolos de rede.
* Identificar portas e serviços conhecidos.
* Consultar e analisar de registros DNS.
* Investigar headers HTTP utilizando `curl`.
* Utilizar ferramentas de diagnóstico para análise de conectividade.
* Capturar e analisar tráfego de rede com `Wireshark`, `Tshark` e `Tcpdump`.
* Extrair informações relevantes de arquivos PCAP.
* Investigar tráfego HTTP em texto puro.
* Analisar consultas DNS utilizadas para exfiltração de dados.
* Realizar reconhecimento de redes utilizando Nmap.
* Identificar hosts, portas abertas, serviços e possíveis superfícies de ataque.
