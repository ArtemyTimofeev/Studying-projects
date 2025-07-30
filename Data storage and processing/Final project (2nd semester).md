# База данных SQL «Перерабатывающий завод»
### 1. Описание предметной области
Есть универсальный перерабатывающий завод, который из поставляемого поставщиками сырья производит некоторые конечные продукты. Затем эти продукты закупаются другими клиентами. Причем поставщики и клиенты - представители различных стран. Каждый поставщик поставляет некоторое сырье, с определенной ценой, объемом, маркировкой и типом сырья. Из одного вида сырья можно приготовить различные конечные продукты. Необходимо иметь возможность хранить информацию о поставщиках и клиентах, о сырье (маркировка, цена, фасовка), о конечном продукте (включая тип сырья, из которого он был произведен), о заводских заказах на сырье и заказах на конечные продукты – от клиентов.
### 2. Ожидаемые запросы к предметной области
1. Определите, сколько килограммов **халвы** купила **Молдова**.
2. Какая из стран-поставщиков **пшеничной муки** поставила её **больше всего**?
3. Посчитайте, во сколько раз отличается число заказов на продукцию завода из **Турции** и из **Казахстана**. Ответ округлите до десятых.
4. Какая страна закупила **меньше всего зефира** (при условии, что закупала его в принципе)?
5. Выведите названия двух стран: той, которая продавала **больше** всего самого **дорогого** сырья, и той, которая покупала **меньше** всего самого дешёвого **продукта**.
### 3. Описание базы
В базе ПЕРЕРАБАТЫВАЮЩИЙ ЗАВОД содержатся следующие таблицы:
![](https://geekko.co/storage/v/a1fb469d1e056e326c9a9148a40262b9.JPG)
**COUNTRY** — список стран:

| Название | Тип | Описание |
|---|---|---|
|ID_COUNTRY|ЦЕЛОЕ ЧИСЛО|Идентификатор клиента|
|COUNTRY_NAME|СТРОКА|Название страны|
|COUNTRY_NAME_EN|СТРОКА|Название страны (англ.)|

**RESOURCES** — список сырья:

| Название | Тип | Описание |
|---|---|---|
|ID_RESOURCE|ЦЕЛОЕ ЧИСЛО|Идентификатор ресурса|
|RESOURCE_NAME|СТРОКА|Название ресурса|
|RESOURCE_NAME_EN|СТРОКА|Название ресурса (англ.)|
|TYPE|СТРОКА|Тип сырья|
|MARK|СТРОКА|Маркировка|
|PRICE|ЦЕЛОЕ ЧИСЛО|Цена одной упаковки|
|MENGE|ЦЕЛОЕ ЧИСЛО|Количество ресурса в упаковке (масса в кг)|

**PRODUCTS** — список изготавливаемых продуктов:

| Название | Тип | Описание |
|---|---|---|
|ID_PRODUCT|ЦЕЛОЕ ЧИСЛО|Идентификатор продукта|
|PRODUCT_NAME|СТРОКА|Название продукта|
|PRODUCT_NAME_EN|СТРОКА|Название продукта (англ.)|
|TYPE|СТРОКА|Тип сырья|
|PRICE|ЦЕЛОЕ ЧИСЛО|Цена одной упаковки|
|MENGE|ЦЕЛОЕ ЧИСЛО|Количество ресурса в упаковке (масса в кг)|

**BUY** — список заказов на сырьё:

| Название | Тип | Описание |
|---|---|---|
|ID_RESOURCE|ЦЕЛОЕ ЧИСЛО|Идентификатор сырья|
|ID_COUNTRY|ЦЕЛОЕ ЧИСЛО|Страна-покупатель|
|BUY_QUANTITY|ЦЕЛОЕ ЧИСЛО|Число заказанных упаковок|

**SELL** — список заказов на продукты:

| Название | Тип | Описание |
|---|---|---|
|ID_PRODUCT|ЦЕЛОЕ ЧИСЛО|Идентификатор продукта|
|ID_COUNTRY|ЦЕЛОЕ ЧИСЛО|Страна-покупатель|
|SELL_QUANTITY|ЦЕЛОЕ ЧИСЛО|Число заказанных упаковок|

### 4. Скрипт создания базы
Приведён в файле `database_settings.sql`.
```
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

```
### 5. Скрипт заполнения базы
Приведён в файле `database_filling.sql`.
```
INSERT INTO country(id_country, country_name, country_name_en) VALUES (1, 'АФГАНИСТАН', 'AFGHANISTAN');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (2, 'ТУРЦИЯ', 'TURKEY');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (3, 'МОЛДОВА', 'MOLDOVA');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (4, 'КАЗАХСТАН', 'KAZAKHSTAN');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (5, 'БЕЛАРУСЬ', 'BELARUS');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (6, 'ГРУЗИЯ', 'GEORGIA');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (7, 'УЗБЕКИСТАН', 'UZBEKISTAN');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (8, 'ГЕРМАНИЯ', 'GERMANY');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (9, 'ПОЛЬША', 'POLAND');
INSERT INTO country(id_country, country_name, country_name_en) VALUES (10, 'ТАДЖИКИСТАН', 'TAJIKISTAN');

INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (1, 'ПШЕНИЧНАЯ МУКА', 'WHEAT FLOUR', 'МУЧНОЕ', 'ОБЩЕГО НАЗНАЧЕНИЯ', '250', '50');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (2, 'СЕМЕНА ПОДСОЛНЕЧНИКА', 'SUNFLOWER SEEDS', 'МАСЛИЧНЫЕ', 'ВЫСШИЙ СОРТ', '350', '100');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (3, 'ВОДА', 'WATER', 'ЖИДКОСТИ', 'РАСХОДНИК', '10', '1000');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (4, 'МОЛОКО', 'MILK', 'МОЛОЧНЫЕ ПРОДУКТЫ', 'РАСХОДНИК', '590', '100');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (5, 'САХАР', 'SUGAR', 'САХАРА', 'ДЛЯ СИРОПА', '15', '100');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (6, 'ПАТОКА', 'TREACLE', 'КАРАМЕЛЬНОЕ', 'ДЛЯ СИРОПА', '780', '1040');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (7, 'ГРЕЦКИЙ ОРЕХ', 'WALNUT', 'ОРЕХИ', 'ДЛЯ НАЧИНКИ', '1730', '500');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (8, 'КУКУРУЗНАЯ МУКА', 'CORN FLOUR', 'ЗЛАКОВОЕ', 'ОБЩЕГО НАЗНАЧЕНИЯ', '290', '1060');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (9, 'АРАХИС', 'PEANUT', 'БОБОВЫЕ', 'В СКОРЛУПЕ', '1450', '300');
INSERT INTO resources(id_resource, resource_name, resource_name_en, res_type, mark, price, menge) VALUES (10, 'СМЕТАНА', 'SOUR CREAM', 'КИСЛОМОЛОЧКА', 'ДЛЯ НАЧИНКИ', '1730', '500');

INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (1, 'КОЗИНАКИ', 'KOZINAKI', 'МАСЛИЧНЫЕ', '2500', '50');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (2, 'ХАЛВА', 'HALVA', 'МАСЛИЧНЫЕ', '1300', '60');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (3, 'ПРЯНИКИ', 'TREACLE CAKES', 'МУЧНОЕ', '400', '10');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (4, 'ИРИС', 'TOFFEE', 'ХИМИЯ', '340', '220');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (5, 'ЗЕФИР', 'MARSHMALLOW', 'МОЛОЧНЫЕ ПРОДУКТЫ', '120', '15');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (6, 'ПАХЛАВА', 'PAHLAVA', 'ОРЕХИ', '765', '50');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (7, 'БУШЕ', 'BOUCHER', 'МУЧНОЕ', '710', '70');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (8, 'АРАХИСОВАЯ ПАСТА', 'PEANUT BUTTER', 'ОРЕХИ', '890', '110');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (9, 'ВАФЛИ', 'WAFER', 'МУЧНОЕ', '250', '150');
INSERT INTO products(id_product, product_name, product_name_en, res_type, price, menge) VALUES (10, 'ЩЕРБЕТ', 'SORBET', 'ХИМИЯ', '670', '100');
```

Для заполнения таблиц **BUY** и **SELL** воспользуемся функцией `random()`, генерирующей случайное вещественное число в диапазоне от 0 до 1 (например, 0,68213413412…). Умножим его на 10, чтобы получить целую часть от 0 до 9, выделим эту целую часть функцией ``trunc`` и прибавим единицу, потому что идентификаторы стран, сырья и продуктов варьируются от 1 до 10. Количество продаваемого и покупаемого товара зададим аналогично, считая, что его можно купить в объёме до 1000. Создадим по 50 строк каждой таблицы.
Скрипты приведены в файле `database_buysell.sql`.
```
INSERT INTO buy(id_resource, id_country, buy_quantity) VALUES (trunc(random()*10+1), trunc(random()*10+1), trunc(random()*1000+1));
-- SHOULD BE REPEATED 50 TIMES TO COMPLETE BUY TABLE

INSERT INTO sell(id_product, id_country, sell_quantity) VALUES (trunc(random()*10+1), trunc(random()*10+1), trunc(random()*1000+1))
-- SHOULD BE REPEATED 50 TIMES TO COMPLETE SELL TABLE
```
### 6. Запросы к базе
Запросы приведены в файле `database_answers.sql`.
```
-- FIRST QUERY

SELECT (
	SELECT SUM(sell_quantity)
	FROM sell
	WHERE id_product = (
		SELECT id_product
		FROM products
		WHERE product_name = 'ХАЛВА') AND id_country = (
			SELECT id_country
			FROM country
			WHERE country_name_en = 'MOLDOVA')
		) * (
				SELECT menge
				FROM products
				WHERE id_product = (
					SELECT id_product
					FROM products
					WHERE product_name = 'ХАЛВА')
	)

-- SECOND QUERY

SELECT country_name
FROM country
WHERE id_country = (
	SELECT id_country
	FROM buy
	WHERE id_resource = (
		SELECT id_resource
		FROM resources
		WHERE resource_name = 'ПШЕНИЧНАЯ МУКА') AND buy_quantity = (
			SELECT MAX(buy_quantity)
			FROM buy
			WHERE id_resource = (
				SELECT id_resource
				FROM resources
				WHERE resource_name = 'ПШЕНИЧНАЯ МУКА')
		)
	)

-- THIRD QUERY

SELECT trunc(trunc((SELECT (count(*))
FROM sell
WHERE id_country = (
	SELECT id_country
	FROM country
	WHERE country_name_en = 'TURKEY')), 1) / (
		SELECT (count(*))
		FROM sell
		WHERE id_country = (
			SELECT id_country
			FROM country
			WHERE country_name_en = 'KAZAKHSTAN')
		), 1)

-- FOURTH QUERY

SELECT country_name
FROM country
WHERE id_country = (
	SELECT id_country
	FROM sell
	WHERE id_product = (
		SELECT id_product
		FROM products
		WHERE product_name = 'ЗЕФИР') AND sell_quantity = (
			SELECT MIN(sell_quantity)
			FROM sell
			WHERE id_product = (
				SELECT id_product
				FROM products
				WHERE product_name = 'ЗЕФИР')
		)
	)

-- FIFTH QUERY

SELECT country_name
FROM country
WHERE id_country = (
	SELECT id_country
	FROM sell
	WHERE id_product = (
		SELECT id_product
		FROM products
		WHERE price = (
			SELECT MAX(price)
			FROM products)) AND sell_quantity = (
				SELECT MIN(sell_quantity)
				FROM sell
				WHERE id_product = (
					SELECT id_product
					FROM products
					WHERE price = (
						SELECT MAX(price)
						FROM products)
				)
			)
		) UNION 
SELECT country_name
FROM country
WHERE id_country = (
	SELECT id_country
	FROM buy
	WHERE id_resource = (
		SELECT id_resource
		FROM resources
		WHERE price = (
			SELECT MIN(price)
			FROM resources)
	) AND buy_quantity = (
		SELECT MAX(buy_quantity)
		FROM buy
		WHERE id_resource = (
			SELECT id_resource
			FROM resources
			WHERE price = (
				SELECT MIN(price)
				FROM resources)
			)
		)
	)
```
