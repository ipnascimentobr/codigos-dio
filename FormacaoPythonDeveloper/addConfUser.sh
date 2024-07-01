#!/bin/bash

# Variáveis de senha criptografada
SENHA_GRUPO_ADM=$(openssl passwd -crypt senha_grupo_adm)
SENHA_GRUPO_VEN=$(openssl passwd -crypt senha_grupo_ven)
SENHA_GRUPO_SEC=$(openssl passwd -crypt senha_grupo_sec)

# Criar diretórios
sudo mkdir -p /diretorio/publico /diretorio/adm /diretorio/ven /diretorio/sec

# Criar grupos
sudo groupadd GRP_ADM
sudo groupadd GRP_VEN
sudo groupadd GRP_SEC

# Criar usuários e associá-los aos grupos
sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_ADM" -G GRP_ADM carlos
sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_ADM" -G GRP_ADM maria
sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_ADM" -G GRP_ADM joao

sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_VEN" -G GRP_VEN debora
sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_VEN" -G GRP_VEN sebastiana
sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_VEN" -G GRP_VEN roberto

sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_SEC" -G GRP_SEC josefina
sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_SEC" -G GRP_SEC amanda
sudo useradd -m -s /bin/bash -p "$SENHA_GRUPO_SEC" -G GRP_SEC rogerio

# Definir proprietário dos diretórios como root
sudo chown -R root:root /diretorio/publico /diretorio/adm /diretorio/ven /diretorio/sec

# Definir permissões
# Diretório /diretorio/publico com permissões para todos
sudo chmod -R 777 /diretorio/publico

# Diretórios específicos com permissões para seus respectivos grupos
sudo chmod -R 770 /diretorio/adm
sudo chmod -R 770 /diretorio/ven
sudo chmod -R 770 /diretorio/sec

# Restringir permissões de outros diretórios
sudo chmod -R o-rwx /diretorio/adm /diretorio/ven /diretorio/sec

# Exemplo de limpeza (excluir usuários, grupos e diretórios)
# sudo userdel -r carlos maria joao debora sebastiana roberto josefina amanda rogerio
# sudo groupdel GRP_ADM GRP_VEN GRP_SEC
# sudo rm -rf /diretorio/publico /diretorio/adm /diretorio/ven /diretorio/sec

echo "Provisionamento concluído."
