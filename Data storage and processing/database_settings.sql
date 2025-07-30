CREATE TABLE country
(
 id_country integer ,
 country_name character varying(16) ,
 country_name_en character varying(16) ,
 PRIMARY KEY (id_country)
);

CREATE TABLE resources
(
 id_resource integer ,
 resource_name character varying(32) ,
 resource_name_en character varying(32) ,
 res_type character varying(32) ,
 mark character varying(32) ,
 price integer ,
 menge integer ,
 UNIQUE (id_resource),
 PRIMARY KEY (res_type)
);

CREATE TABLE products
(
 id_product integer ,
 product_name character varying(32) ,
 product_name_en character varying(32) ,
 res_type CHARACTER VARYING(32) ,
 price integer ,
 menge integer ,
PRIMARY KEY (id_product),
FOREIGN KEY (res_type) REFERENCES resources (res_type)
);

CREATE TABLE buy
(
 id_resource integer ,
 id_country integer ,
 buy_quantity integer ,
 FOREIGN KEY (id_country) REFERENCES country (id_country),
 FOREIGN KEY (id_resource) REFERENCES resources (id_resource)
);

CREATE TABLE sell
(
 id_product integer ,
 id_country integer ,
 sell_quantity integer ,
  FOREIGN KEY (id_country) REFERENCES country (id_country),
FOREIGN KEY (id_product) REFERENCES products (id_product)
)
