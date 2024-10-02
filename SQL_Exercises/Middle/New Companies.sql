/*Amber's conglomerate corporation just acquired some new companies. Each of the companies follows this hierarchy:
- Founder -> Lead Manager -> Senior Manager -> Manager -> Employee
 
Given the table schemas below, write a query to print the company_code, founder name, total number of lead managers, 
total number of senior managers, total number of managers, and total number of employees. Order your output by ascending 
company_code.

Note:

- The tables may contain duplicate records.
- The company_code is string, so the sorting should not be numeric. For example, if the company_codes are C_1, C_2, and C_10, 
then the ascending company_codes will be C_1, C_10, and C_2.

Input Format

The following tables contain company data:

- Company: The company_code is the code of the company and founder is the founder of the company.

+-------------+------------+        
| Column      |   Type     | 
+-------------+------------+
|company_code | String     | 
| Founder     | String     |
+-------------+------------+

Lead_Manager: The lead_manager_code is the code of the lead manager, and the company_code is the code of the working company.

+-------------------+------------+        
| Column            |   Type     | 
+-------------------+------------+
| Lead_manager_code | String     | 
| Company_code      | String     |
+-------------------+------------+
...
*/

SELECT C.COMPANY_CODE, C.FOUNDER,
       COUNT(DISTINCT LM.LEAD_MANAGER_CODE) AS Lead_Manager_Count,
       COUNT(DISTINCT SM.SENIOR_MANAGER_CODE) AS Senior_Manager_Count,
       COUNT(DISTINCT M.MANAGER_CODE) AS Manager_Count,
       COUNT(DISTINCT E.EMPLOYEE_CODE) AS Employee_Count
FROM COMPANY C
LEFT JOIN LEAD_MANAGER LM ON C.COMPANY_CODE = LM.COMPANY_CODE
LEFT JOIN SENIOR_MANAGER SM ON C.COMPANY_CODE = SM.COMPANY_CODE
LEFT JOIN MANAGER M ON C.COMPANY_CODE = M.COMPANY_CODE
LEFT JOIN EMPLOYEE E ON C.COMPANY_CODE = E.COMPANY_CODE
GROUP BY C.COMPANY_CODE, C.FOUNDER
ORDER BY C.COMPANY_CODE;