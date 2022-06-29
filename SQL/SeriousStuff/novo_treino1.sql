CREATE DATABASE ;

SELECT * 
FROM produts
WHERE stock  IN (49,38,72);


SELECT *
FROM clients
WHERE points BETWEEN 1000 AND 3000;

SELECT *
FROM clients
WHERE birtday BETWEEN '1990-01-01' AND '2000-12-01';
LIMIT 5,10 --offset, skips first 10 clients, than shows the other 5

-- % = Any nuymber of characters
-- _ = 1 character

SELECT *
FROM clients
WHERE adress LIKE '%TRAIL%' OR 
adress LIKE '%AVENUE%' AND -- Adress REGEX 'Avenue|trail'
 phone_number LIKE '%9'; --phone_number  REGEX '9$';

 SELECT *, quantity*price AS 'total price'
 FROM order_items
 WHERE order_id = 2
 ORDER BY 'total price' DESC;

SELECT *
FROM clients
ORDER BY points DESC
LIMIT 3;

SELECT 
    order_id, 
    o.customer_id,
    first_name,
    last_name
    FROM orders o
    JOIN customers c ON o.customer_id = c.customer_id
        LIMIT 10;

SELECT 
    order_id,
    o.product_id,
    p.name,
    quantity,
    o.unit_price
    FROM order-items o
    JOIN products c on o.product_id = c.product_id;

SELECT 
    pm.payment_id,
    c.name,
    invoice_id,
    date,
    p.amount,
    pm.name
    FROM payments p 
    JOIN payment_methods pm 
        ON pm.payment_method_id = p.payment_method
    JOIN clients c 
        ON c.client_id = p.client_id;


-- 