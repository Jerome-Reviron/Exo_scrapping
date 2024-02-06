-- Table dimension D_Fromage
CREATE TABLE D_Fromage (
    D_fromage_names VARCHAR2(50) NOT NULL,
    fromage_familles VARCHAR2(20) NULL,
    pates VARCHAR2(80) NULL,
    url_info_fromages VARCHAR2(100) NULL,
    descriptions VARCHAR2(1500) NULL,
    note_moyenne NUMBER(10) NULL,
    nb_avis NUMBER(10) NULL,
    prix NUMBER(10) NULL,
    images_fromage VARCHAR2(100) NULL,
    PRIMARY KEY (D_fromage_names)
);

-- Table dimension D_Dates_de_ventes
CREATE TABLE D_Dates_de_ventes (
    EpochTimestamp TIMESTAMP(6) NOT NULL,
    EpochDay NUMBER(2) NULL,
    EpochMonth NUMBER(2) NULL,
    EpochYear NUMBER(4) NULL,
    PRIMARY KEY (EpochTimestamp)
);

-- Table de fait F_Vente
CREATE TABLE F_Vente (
    F_Transaction VARCHAR2(50) NOT NULL,
    D_Fromage_FK VARCHAR2(50) NOT NULL,
    D_Dates_de_ventes_FK TIMESTAMP(6) NOT NULL,
    quantites_vendues NUMBER(5) NOT NULL,
    PRIMARY KEY (F_Transaction, D_Fromage_FK, D_Dates_de_ventes_FK),
    FOREIGN KEY (D_Fromage_FK) REFERENCES D_Fromage(D_fromage_names),
    FOREIGN KEY (D_Dates_de_ventes_FK) REFERENCES D_Dates_de_ventes(EpochTimestamp)
);