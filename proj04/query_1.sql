SELECT table_2.student_name AS name, table_2.grade, table_1.major
FROM table_2
LEFT OUTER JOIN table_1
ON netid=msu_netid
ORDER BY student_name;