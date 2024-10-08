/*Query the sum of Northern Latitudes (LAT_N) from 
STATION having values greater than 38.7880 and less 
than 137.2345. Truncate your answer to  decimal places.

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

SELECT ROUND(SUM(LAT_N),4)
FROM STATION
WHERE LAT_N >38.7880 AND LAT_N<137.2345;