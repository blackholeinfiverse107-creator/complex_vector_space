@echo off
echo Trying python...
python run_tests.py
if exist test_results.txt goto end

echo Trying py...
py run_tests.py
if exist test_results.txt goto end

echo Trying python3...
python3 run_tests.py
if exist test_results.txt goto end

:end
echo Done.
