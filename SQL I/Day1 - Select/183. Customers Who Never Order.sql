# Write your MySQL query statement below
select Name as customers from customers where id not in(Select customerid from orders);