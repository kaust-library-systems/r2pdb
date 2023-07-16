# Repository to Preservica Database

Creating a simple [SQLite3](https://www.sqlite.org/index.html) database to store the ingested items.

Below is a simple [ER diagram](https://mermaid.js.org/syntax/entityRelationshipDiagram.html) of how the tables are related.

```mermaid
--- 
title: Ingestion and Verification Diagram
---
erDiagram
    items ||--|{ ingested : ingest
    items {
        int id
        string item
    }
    ingested {
        int id
        int id_item
        string dt_ingest
    }
    items ||--|{ verified: verify
    verified {
        int id
        int id_item
        string dt_verify
    }
```

## Creating the database

To create the database from the SQL files, execute the `createdb.py` script

```
PS C:\Users\garcm0b\Work\r2pdb> python .\createdb.py
Creating table from 'items.sql'... done
Creating table from 'verify.sql'... done
Creating table from 'ingest.sql'... done
PS C:\Users\garcm0b\Work\r2pdb> 
```

The result is the `r2p.db` file:

```
PS C:\Users\garcm0b\Work\r2pdb> ls r2p.db

    Directory: C:\Users\garcm0b\Work\r2pdb

Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a---           6/21/2023  9:35 AM          16384 r2p.db

PS C:\Users\garcm0b\Work\r2pdb> 
```

## Populating the Database

Populating the database with some sample data and a date

```
PS C:\Users\garcm0b\Work\r2pdb> python .\populate.py .\sample_items_2.txt "2023-07-13"
```

The `sample_items*.txt` is a simple file with one item from the repository per line

```
PS C:\Users\garcm0b\Work\r2pdb> cat .\sample_items.txt  
10754_136193
10754_136194
10754_136195
10754_136196
```

## Verify Items

Whenever an item is ingested, the flag `verified` is set to _false_.

```mermaid
flowchart LR
    A[Ingest] -->B[Add Item to Database]
    B --> C[set verified to false]
```

The verification step sets the flag to _true_. 

```mermaid
flowchart LR
	A[Verify] -->|Query Ingested| B{Already Verified?}
	B -->|Yes| C[Skip]
	B -->|No| D[Verify item] -->E{Successful?}
    E -->|Yes| F[Set verified to True]
    E -->|No| G[Ingest Again]
```

If the item has to be ingested again, the flag `verified` is set to _false_ again until the verification is successful and set the flag to _true_.