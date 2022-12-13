create table if not exists "products"
(
    uuid       text default uuid_generate_v4() not null
    constraint "products_pk"
        primary key,
    id integer,
    ena_a text,
    id_slika text,
    kategorija text,
    novo_ime text,
    blagovna_znamka text,
    drzava_proizvajalca_poreklo text,
    hranilna_vrednost_enota text,
    energijska_vrednost_kJ text,
    enota text,
    izbrana_kakovost text,
    izbrana_kakovost_slovenija text,
    ekoloski_proizvodi text,
    zascitena_oznacba_porekla text,
    zascitena_geografska_oznacba text,
    zajamcena_tradicionalna_posebnost text,
    oznacba_visje_kakovosti text,
    integrirana_pridelava text,
    vrsta_porekla text,
    tip_znamke text,
    slika_ok text,
    prices text
);

create table if not exists "product_prices" (
    uuid text default uuid_generate_v4() not null
    constraint "product_prices_pk"
        primary key,
    id integer,
    ena_a text,
    trgovina text,
    redna_cena_na_kos text,
    redna_cena_na_kilogram_liter text,
    akcijska_cena_na_kos text,
    akcijska_cena_na_kilogram_liter text,
    date text,
    kategorija text,
    teza_g text,
    količina (mL) text,
    vrsta_popusta text,
    drzava text,
    enota text,
    drzava_dolgo_ime text,
    alternativna_kategorija text,
    cena_kosarica text,
    cena_kosarica_akcija text,
    datestamp text
);

create table if not exists "products"
(
    uuid                              text default uuid_generate_v4() not null
        constraint products_pk
            primary key,
    ena_a                             text,
    id_slika                          text,
    kategorija                        text,
    novo_ime                          text,
    blagovna_znamka                   text,
    drzava_proizvajalca_poreklo       text,
    hranilna_vrednost_enota           text,
    energijska_vrednost_kj            text,
    enota                             text,
    izbrana_kakovost                  text,
    izbrana_kakovost_slovenija        text,
    ekoloski_proizvodi                text,
    zascitena_oznacba_porekla         text,
    zascitena_geografska_oznacba      text,
    zajamcena_tradicionalna_posebnost text,
    oznacba_visje_kakovosti           text,
    integrirana_pridelava             text,
    vrsta_porekla                     text,
    tip_znamke                        text,
    slika_ok                          text,
    prices                            text,
    id                                integer
);

create table if not exists "product_prices"
(
    uuid                            text default uuid_generate_v4() not null
        constraint product_prices_pk
            primary key,
    id                              integer,
    ena_a                           text,
    trgovina                        text,
    redna_cena_na_kos               text,
    redna_cena_na_kilogram_liter    text,
    akcijska_cena_na_kos            text,
    akcijska_cena_na_kilogram_liter text,
    date                            text,
    kategorija                      text,
    teza_g                          text,
    kolicina_ml                     text,
    vrsta_popusta                   text,
    drzava                          text,
    enota                           text,
    drzava_dolgo_ime                text,
    alternativna_kategorija         text,
    cena_kosarica                   text,
    cena_kosarica_akcija            text,
    datestamp                       text,
    product                         text
);

