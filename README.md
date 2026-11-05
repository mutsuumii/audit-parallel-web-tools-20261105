# Security audit: parallel-web/parallel-web-tools

Date: 2026-11-05 | Auditor: [mutsuumii](https://github.com/mutsuumii)

## Summary

Found 21 issue(s): 2 critical, 19 high.

## Findings

### 1. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_service.py` line 199

Credentials hardcoded in source. Anyone with repo access can extract them.

```
return _api_key_response(raw_api_key="sk_provisioned")
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 2. [CRITICAL] SQL injection via string formatting

**CWE-89** | `parallel_web_tools/integrations/duckdb/findall.py` line 183

SQL query built by string formatting. Attacker can inject arbitrary SQL.

```
conn.execute(f"CREATE TEMP TABLE {temp_quoted} ({col_defs})")
```

**Fix:** Use parameterized queries: cursor.execute('SELECT * FROM t WHERE id=%s', (val,))
---

### 3. [CRITICAL] SQL injection via string formatting

**CWE-89** | `parallel_web_tools/integrations/duckdb/findall.py` line 195

SQL query built by string formatting. Attacker can inject arbitrary SQL.

```
conn.execute(f"CREATE OR REPLACE TABLE {result_quoted} AS SELECT * FROM {temp_quoted}")
```

**Fix:** Use parameterized queries: cursor.execute('SELECT * FROM t WHERE id=%s', (val,))
---

### 4. [HIGH] Hardcoded credentials

**CWE-798** | `parallel_web_tools/integrations/spark/udf.py` line 200

Credentials hardcoded in source. Anyone with repo access can extract them.

```
>>> register_parallel_udfs(spark, api_key="your-key")
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 5. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 156

Credentials hardcoded in source. Anyone with repo access can extract them.

```
access_token="at_123",
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 6. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 157

Credentials hardcoded in source. Anyone with repo access can extract them.

```
refresh_token="rt_123",
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 7. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 490

Credentials hardcoded in source. Anyone with repo access can extract them.

```
_persist_token_response(_token_response(access_token="at_new", refresh_token="rt_new", org_id="org_real"))
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 8. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 544

Credentials hardcoded in source. Anyone with repo access can extract them.

```
orgs={credentials.LEGACY_ORG_ID: credentials.OrgCredentials(api_key="legacy_key")},
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 9. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 548

Credentials hardcoded in source. Anyone with repo access can extract them.

```
token_resp = _token_response(access_token="at_new", refresh_token="rt_new", org_id="org_real")
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 10. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 726

Credentials hardcoded in source. Anyone with repo access can extract them.

```
orgs={"org_a": credentials.OrgCredentials(api_key="stored_key", org_name="Acme Org")},
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 11. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 800

Credentials hardcoded in source. Anyone with repo access can extract them.

```
control_api=credentials.ControlApiTokens(refresh_token="rt_keep"),
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 12. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 842

Credentials hardcoded in source. Anyone with repo access can extract them.

```
control_api=credentials.ControlApiTokens(refresh_token="rt_shared"),
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 13. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 845

Credentials hardcoded in source. Anyone with repo access can extract them.

```
control_api=credentials.ControlApiTokens(refresh_token="rt_shared"),
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 14. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 861

Credentials hardcoded in source. Anyone with repo access can extract them.

```
control_api=credentials.ControlApiTokens(refresh_token="rt_bad"),
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 15. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 886

Credentials hardcoded in source. Anyone with repo access can extract them.

```
create_client(api_key="test-key-123", source="cli")
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 16. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 991

Credentials hardcoded in source. Anyone with repo access can extract them.

```
api_key="sk_data",
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 17. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 1023

Credentials hardcoded in source. Anyone with repo access can extract them.

```
return_value=_token_response(access_token="at_refreshed", refresh_token="rt_new"),
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 18. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_auth.py` line 1043

Credentials hardcoded in source. Anyone with repo access can extract them.

```
return_value=_token_response(access_token="at_refreshed"),
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 19. [HIGH] Hardcoded credentials

**CWE-798** | `parallel_web_tools/integrations/snowflake/__init__.py` line 15

Credentials hardcoded in source. Anyone with repo access can extract them.

```
password="your-password",
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 20. [HIGH] Hardcoded credentials

**CWE-798** | `parallel_web_tools/integrations/snowflake/__init__.py` line 16

Credentials hardcoded in source. Anyone with repo access can extract them.

```
parallel_api_key="your-api-key",
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---

### 21. [HIGH] Hardcoded credentials

**CWE-798** | `tests/test_findall.py` line 231

Credentials hardcoded in source. Anyone with repo access can extract them.

```
ingest_findall("query", api_key="test-key", source="cli")
```

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
---
