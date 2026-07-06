## GitHub Actions Workflow
(anatomia)

#### -> `on`
Define quando o workflow será executado, como em um push, pull request ou acionamento manual.

#### -> `jobs`
Agrupa as tarefas que serão executadas pelo workflow. Um workflow pode conter um ou mais jobs.

#### -> `runs-on`
Especifica o ambiente (runner) onde o job será executado, como `ubuntu-latest`.

#### -> `steps`
Lista as etapas  que compõe um job. Cada step executa uma ação específiica, como rodar comandos ou utilizar uma Action pronta.

#### Diferença entre `run:` e `uses:`
-> `run:` executa comandos diretamente no terminal do runner (shell).
-> `uses:` reutiliza uma GitHub Action já existente, criada pelo GitHub ou pela comunidade.
