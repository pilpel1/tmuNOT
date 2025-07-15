# tmuNOT - משחק תמונות / Image Game

## עברית

### תיאור
משחק HTML אינטראקטיבי מתמונות לצורך משחק חברה מבלבל ומצחיק! כל תמונה מוצגת על רקע אקראי - אדום או ירוק.

### חוקי המשחק
**משחק חברה לכל הגילאים - יכול להיות ראש בראש או קבוצות!**

- **רקע ירוק** 🟢: השחקן צריך להגיד **מה יש בתמונה**
- **רקע אדום** 🔴: השחקן צריך להגיד **משהו אחר** (לא מה שבתמונה!)
- חייבים לענות **מהר** ⚡
- הכי חשוב ש**יהיה מצחיק** 😂
- הקרינו על מסך או קיר לחוויה הטובה ביותר 📽️
- ניתן לשחק גם במפגש וירטואלי באמצעות שיתוף מסך 💻

**זכויות המשחק שמורות לדונקי - [חרטטוני](https://youtu.be/0VcDc3aWCDE?feature=shared&t=763){:target="_blank"}** ©️

### דרישות
- דפדפן מודרני (Chrome, Firefox, Safari, Edge)
- תמונות בפורמט JPG, JPEG, PNG או GIF

### איך להשתמש

1. **פתח את המשחק:**
   - פתח את הקובץ `html-version/tmuNOT-game.html` בדפדפן
   - או הורד והפעל מקומית

2. **בחר תמונות:**
   - לחץ על "בחר תמונות" או "בחר תיקיית תמונות"
   - או פשוט גרור תמונות למסך
   - תומך בפורמטים: `.jpg`, `.jpeg`, `.png`, `.gif`

3. **התאם הגדרות:**
   - זמן לתמונה (1-30 שניות)
   - תמונות לסבב (או ללא הפסקות)
   - שפה (עברית/אנגלית)

4. **התחל לשחק:**
   - לחץ על "התחל משחק"
   - לחץ F11 למסך מלא
   - השתמש בחצים שמאל/ימין לניווט או לחץ בחצי שמאל/ימין של המסך
   - רווח להשהיה/המשכה

### תכונות
- 📱 עיצוב רספונסיבי למכשירים שונים
- 🎨 רקע אקראי לכל תמונה (אדום/ירוק) - מקסימום 3 ברצף
- ⏱️ טיימר אוטומטי עם בר התקדמות וזמן מתכוונן
- 🎬 מסך פתיחה עם הגדרות משחק
- ⏸️ הפסקות אוטומטיות כל מספר תמונות (ניתן להגדרה)
- 📊 מונה התקדמות (תמונה נוכחית מתוך כולל)
- ⌨️ ניווט עם מקלדת (חצים, רווח לפאוז)
- 🖱️ ניווט עם עכבר (לחיצה)
- 🖼️ התאמה אוטומטית של גודל התמונות
- 🌐 תמיכה בעברית ואנגלית
- 📂 בחירת תמונות בגרירה או דפדוף

### מבנה הקבצים
```
tmuNOT/
├── html-version/
│   └── tmuNOT-game.html      # המשחק הראשי
├── archive/                   # קבצים ישנים (גישה Python)
│   ├── generate_presentation.py
│   └── create_presentation.bat
├── images/                    # תיקיית תמונות לדוגמה
└── README.md                 # קובץ זה
```

---

## English

### Description
An interactive HTML game from images for a fun and confusing party game! Each image is displayed on a random background - red or green.

### Game Rules
**A party game for all ages - can be played head-to-head or in teams!**

- **Green background** 🟢: Player must say **what's in the image**
- **Red background** 🔴: Player must say **something else** (not what's in the image!)
- Must answer **quickly** ⚡
- Most importantly, it should be **funny** 😂
- Project on a screen or wall for the best experience 📽️
- Can also be played in virtual meetings via screen sharing 💻

**Game rights reserved to Donkey - [Hartetooni](https://youtu.be/0VcDc3aWCDE?feature=shared&t=763){:target="_blank"}** ©️

### Requirements
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Images in JPG, JPEG, PNG, or GIF format

### How to Use

1. **Open the Game:**
   - Open `html-version/tmuNOT-game.html` in a web browser
   - Or download and run locally

2. **Select Images:**
   - Click "Select Images" or "Select Image Folder"
   - Or simply drag images to the screen
   - Supports formats: `.jpg`, `.jpeg`, `.png`, `.gif`

3. **Configure Settings:**
   - Time per image (1-30 seconds)
   - Images per round (or no breaks)
   - Language (Hebrew/English)

4. **Start Playing:**
   - Click "Start Game"
   - Press F11 for fullscreen
   - Use left/right arrow keys to navigate or click left/right half of the screen
   - Space to pause/resume

### Features
- 📱 Responsive design for different devices
- 🎨 Random background for each image (red/green) - max 3 consecutive
- ⏱️ Auto-timer with progress bar and configurable timing
- 🎬 Start screen with game settings
- ⏸️ Automatic breaks every configurable number of slides
- 📊 Progress counter (current slide of total)
- ⌨️ Keyboard navigation (arrows, space to pause)
- 🖱️ Mouse navigation (click)
- 🖼️ Automatic image sizing
- 🌐 Hebrew and English support
- 📂 Drag & drop or browse image selection

### File Structure
```
tmuNOT/
├── html-version/
│   └── tmuNOT-game.html      # Main game file
├── archive/                   # Old files (Python approach)
│   ├── generate_presentation.py
│   └── create_presentation.bat
├── images/                    # Sample images folder
└── README.md                 # This file
```

### License
Free to use and modify. 