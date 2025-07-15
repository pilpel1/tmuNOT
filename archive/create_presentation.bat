@echo off
chcp 65001 >nul
echo יוצר מצגת מהתמונות...
echo Creating presentation from images...

python generate_presentation.py

if %errorlevel% equ 0 (
    echo.
    echo ✓ המצגת נוצרה בהצלחה! / Presentation created successfully!
    echo פתח את presentation.html בדפדפן / Open presentation.html in browser
    echo.
    pause
) else (
    echo.
    echo ✗ שגיאה ביצירת המצגת / Error creating presentation
    echo.
    pause
) 