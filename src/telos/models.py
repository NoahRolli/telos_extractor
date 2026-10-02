"""Datenmodell von telos.

Ebene A: Was auf dem Dokument steht (Output der Extraktion / des LLM).
Ebene B: Was die Verzollung braucht (Output der Regelschicht).
"""
from datetime import date
from decimal import Decimal

from pydantic import BaseModel, Field


# ---------- Ebene A: Was auf dem Dokument steht ----------

class Sorte(BaseModel):
    """Eine Unterposition eines Artikels, z.B. 'Erdbeere'."""
    bezeichnung: str
    stueck: int = Field(ge=0)
    wert: Decimal = Field(ge=0)


class Artikel(BaseModel):
    """Eine Artikelzeile auf der Rechnung."""
    artikelnummer: str | None = None
    ge_ean: str | None = None
    bezeichnung: str
    karton: int = Field(ge=0)
    sorten: list[Sorte] = []


class Rechnung(BaseModel):
    """Die extrahierten Kopf- und Positionsdaten einer Rechnung."""
    rechnungsnummer: str
    rechnungsdatum: date
    waehrung: str = "EUR"
    warenwert_total: Decimal = Field(ge=0)
    netto_total: Decimal = Field(ge=0)
    brutto_total: Decimal = Field(ge=0)
    artikel: list[Artikel]


# ---------- Ebene B: Was die Verzollung braucht ----------

class Zollposition(BaseModel):
    """Eine fertige Position für die Zollanmeldung."""
    artikelnummer: str
    tarifnummer: str
    karton: int
    netto: Decimal
    brutto: Decimal
    wert: Decimal
