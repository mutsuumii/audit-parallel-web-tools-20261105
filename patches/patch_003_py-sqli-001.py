# SQL injection via string formatting
# CWE-89 | Severity: CRITICAL
# File: parallel_web_tools/integrations/duckdb/findall.py line 195

**Risk:** SQL query built by string formatting. Attacker can inject arbitrary SQL.

**Fix:** Use parameterized queries: cursor.execute('SELECT * FROM t WHERE id=%s', (val,))
