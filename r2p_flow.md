# R2P Diagrams

```mermaid
flowchart LR
    A(Repo Item) -->|Check| B[Ingest Item]
    B --> C{Already Ingested?}
    C -->|New| D[Insert item]
    C -->|Failed| E[Add new ingested record]
```
