from typing import List

from pony.orm import Database, PrimaryKey, Optional

from app.common.settings import get_settings

db = Database()
settings = get_settings()


class ProductsPony(db.Entity):
    _table_ = 'products'

    uuid = PrimaryKey(str)
    id = Optional(int, nullable=True)
    ena_a = Optional(str, nullable=True)
    id_slika = Optional(str, nullable=True)
    kategorija = Optional(str, nullable=True)
    novo_ime = Optional(str, nullable=True)
    blagovna_znamka = Optional(str, nullable=True)
    drzava_proizvajalca_poreklo = Optional(str, nullable=True)
    hranilna_vrednost_enota = Optional(str, nullable=True)
    energijska_vrednost_kJ = Optional(str, nullable=True)
    enota = Optional(str, nullable=True)
    izbrana_kakovost = Optional(str, nullable=True)
    izbrana_kakovost_slovenija = Optional(str, nullable=True)
    ekoloski_proizvodi = Optional(str, nullable=True)
    zascitena_oznacba_porekla = Optional(str, nullable=True)
    zascitena_geografska_oznacba = Optional(str, nullable=True)
    zajamcena_tradicionalna_posebnost = Optional(str, nullable=True)
    oznacba_visje_kakovosti = Optional(str, nullable=True)
    integrirana_pridelava = Optional(str, nullable=True)
    vrsta_porekla = Optional(str, nullable=True)
    tip_znamke = Optional(str, nullable=True)
    slika_ok = Optional(str, nullable=True)
    prices = Optional(str, nullable=True)


class ProductPricesPony(db.Entity):
    _table_ = 'product_prices'
    product = Optional(str, nullable=True)
    uuid = PrimaryKey(str)
    id = Optional(int, nullable=True)
    ena_a = Optional(str, nullable=True)
    trgovina = Optional(str, nullable=True)
    redna_cena_na_kos = Optional(str, nullable=True)
    redna_cena_na_kilogram_liter = Optional(str, nullable=True)
    akcijska_cena_na_kos = Optional(str, nullable=True)
    akcijska_cena_na_kilogram_liter = Optional(str, nullable=True)
    date = Optional(str, nullable=True)
    kategorija = Optional(str, nullable=True)
    teza_g = Optional(str, nullable=True)
    kolicina_mL = Optional(str, nullable=True)
    vrsta_popusta = Optional(str, nullable=True)
    drzava = Optional(str, nullable=True)
    enota = Optional(str, nullable=True)
    drzava_dolgo_ime = Optional(str, nullable=True)
    alternativna_kategorija = Optional(str, nullable=True)
    cena_kosarica = Optional(str, nullable=True)
    cena_kosarica_akcija = Optional(str, nullable=True)
    datestamp = Optional(str, nullable=True)


class ProductFavoritesPony(db.Entity):
    _table_ = 'product_favorites'
    uuid = PrimaryKey(str)
    user_uuid = Optional(str, nullable=True)
    product_uuids = Optional(str, nullable=True)
