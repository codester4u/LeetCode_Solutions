select user_id, concat(upper(left(name, 1)),lower(substring(name, 2))) as name from Users order by user_id;Day 3
String Processing Functions