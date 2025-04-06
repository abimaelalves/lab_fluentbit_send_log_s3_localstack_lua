# 🔍 Observabilidade com Fluent Bit, e LocalStack (S3)

Este laboratório demonstra como configurar um pipeline local de logs com **Fluent Bit**, onde os logs são enviados simultaneamente para:

- 📦 **S3 (via LocalStack)** — simulação do bucket AWS

Script lua foi desenvolvido para poder filtrar os campos que desejamos excluir, tanto na raiz e aninhados

---

## ✅ Pré-requisitos

- Docker
- Docker Compose

---

## 🚀 Execução

1. Clone este repositório e acesse o diretório do projeto:

```bash
git clone https://github.com/abimaelalves/lab_fluentbit_send_log_s3_localstack_lua.git
cd lab_fluentbit_send_log_s3_localstack_lua
```

2. Dê permissão de execução aos scripts:

```bash
chmod +x *.sh
```

3. Inicie o ambiente completo:

```bash
./start_lab.sh
```
---

### S3 (LocalStack)

Use o comando abaixo para visualizar os arquivos enviados:

```bash
aws --endpoint-url=http://localhost:4566 s3 ls s3://meubucket/clientes_impactados/ --recursive
```

---

## 🛠️ Ajustes e Customizações

- O `init.sh` define o `fluent-bit.conf` com logs do tipo `dummy`.
- É possível modificar o `INPUT` para ler arquivos reais, usar `tail`, `tcp`, etc.

---

## 🧹 Encerramento

Para remover os containers e volumes:

```bash
docker-compose down -v
```

---