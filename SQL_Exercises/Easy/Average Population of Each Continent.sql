/*Given the CITY and COUNTRY tables, query the names of all the continents (COUNTRY.Continent) and their 
respective average city populations (CITY.Population) rounded down to the nearest integer.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Input Format

The CITY and COUNTRY tables are described as follows:
+-------------+------------+
| Field      |   Type      |
+-------------+------------+
| ID         | NUMBER      |
| NAME       | VARCHAR2(17)|
| COUNTRYCODE| VARCHAR2(3) |
| DISTRICT   | VARCHAR2(20)|
| POPULATION | NUMBER      |
+-------------+------------+
*/

SELECT COUNTRY.Continent, FLOOR(AVG(CITY.Population))
FROM COUNTRY
JOIN CITY ON CITY.COUNTRYCODE = COUNTRY.CODE
GROUP BY COUNTRY.CONTINENT;