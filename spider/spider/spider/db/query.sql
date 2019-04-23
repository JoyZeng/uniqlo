select distinct product.product_id, product.name, promo_commodity.price from
 (select * from commodity
 where is_promo=TRUE 
 and stock_quantity > 0 
 and commodity.product_id in
 (select product.id from product join kind on product.kind_id = kind.id where gender_name='WOMEN')
 and commodity.size_code_id in 
 (select size.code from size where size.name='XXS')
 ) as promo_commodity
 left join product on product.id=promo_commodity.product_id
