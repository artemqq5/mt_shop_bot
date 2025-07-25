@echo off

echo -----------------------------
echo Removing unused imports...
autoflake --remove-all-unused-imports --recursive --in-place bot --exclude=venv

echo -----------------------------
echo Sorting imports (isort)...
isort ./bot

echo -----------------------------
echo Formatting code (black)...
black ./bot

echo -----------------------------
echo Checking style (flake8)...
flake8 ./bot

@REM echo -----------------------------
@REM echo Running static analysis (pylint)...
@REM pylint ./bot
@REM
@REM echo -----------------------------
@REM echo Running security checks (bandit)...
@REM bandit -r ./bot --exclude ./venv

echo ✅ All checks completed!
