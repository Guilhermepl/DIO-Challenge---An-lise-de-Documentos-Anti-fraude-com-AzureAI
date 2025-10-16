# 🧠 Análise Automatizada de Documentos com Azure AI

Projeto de desafio da **DIO** para construir um sistema que analisa imagens com Azure AI e identifica dados de cartão de crédito.
---

## 🧾 Sobre o Projeto

Este repositório contém uma implementação em **Python** que:

- Recebe uma imagem.
- Envia a imagem para os serviços Azure Document Intelligence.
- Extrai dados do cartão da imagem.
- Apresenta em tela os dados do cartão.

O objetivo é demonstrar como integrar serviços cognitivos de Azure para analise de imagem.

## 🧩 Tecnologias Utilizadas

- **Python**
- **Azure Document Intelligence**
- **Azure Storage Blob**
- **dotenv** para gerenciamento de variáveis de ambiente

---

## ⚙️ Configuração do Ambiente

1. Clone este repositório:
   ```bash
   git clone https://github.com/<seu-usuario>/<nome-do-repositorio>.git
   cd <nome-do-repositorio>
   ```

2. Crie um ambiente virtual e instale as dependências:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate   # Windows
   pip install -r requirements.txt
   ```

3. Preencha o `.env` na raiz do projeto com os dados do Azure:
   ```env
   ENDPOINT=""
   SUBSCRIPTION_KEY=""
   CONTAINER_NAME=""
   AZURE_STORAGE_CONNECTION_STRING=""
   ```

   > Preencha os valores conforme suas credenciais e configurações no portal do Azure.

---

## 🧠 Uso

Após configurar o ambiente, execute o script principal:

```bash
streamlit run ./src/app.py
```

Irá abrir a interface do streamlit com a opção para o upload do arquivo de imagem.

Ao submeter o arquivo, o sistema irá:

1. Conectar ao Azure AI para fazer o upload do arquivo.
1. Realizar análise imagem para verificar o documento extrair os dados.
3. Apresentar na tela a imagem carregada e os dados do cartão enviado.

---

## 📄 Estrutura do Projeto

```
📦 azure-ai-doc-analyzer
├── app.py
├── requirements.txt
├── .gitignore
├── .env.example
├── src/
│   └── services
│       ├── blob_service.py
│       └── credit_card_service.py
│   └── utils
│       └── config.py
└── README.md
```

---

## 🔒 Segurança

- Todas as credenciais e chaves devem ser armazenadas apenas no arquivo `.env`.
---

## 🧑‍💻 Autor

**Guilherme Pereira Lima**  
💼 Desenvolvedor Full Stack
📍 Belo Horizonte - MG, Brasil  
🔗 [LinkedIn](https://www.linkedin.com/in/guilherme-lima1602/) | [GitHub](https://github.com/guilhermepl)
