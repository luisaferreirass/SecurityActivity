# 🔐 Security Activity

## 📝 Sobre o projeto

API REST de autenticação e segurança desenvolvida com **Flask**, implementando práticas modernas de segurança como criptografia de senhas com **bcrypt** e autenticação via **JWT (JSON Web Tokens)**. O projeto demonstra conceitos essenciais de segurança em aplicações web.

Ideal para aprendizado de:
- Autenticação e autorização
- Criptografia de senhas com bcrypt
- JSON Web Tokens (JWT)
- Boas práticas de segurança em APIs
- Variáveis de ambiente com python-dotenv
- Framework Flask
- Testes automatizados

## 🚀 Tecnologias utilizadas

- **Python 3.x**
- **Flask 3.0.3** - Framework web
- **bcrypt 4.2.0** - Criptografia de senhas
- **PyJWT 2.9.0** - Autenticação via tokens JWT
- **python-dotenv 1.0.1** - Gerenciamento de variáveis de ambiente
- **Pytest 8.3.3** - Framework de testes
- **Jinja2 3.1.4** - Template engine

## ⚙️ Como executar

### Pré-requisitos

- Python 3.x instalado
- pip (gerenciador de pacotes Python)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/luisaferreirass/SecurityActivity.git
cd SecurityActivity
```

2. Crie um ambiente virtual (recomendado):
```bash
python -m venv venv
```

3. Ative o ambiente virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Configure as variáveis de ambiente:
```bash
# Crie um arquivo .env na raiz do projeto
SECRET_KEY=sua_chave_secreta_aqui
JWT_SECRET_KEY=sua_chave_jwt_aqui
```

### Executando a aplicação
```bash
python app.py
```

A API estará disponível em: `http://localhost:5000`

### Executando os testes
```bash
pytest
```

ou para ver mais detalhes:
```bash
pytest -v
```

## 🎯 Funcionalidades

- 🔐 **Registro de usuários** com senha criptografada
- 🔑 **Login** com geração de token JWT
- ✅ **Autenticação** via token JWT
- 🛡️ **Rotas protegidas** que requerem autenticação
- 🔒 **Criptografia de senhas** com bcrypt
- 🧪 **Testes automatizados**

## 🛠️ Modelo de dados

### User (Usuário)

| Campo | Tipo | Descrição |
|-------|------|-----------|
| id | Integer | Identificador único |
| username | String | Nome de usuário (único) |
| password | String | Senha criptografada com bcrypt |
| email | String | E-mail do usuário |

## 📸 Endpoints da API

### Autenticação

| Método | Endpoint | Descrição | Autenticação |
|--------|----------|-----------|--------------|
| POST | `/register` | Registra um novo usuário | Não |
| POST | `/login` | Autentica usuário e retorna JWT | Não |
| GET | `/profile` | Retorna dados do usuário logado | Sim (JWT) |

## 💡 Exemplos de uso

### Registrar um novo usuário
```bash
POST /register
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "senha123"
}
```

**Resposta:**
```json
{
  "message": "Usuário criado com sucesso",
  "user_id": 1
}
```

### Fazer login
```bash
POST /login
Content-Type: application/json

{
  "username": "johndoe",
  "password": "senha123"
}
```

**Resposta:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "message": "Login realizado com sucesso"
}
```

### Acessar rota protegida
```bash
GET /profile
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
```

**Resposta:**
```json
{
  "id": 1,
  "username": "johndoe",
  "email": "john@example.com"
}
```

## 🔒 Recursos de Segurança

- **Bcrypt**: Hash de senhas com salt automático
- **JWT**: Tokens stateless para autenticação
- **Variáveis de ambiente**: Proteção de credenciais sensíveis
- **Validação de dados**: Verificação de entrada do usuário
- **Rotas protegidas**: Middleware de autenticação

## ⚠️ Boas Práticas Implementadas

- Senhas nunca armazenadas em texto puro
- Uso de variáveis de ambiente para informações sensíveis
- Tokens JWT com expiração
- Validação de entrada de dados
- Separação de responsabilidades

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT.

## 👩‍💻 Autora

Desenvolvido por [Luisa Ferreira](https://github.com/luisaferreirass)
