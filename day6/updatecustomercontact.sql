show databases;
use w3schools;
delimiter @
create procedure updatecontacts(in customer_id int,in newcontactname varchar(100))
begin
update customers set ContactName=newcontactname
where CustomerID= customer_id;
select "customer contact updated" as message;
end @
delimiter ;
call updatecontacts(5,"pravalika")	

