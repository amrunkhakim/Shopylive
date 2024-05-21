@echo off

REM Memeriksa arsitektur sistem
if "%PROCESSOR_ARCHITECTURE%"=="AMD64" (
    set URL=https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/win64/chromedriver-win64.zip
) else (
    set URL=https://storage.googleapis.com/chrome-for-testing-public/125.0.6422.60/win32/chromedriver-win32.zip
)

echo Memulai pengunduhan...
python -c "import urllib.request; urllib.request.urlretrieve('%URL%', 'chromedriver.zip')"
echo Pengunduhan selesai.

REM Menginstal selenium
echo Menginstal selenium...
pip install selenium
echo Selenium telah diinstal.

REM Menginstal colorama
echo Menginstal colorama...
pip install colorama
echo Colorama telah diinstal.

pause
