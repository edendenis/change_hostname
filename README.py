#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `hostname` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `hostname` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `hostname` on `Linux Ubuntu`._

# ## Revisão(ões)/Versão(ões)

# | Revisão número | Data da revisão | Descrição da revisão                                    | Autor da revisão                                |
# |:--------------:|:---------------:|:--------------------------------------------------------|:------------------------------------------------|
# | 0              | 18/03/2024      | <ul><li>Revisão inicial/criação do documento.</li></ul> | <ul><li>Eden Denis F. da S. L. Santos</li></ul> |
# 

# ## Descrição [2]
# 
# ### `hostname`
# 
# Um nome de host é um rótulo exclusivo atribuído a um dispositivo conectado a uma rede de computadores. Ele serve como um identificador legível para esse dispositivo, permitindo distingui-lo facilmente de outros dispositivos na rede. Você pode pensar nisso como o nome do seu computador ou de outros dispositivos habilitados para rede.
# 

# ## 1. Como configurar/instalar/usar o `thunar com o sudo` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `thunar com o sudo` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes APT. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo APT e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update -y`
# 
#     2.5 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.6 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update -y`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
# 
#     2.7 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.8 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

# Para alterar o `hostname` no `Linux Ubuntu` através do `Terminal`, você pode seguir os seguintes passos:
# 
# 1. **Abrir o Terminal:** Você pode abrir o Terminal pressionando: `Ctrl + Alt + T`
# 
# 2. **Verificar o `hostname` atual:** Antes de alterar o `hostname`, pode ser útil saber qual é o atual. Você pode verificar isso usando o comando: `hostname`
# 
#     Este comando retornará o `hostname` atual do seu sistema.
# 
# 3. **Permissões de Arquivo:** Alterar arquivos importantes do sistema pode às vezes alterar inadvertidamente suas permissões. Verifique se as permissões dos arquivos estão corretas. Normalmente, ambos deveriam ter permissões de leitura para todos os usuários: `sudo chmod 644 /etc/hostname /etc/hosts`
# 
# 4. **Alterar o `hostname` permanentemente:** Para alterar o `hostname` de forma permanente, você precisa editar o arquivo `/etc/hostname` e o arquivo `/etc/hosts`:
# 
#     4.1 **Edite o arquivo `/etc/hostname`:** `sudo nano /etc/hostname`
# 
#     4.1.1 Apague o `hostname` atual e substitua pelo novo `hostname`. Salve e feche o arquivo pressionando `Ctrl + X`, confirme com `Y` e pressione `Enter`.
# 
#     4.2 **Edite o arquivo `/etc/hosts`:**  `sudo nano /etc/hosts`
# 
#     4.2.1 Encontre a linha que começa com `127.0.1.1` ou qualquer outra linha que contenha o `hostname` antigo. Substitua o `hostname` antigo pelo novo e salve o arquivo da mesma forma que o anterior.
# 
# 5. **Corrigir o Nome de Host em IPv4 e IPv6:** Para IPv4 (`127.0.0.1` e `127.0.1.1`) e IPv6 (`::1`), você deve garantir que o novo hostname esteja listado corretamente. Aqui está um exemplo se você quiser mudar para um novo hostname, digamos `edenedfsls`:
# 
#     ```
#     Copy code
#     127.0.0.1       localhost
#     127.0.1.1       edenedfsls
# 
#     # The following lines are desirable for IPv6 capable hosts
#     ::1     localhost ip6-localhost ip6-loopback edenedfsls
#     fe00::0 ip6-localnet
#     ff00::0 ip6-mcastprefix
#     ff02::1 ip6-allnodes
#     ff02::2 ip6-allrouters
#     ```
# 
# **Neste exemplo:**
# 
# - `localhost` ainda está associado a `127.0.0.1` e `::1` porque você sempre quer manter o acesso local padrão.
# 
# - O novo hostname `edenedfsls` está colocado em `127.0.1.1` para IPv4 e também adicionado ao `::1` para IPv6, junto com os outros nomes padrão de loopback.
# 
# 6. **Verificar Configuração**: 
# 
#     6.1 Após reiniciar, você pode verificar o hostname atual com: `hostname`
# 
#     6.2 E verificar a resolução de nome com: `ping edenedfsls`
# 
# 7. **Reinicie o sistema:** Para que a alteração seja aplicada, você pode reiniciar o sistema com o comando: `sudo systemctl reboot`
# 
#     7.1 Após reiniciar, seu Ubuntu deverá estar com o `hostname` atualizado.
# 
# A alteração do `hostname` no `Ubuntu`, seguindo os passos mencionados, afeta o sistema como um todo, e não apenas um usuário específico. O `hostname` é uma identidade do sistema inteiro, e não é algo que se aplica a contas de usuário individuais. Portanto, quando você altera o `hostname` utilizando os métodos descritos (editando `/etc/hostname` e `/etc/hosts`), essa mudança é refletida em todo o sistema, independentemente de qual usuário esteja logado.
# 
# Isso significa que qualquer usuário que acessar o sistema, seja localmente ou remotamente, verá o novo `hostname` como a identificação do sistema. Esse `hostname` é utilizado em várias situações de rede e de identificação do sistema, como durante sessões SSH, exibição em redes, e em logs de sistema, entre outros.

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `hostname` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o terminal. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Alterar o hostname no ubuntu.*** Disponível em: <https://chat.openai.com/c/c7e97cab-38be-4bf9-ab01-be9063822dbc> (texto adaptado). Acessado em: 18/03/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 18/03/2024 17:10.
# 
