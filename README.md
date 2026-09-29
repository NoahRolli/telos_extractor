# telos

Hybrid ML + rule-based extraction of customs data from trade documents.

A local vision LLM **reads** invoices, packing lists and shipment notices.
A deterministic rule engine **decides**: it turns the extracted data into
customs positions (tariff lookup, splitting, aggregation, rounding, checks).

> Semester project – *Machine Learning and Knowledge-Based Systems*,
> BSc Business AI, FHNW.

## Why hybrid?

| Layer | Approach | Responsibility |
|---|---|---|
| Extraction | Local vision LLM (Ollama) | What is written on the document? |
| Validation | Pydantic schemas | Is the extracted data well-formed? |
| Rules | Knowledge-based rule engine | What does it mean for customs? |
| Checks | Cross-document consistency | Do totals, weights and counts match? |

The model never decides a tariff number. Every customs position can be
traced back to an explicit rule – which keeps results explainable and auditable.

## Pipeline

```
document (photo/PDF)
   → extraction (LLM)     raw fields as JSON
   → validation           schema check
   → rule engine          master-data lookup, split, aggregate, round
   → consistency checks   totals vs. invoice vs. shipment notice
   → customs positions + warnings
```

## Project structure

```
src/telos/
├── extraction/   ML: document → structured data
└── rules/        knowledge base: customs rules
data/
├── private/      real documents – never committed
└── samples/      anonymised / synthetic test documents
tests/
docs/
```

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Requires a local [Ollama](https://ollama.com) installation for extraction.

## Data privacy

All processing runs locally – no document leaves the machine.
Real trade documents and master data are excluded via `.gitignore`;
the repository only contains anonymised or synthetic samples.

## Status

- [x] Project structure
- [ ] Data model
- [ ] Extraction prototype
- [ ] Rule engine
- [ ] Evaluation
