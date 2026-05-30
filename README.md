# 🚀 VaultriX — Smart Financial Intelligence System

VaultriX é uma plataforma de inteligência financeira com arquitetura modular e abordagem **API-first**, focada em coleta, análise e previsão de dados financeiros.

---

## 🎯 Objetivo
- Centralizar dados financeiros  
- Categorizar transações  
- Gerar análises de gastos  
- Realizar previsões (forecasting)  
- Apoiar planejamento com metas  

---

## 🏗️ Estrutura

**Backend (Django + DRF)**
- API Layer  
- Service Layer  
- Domain Layer  
- Infrastructure Layer  

**Frontend & Mobile**
- Web: Next.js  
- Mobile: React Native / Flutter  

---

## ⚙️ Stack
- Backend: Python + Django + DRF  
- Database: PostgreSQL  
- Frontend: Next.js  
- Mobile: React Native / Flutter  
- Infra: Docker  

---

## 🗄️ Dados (Resumo)
- `users`  
- `transactions`  
- `categories`  
- `goals`  

---

## 🔄 Fluxo

```mermaid
sequenceDiagram
    participant U as User
    participant C as Web/Mobile
    participant A as API (Controller)
    participant S as Service Layer
    participant R as Repository
    participant D as Database

    U->>C: Create transaction
    C->>A: POST /transactions
    A->>S: Validate + process
    S->>S: Categorize transaction
    S->>R: Persist data (SQL)
    R->>D: INSERT transaction
    D-->>R: OK
    R-->>S: Success
    S-->>A: Response DTO
    A-->>C: 201 Created
```

---

## 🚀 Setup
```bash
docker-compose up --build
```

Docs: http://localhost:8000/docs/
