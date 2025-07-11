# יוצר מצגות תמונות / Image Presentation Generator

## עברית

### תיאור
כלי ליצירת מצגות HTML אינטראקטיביות מתמונות לצורך משחק חברה מבלבל ומצחיק! כל תמונה מוצגת על רקע אקראי - אדום או ירוק.

### חוקי המשחק
**משחק חברה לכל הגילאים - יכול להיות ראש בראש או קבוצות!**

- **רקע ירוק** 🟢: השחקן צריך להגיד **מה יש בתמונה**
- **רקע אדום** 🔴: השחקן צריך להגיד **משהו אחר** (לא מה שבתמונה!)
- חייבים לענות **מהר** ⚡
- הכי חשוב ש**יהיה מצחיק** 😂
- הקרינו על מסך או קיר לחוויה הטובה ביותר 📽️

**זכויות המשחק שמורות לדונקי - חרטטוני** ©️

### דרישות
- Python 3.x
- תמונות בפורמט JPG, JPEG או PNG

### איך להשתמש

1. **הכנת התמונות:**
   - שים את כל התמונות שלך בתיקיית `images/`
   - הכלי תומך בפורמטים: `.jpg`, `.jpeg`, `.png`

2. **יצירת המצגת:**
   ```bash
   # באמצעות הסקריפט:
   python generate_presentation.py
   
   # או באמצעות קובץ ה-bat:
   create_presentation.bat
   ```

3. **הצגת המצגת:**
   - פתח את הקובץ `presentation.html` בדפדפן
   - לחץ F11 למסך מלא
   - השתמש בחצים שמאל/ימין לניווט
   - או לחץ בחצי שמאל/ימין של המסך

### תכונות
- 📱 עיצוב רספונסיבי 16:9
- 🎨 רקע אקראי לכל תמונה (אדום/ירוק)
- ⌨️ ניווט עם מקלדת (חצים)
- 🖱️ ניווט עם עכבר (לחיצה)
- 🖼️ התאמה אוטומטית של גודל התמונות

### מבנה הקבצים
```
tmuNOT/
├── images/                    # תיקיית התמונות
├── generate_presentation.py   # הסקריפט הראשי
├── create_presentation.bat    # קובץ הפעלה מהיר
├── presentation.html          # המצגת שנוצרת
└── README.md                 # קובץ זה
```

---

## English

### Description
A tool for creating interactive HTML presentations from images for a fun and confusing party game! Each image is displayed on a random background - red or green.

### Game Rules
**A party game for all ages - can be played head-to-head or in teams!**

- **Green background** 🟢: Player must say **what's in the image**
- **Red background** 🔴: Player must say **something else** (not what's in the image!)
- Must answer **quickly** ⚡
- Most importantly, it should be **funny** 😂
- Project on a screen or wall for the best experience 📽️

**Game rights reserved to Donkey - Charttooni** ©️

### Requirements
- Python 3.x
- Images in JPG, JPEG, or PNG format

### How to Use

1. **Prepare Images:**
   - Place all your images in the `images/` folder
   - Supported formats: `.jpg`, `.jpeg`, `.png`

2. **Generate Presentation:**
   ```bash
   # Using the script:
   python generate_presentation.py
   
   # Or using the batch file:
   create_presentation.bat
   ```

3. **View Presentation:**
   - Open `presentation.html` in a browser
   - Press F11 for fullscreen
   - Use left/right arrow keys to navigate
   - Or click left/right half of the screen

### Features
- 📱 Responsive 16:9 design
- 🎨 Random background for each image (red/green)
- ⌨️ Keyboard navigation (arrow keys)
- 🖱️ Mouse navigation (click)
- 🖼️ Automatic image sizing

### File Structure
```
tmuNOT/
├── images/                    # Images folder
├── generate_presentation.py   # Main script
├── create_presentation.bat    # Quick run batch file
├── presentation.html          # Generated presentation
└── README.md                 # This file
```

### License
Free to use and modify. 