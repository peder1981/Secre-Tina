# Instruções para Configurar o Repositório Remoto no GitHub

Para completar a configuração do repositório Git para o projeto secre-tina, siga os passos abaixo:

## 1. Criar um novo repositório no GitHub

1. Acesse [GitHub](https://github.com) e faça login em sua conta
2. Clique no botão "+" no canto superior direito e selecione "New repository"
3. Preencha o nome do repositório como "secre-tina"
4. Adicione uma descrição opcional
5. Mantenha o repositório como público ou selecione privado conforme sua preferência
6. **NÃO** inicialize o repositório com README, .gitignore ou licença, pois já temos esses arquivos localmente
7. Clique em "Create repository"

## 2. Vincular o repositório local ao remoto

Após criar o repositório no GitHub, execute os comandos abaixo no terminal dentro da pasta do projeto:

```bash
# Substitua 'seu-usuario' pelo seu nome de usuário do GitHub
git remote add origin https://github.com/seu-usuario/secre-tina.git

# Envie o código para o GitHub
git push -u origin main
```

## 3. Verificar a configuração

Para confirmar que o repositório foi configurado corretamente:

```bash
# Verificar o repositório remoto configurado
git remote -v
```

Você deve ver algo como:
```
origin  https://github.com/seu-usuario/secre-tina.git (fetch)
origin  https://github.com/seu-usuario/secre-tina.git (push)
```

## 4. Fluxo de trabalho futuro

Para futuras alterações, você pode usar o fluxo de trabalho padrão do Git:

```bash
git add .
git commit -m "Descrição das alterações"
git push origin main
```
