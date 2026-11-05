# Hardcoded credentials
# CWE-798 | Severity: HIGH
# File: parallel_web_tools/integrations/snowflake/__init__.py line 15

**Risk:** Credentials hardcoded in source. Anyone with repo access can extract them.

**Fix:** Use os.environ.get('SECRET') or a secrets manager. Never commit credentials.
