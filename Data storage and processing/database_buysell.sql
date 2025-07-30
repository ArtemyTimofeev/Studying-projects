INSERT INTO buy(id_resource, id_country, buy_quantity) VALUES (trunc(random()*10+1), trunc(random()*10+1), trunc(random()*1000+1));
-- SHOULD BE REPEATED 50 TIMES TO COMPLETE BUY TABLE

INSERT INTO sell(id_product, id_country, sell_quantity) VALUES (trunc(random()*10+1), trunc(random()*10+1), trunc(random()*1000+1))

-- SHOULD BE REPEATED 50 TIMES TO COMPLETE SELL TABLE