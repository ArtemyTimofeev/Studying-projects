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