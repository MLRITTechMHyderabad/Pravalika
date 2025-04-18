show databases;
use w3schools;
delimiter @
create procedure GetEmployeeSale(in employee_id int)
begin
select count(o.OrderID) as ordercount,sum(products.UnitPrice*od.Quantity* (1-products.Discount))
as totalsales from orders o inner join order_details od on od.OrderID=o.OrderID WHERE
o.EmployeeID=employee_id;
end @
delimiter ;
call GetEmployeeSales(4)

