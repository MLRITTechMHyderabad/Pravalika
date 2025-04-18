show databases;
use w3schools;
delimiter @
create procedure getcustomerorders(in customer_id int)
begin
select o.OrderID, o.OrderDate, s.ShipperName from orders o 
inner join shippers s on s.ShipperID = o.ShipperID
where o.CustomerID= customer_id;
end @
delimiter ;
call getcustomerorders(2)

