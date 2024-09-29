/*Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.

Note: CITY.CountryCode and COUNTRY.Code are matching key columns.

Input Format

The CITY and COUNTRY tables are described as follows:
+-------------+------------+                +-----------------+---------------+     
| Field      |   Type      |                | Field           |   Type        |  
+-------------+------------+                +-----------------+---------------+
| ID         | NUMBER      |                | CODE            | VARCHAR2(3)   |
| NAME       | VARCHAR2(17)|                | NAME            | VARCHAR2(44)  |
| COUNTRYCODE| VARCHAR2(3) |                | CONTINENT       | VARCHAR2(13)  |
| DISTRICT   | VARCHAR2(20)|                | REGION          | VARCHAR2(25)  |
| POPULATION | NUMBER      |                | SURFACEAREA     | NUMBER        |
+-------------+------------+                | INDEPYEAR       | VARCHAR2(5)   |     
                                            | POPULATION      | NUMBER        |
                                            | LIFEEXPECTANCY  | VARCHAR2(4)   |   
                                            | GNP             | NUMBER        |   
                                            | GNPOLD          | VARCHAR2(9)   |   
                                            | LOCALNAME       | VARCHAR2(44)  |   
                                            | GOVERNMENTFORM  | VARCHAR2(44)  |   
                                            | HEADOFSTATE     | VARCHAR2(32)  |   
                                            | CAPITAL         | VARCHAR2(4)   |   
                                            | CODE2           | VARCHAR2(2)   |   
                                            +-----------------+---------------+
*/

SELECT CITY.NAME
FROM CITY
JOIN COUNTRY ON CITY.COUNTRYCODE = COUNTRY.CODE
WHERE COUNTRY.CONTINENT = 'Africa';