from typing import List, Optional
from uuid import uuid4

from pydantic import BaseModel


class Product(BaseModel):
    uuid: str
    id: Optional[int]
    ena_a: Optional[str]
    id_slika: Optional[str]
    kategorija: Optional[str]
    novo_ime: Optional[str]
    blagovna_znamka: Optional[str]
    drzava_proizvajalca_poreklo: Optional[str]
    hranilna_vrednost_enota: Optional[str]
    energijska_vrednost_kJ: Optional[str]
    enota: Optional[str]
    izbrana_kakovost: Optional[str]
    izbrana_kakovost_slovenija: Optional[str]
    ekoloski_proizvodi: Optional[str]
    zascitena_oznacba_porekla: Optional[str]
    zascitena_geografska_oznacba: Optional[str]
    zajamcena_tradicionalna_posebnost: Optional[str]
    oznacba_visje_kakovosti: Optional[str]
    integrirana_pridelava: Optional[str]
    vrsta_porekla: Optional[str]
    tip_znamke: Optional[str]
    slika_ok: Optional[str]
    prices: Optional[List[dict]] = None


class ProductPrice(BaseModel):
    uuid: str
    product: Optional[str]
    id: Optional[int]
    ena_a: Optional[str]
    trgovina: Optional[str]
    redna_cena_na_kos: Optional[str]
    redna_cena_na_kilogram_liter: Optional[str]
    akcijska_cena_na_kos: Optional[str]
    akcijska_cena_na_kilogram_liter: Optional[str]
    date: Optional[str]
    kategorija: Optional[str]
    teza_g: Optional[str]
    kolicina_mL: Optional[str]
    vrsta_popusta: Optional[str]
    drzava: Optional[str]
    enota: Optional[str]
    drzava_dolgo_ime: Optional[str]
    alternativna_kategorija: Optional[str]
    cena_kosarica: Optional[str]
    cena_kosarica_akcija: Optional[str]
    datestamp: Optional[str]


class ProductFavorites(BaseModel):
    uuid: Optional[str]
    user_uuid: str
    product_uuids: List[str] = []
    products: List[Product] = []
