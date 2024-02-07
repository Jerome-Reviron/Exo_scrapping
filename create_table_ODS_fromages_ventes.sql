-- Table ODS_fromages_table
CREATE TABLE ODS_fromages_table (
    fromage_names VARCHAR2(50) NOT NULL,
    fromage_familles VARCHAR2(20)NULL,
    pates VARCHAR2(80)NULL,
    url_info_fromages VARCHAR2(100)NULL,
    descriptions VARCHAR2(1500)NULL,
    note_moyenne NUMBER(10,2)NULL,
    nb_avis NUMBER(10,0)NULL,
    prix NUMBER(10,2)NULL,
    images_fromage VARCHAR2(100) NULL
);

-- Table ODS_cheeses_sales
CREATE TABLE ODS_cheeses_sales (
    transaction VARCHAR2(50) NOT NULL,
    cheeses VARCHAR2(50) NULL,
    dates TIMESTAMP(6) NULL,
    quantities NUMBER(5) NULL
);
