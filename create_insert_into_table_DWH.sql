-- Table dimension D_Dates_de_ventes
INSERT INTO D_DATES_DE_VENTES (EPOCHTIMESTAMP, EPOCHDAY, EPOCHMONTH, EPOCHYEAR)
SELECT DISTINCT DATES,
        EXTRACT(DAY FROM DATES),
        EXTRACT(MONTH FROM DATES),
        EXTRACT(YEAR FROM DATES)
FROM ODS_CHEESES_SALES;

-- Table dimension D_Fromage
INSERT INTO D_FROMAGE (D_FROMAGE_NAMES, FROMAGE_FAMILLES, PATES, URL_INFO_FROMAGES, DESCRIPTIONS, NOTE_MOYENNE, NB_AVIS, PRIX, IMAGES_FROMAGE)
SELECT DISTINCT FROMAGE_NAMES, FROMAGE_FAMILLES, PATES, URL_INFO_FROMAGES, DESCRIPTIONS, NOTE_MOYENNE, NB_AVIS, PRIX, IMAGES_FROMAGE
FROM ODS_FROMAGES_TABLE;

-- Table de fait F_Vente
INSERT INTO F_VENTE (F_TRANSACTION, D_FROMAGE_FK, D_DATES_DE_VENTES_FK, QUANTITES_VENDUES)
SELECT DISTINCT ODS_CHEESES_SALES.TRANSACTION, D_FROMAGE.D_FROMAGE_NAMES, ODS_CHEESES_SALES.DATES, ODS_CHEESES_SALES.QUANTITIES
FROM ODS_CHEESES_SALES
JOIN D_FROMAGE ON ODS_CHEESES_SALES.CHEESES = D_FROMAGE.D_FROMAGE_NAMES;
