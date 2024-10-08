/*Query the list of CITY names from STATION which have vowels 
(i.e., a, e, i, o, and u) as both their first and last characters. 
Your result cannot contain duplicates.

Input Format

The STATION table is described as follows:
+-------------+------------+
| Field       |   Type     |
+-------------+------------+
| ID          | INTEGER    |
| CITY        | VARCHAR(21)|
| STATE       | VARCHAR(2) |
| LAT_N       | NUMERIC    |
| LONG_W      | NUMERIC    |
+-------------+------------+
where LAT_N is the northern latitude and LONG_W is the western longitude.
*/

SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '^[AEIOU].*[AEIOU]$'; /*Esta consulta para MYSQL
Para trabajar por postgreeSQL seria lo siguiente:
WHERE CITY SIMILAR TO '[AEIOU]%[AEIOU]'
*/