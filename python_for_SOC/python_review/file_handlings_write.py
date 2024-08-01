file_path = '../files/security_report.txt'

report_content = """Security Report
Date: 2024-07-26
Analyst: John Doe

Findings:
1. Multiple failed login attempts detected
2. Unusual network traffic observed
3. All critical systems are up-to-date

Recommendations:
- Implement multi-factor authentication
- Investigate source of unusual traffic
- Continue regular system updates
"""

with open(file_path, 'w') as file:
    file.write(report_content)