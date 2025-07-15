import os
import random
import glob

# Configuration
SLIDE_DURATION = 4  # seconds per slide
BREAK_INTERVAL = 10  # slides before break

def generate_html():
    # Get all images: jpg, jpeg, png
    image_dir = 'images'
    images = [os.path.join(image_dir, f).replace('\\', '/') for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)  # Randomize order
    print(f"Found {len(images)} images")
    
    slides = []
    last_color = None
    color_count = 0
    
    for img in images:
        # Prevent more than 3 consecutive same colors
        if color_count >= 3:
            # Force opposite color
            color = 'green' if last_color == 'red' else 'red'
            color_count = 1
        else:
            # Random choice
            color = random.choice(['red', 'green'])
            if color == last_color:
                color_count += 1
            else:
                color_count = 1
        
        last_color = color
        
        slide = f"""
        <div class="slide" style="background-color: {color};">
            <img src="{img}" alt="Slide Image">
        </div>
        """
        slides.append(slide)
    
    html = f"""
<!DOCTYPE html>
<html lang="he">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Presentation</title>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;700&display=swap" rel="stylesheet">
    <style>
        body {{
            margin: 0;
            padding: 0;
            overflow: hidden;
            background-color: black;
            outline: none;
        }}
        .slide {{
            display: flex;
            width: 100vw;
            height: 100vh;
            align-items: center;
            justify-content: center;
            outline: none;
            opacity: 0;
            position: absolute;
            top: 0;
            left: 0;
        }}
        .slide.active {{
            opacity: 1;
        }}
        .slide img {{
            max-width: 90%;
            max-height: 90%;
            object-fit: contain;
        }}
        
        .progress-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 8px;
            background-color: rgba(0, 0, 0, 0.3);
            z-index: 1000;
            border-bottom: 1px solid rgba(255, 255, 255, 0.2);
        }}
        
        .progress-bar {{
            height: 100%;
            width: 0%;
            background-color: rgba(255, 255, 255, 0.8);
            transition: none;
        }}
        
        .start-screen {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        
        .start-screen.hidden {{
            display: none;
        }}
        
        .start-left {{
            position: absolute;
            top: 0;
            left: 0;
            width: 50%;
            height: 100%;
            background-color: red;
        }}
        
        .start-right {{
            position: absolute;
            top: 0;
            right: 0;
            width: 50%;
            height: 100%;
            background-color: green;
        }}
        
        .play-button {{
            position: relative;
            width: 120px;
            height: 120px;
            background-color: rgba(255, 255, 255, 0.9);
            border: 3px solid rgba(0, 0, 0, 0.3);
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            z-index: 2001;
        }}
        
        .play-button:hover {{
            background-color: rgba(255, 255, 255, 1);
            transform: scale(1.1);
        }}
        
        .play-triangle {{
            width: 0;
            height: 0;
            border-left: 30px solid rgba(0, 0, 0, 0.7);
            border-top: 20px solid transparent;
            border-bottom: 20px solid transparent;
            margin-left: 8px;
        }}
        
        .slide-counter {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 8px 12px;
            border-radius: 6px;
            font-family: 'Courier New', monospace;
            font-size: 16px;
            font-weight: bold;
            z-index: 1500;
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        
        .slide-counter.visible {{
            opacity: 1;
        }}
        
        .break-screen {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100vw;
            height: 100vh;
            z-index: 2000;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-direction: column;
        }}
        
        .break-screen.hidden {{
            display: none;
        }}
        
        .break-left {{
            position: absolute;
            top: 0;
            left: 0;
            width: 50%;
            height: 100%;
            background-color: red;
        }}
        
        .break-right {{
            position: absolute;
            top: 0;
            right: 0;
            width: 50%;
            height: 100%;
            background-color: green;
        }}
        
        .break-content {{
            position: relative;
            z-index: 2001;
            text-align: center;
            color: white;
            margin-bottom: 30px;
            direction: rtl;
            font-family: 'Heebo', sans-serif;
        }}
        
        .break-title {{
            font-size: 48px;
            font-weight: bold;
            margin-bottom: 20px;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.8);
        }}
        
        .break-info {{
            font-size: 24px;
            margin-bottom: 10px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        }}
        
        .continue-button {{
            position: relative;
            width: 120px;
            height: 120px;
            background-color: rgba(255, 255, 255, 0.9);
            border: 3px solid rgba(0, 0, 0, 0.3);
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: all 0.3s ease;
            z-index: 2001;
        }}
        
        .continue-button:hover {{
            background-color: rgba(255, 255, 255, 1);
            transform: scale(1.1);
        }}
        
        .continue-triangle {{
            width: 0;
            height: 0;
            border-left: 30px solid rgba(0, 0, 0, 0.7);
            border-top: 20px solid transparent;
            border-bottom: 20px solid transparent;
            margin-left: 8px;
        }}
        
        .settings-button {{
            position: absolute;
            bottom: 30px;
            left: 30px;
            width: 50px;
            height: 50px;
            background-color: rgba(0, 0, 0, 0.8);
            color: white;
            border: 2px solid rgba(255, 255, 255, 0.3);
            border-radius: 50%;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 20px;
            transition: all 0.3s ease;
            z-index: 2001;
        }}
        
        .settings-button:hover {{
            background-color: rgba(0, 0, 0, 0.9);
            transform: scale(1.1);
        }}
        
        .settings-panel {{
            position: absolute;
            bottom: 90px;
            left: 30px;
            background-color: rgba(0, 0, 0, 0.9);
            color: white;
            padding: 20px;
            border-radius: 10px;
            font-family: 'Heebo', sans-serif;
            direction: rtl;
            text-align: right;
            z-index: 2001;
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s ease;
            pointer-events: none;
        }}
        
        .settings-panel.visible {{
            opacity: 1;
            transform: translateY(0);
            pointer-events: all;
        }}
        
        .settings-title {{
            font-size: 18px;
            font-weight: bold;
            margin-bottom: 15px;
            text-align: right;
        }}
        
        .setting-item {{
            margin-bottom: 12px;
            display: flex;
            align-items: center;
            justify-content: flex-start;
            gap: 10px;
        }}
        
        .setting-label {{
            font-size: 14px;
            min-width: 100px;
        }}
        
        .setting-input {{
            background-color: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.5);
            border-radius: 5px;
            padding: 5px 8px;
            font-size: 14px;
            width: 60px;
            text-align: center;
            color: black;
        }}
        
        .setting-select {{
            background-color: rgba(255, 255, 255, 0.9);
            border: 1px solid rgba(255, 255, 255, 0.5);
            border-radius: 5px;
            padding: 5px 8px;
            font-size: 14px;
            width: 120px;
            color: black;
            font-family: 'Heebo', sans-serif;
            cursor: pointer;
        }}
        
        .save-button {{
            background-color: rgba(76, 175, 80, 0.9);
            color: white;
            border: none;
            border-radius: 5px;
            padding: 8px 16px;
            font-size: 14px;
            font-family: 'Heebo', sans-serif;
            cursor: pointer;
            margin-top: 10px;
            transition: all 0.3s ease;
        }}
        
        .save-button:hover {{
            background-color: rgba(76, 175, 80, 1);
        }}
        
        .save-button.success {{
            background-color: rgba(46, 125, 50, 1);
        }}
    </style>
  </head>
  <body>
      <div class="start-screen" id="startScreen">
          <div class="start-left"></div>
          <div class="start-right"></div>
          <div class="play-button" id="playButton">
              <div class="play-triangle"></div>
          </div>
          <div class="settings-button" id="settingsButton">
              ⚙️
          </div>
          <div class="settings-panel" id="settingsPanel">
              <div class="settings-title">הגדרות משחק</div>
              <div class="setting-item">
                  <label class="setting-label">זמן לתמונה (שניות):</label>
                  <input type="number" id="slideDuration" class="setting-input" value="4" min="1" max="30">
              </div>
              <div class="setting-item">
                  <label class="setting-label">תמונות לסבב:</label>
                  <select id="breakInterval" class="setting-select">
                      <option value="5">5 תמונות</option>
                      <option value="10" selected>10 תמונות</option>
                      <option value="15">15 תמונות</option>
                      <option value="20">20 תמונות</option>
                      <option value="25">25 תמונות</option>
                      <option value="0">ללא הפסקות</option>
                  </select>
              </div>
              <button class="save-button" id="saveButton">שמור הגדרות</button>
          </div>
      </div>
      
      <div class="progress-container">
          <div class="progress-bar" id="progressBar"></div>
      </div>
      
      <div class="slide-counter" id="slideCounter">1/{len(images)}</div>
      
      <div class="break-screen hidden" id="breakScreen">
          <div class="break-left"></div>
          <div class="break-right"></div>
          <div class="break-content">
              <div class="break-title">הפסקה!</div>
              <div class="break-info" id="breakInfo">סבב 1 הסתיים</div>
              <div class="break-info" id="breakProgress">תמונות 1-10 מתוך {len(images)}</div>
          </div>
          <div class="continue-button" id="continueButton">
              <div class="continue-triangle"></div>
          </div>
      </div>
      
      {''.join(slides)}
    
    <script>
        let SLIDE_DURATION = {int(SLIDE_DURATION * 1000)}; // milliseconds (default)
        let BREAK_INTERVAL = {BREAK_INTERVAL}; // slides before break (default)
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const progressBar = document.getElementById('progressBar');
        const startScreen = document.getElementById('startScreen');
        const playButton = document.getElementById('playButton');
        const slideCounter = document.getElementById('slideCounter');
        const breakScreen = document.getElementById('breakScreen');
        const continueButton = document.getElementById('continueButton');
        const breakInfo = document.getElementById('breakInfo');
        const breakProgress = document.getElementById('breakProgress');
        const slideDurationInput = document.getElementById('slideDuration');
        const breakIntervalSelect = document.getElementById('breakInterval');
        const settingsButton = document.getElementById('settingsButton');
        const settingsPanel = document.getElementById('settingsPanel');
        const saveButton = document.getElementById('saveButton');
        
        // Game state
        let gameStarted = false;
        let onBreak = false;
        let settingsVisible = false;
        
        // Timer state
        let timerState = 'stopped'; // 'running', 'paused', 'stopped'
        let startTime = null;
        let pausedTime = 0;
        let animationId = null;
        
        function showSlide(n) {{
            console.log('Showing slide:', n, 'of', slides.length);
            slides.forEach((slide, index) => {{
                slide.classList.remove('active');
                if (index === n) {{
                    slide.classList.add('active');
                }}
            }});
            
            // Update slide counter
            slideCounter.textContent = `${{n + 1}}/${{slides.length}}`;
            
            if (gameStarted) {{
                resetTimer();
            }}
        }}
        
        function startGame() {{
            // Read settings from UI
            const durationValue = parseInt(slideDurationInput.value);
            const intervalValue = parseInt(breakIntervalSelect.value);
            
            // Validate and apply settings
            if (durationValue >= 1 && durationValue <= 30) {{
                SLIDE_DURATION = durationValue * 1000; // convert to milliseconds
            }}
            
            BREAK_INTERVAL = intervalValue; // 0 means no breaks
            
            gameStarted = true;
            startScreen.classList.add('hidden');
            slideCounter.classList.add('visible');
            showSlide(0);
        }}
        
        function showBreakScreen() {{
            onBreak = true;
            timerState = 'paused';
            if (animationId) {{
                cancelAnimationFrame(animationId);
            }}
            
            const roundNumber = Math.floor(currentSlide / BREAK_INTERVAL);
            const startSlide = (roundNumber - 1) * BREAK_INTERVAL + 1;
            const endSlide = roundNumber * BREAK_INTERVAL;
            
            breakInfo.textContent = `סבב ${{roundNumber}} הסתיים`;
            breakProgress.textContent = `תמונות ${{startSlide}}-${{endSlide}} מתוך ${{slides.length}}`;
            
            breakScreen.classList.remove('hidden');
        }}
        
        function hideBreakScreen() {{
            onBreak = false;
            breakScreen.classList.add('hidden');
            if (gameStarted && currentSlide < slides.length - 1) {{
                resetTimer();
            }}
        }}
        
        function toggleSettings() {{
            settingsVisible = !settingsVisible;
            if (settingsVisible) {{
                settingsPanel.classList.add('visible');
            }} else {{
                settingsPanel.classList.remove('visible');
            }}
        }}
        
        function saveSettings() {{
            // Read and validate settings
            const durationValue = parseInt(slideDurationInput.value);
            const intervalValue = parseInt(breakIntervalSelect.value);
            
            if (durationValue >= 1 && durationValue <= 30) {{
                // Show success feedback
                saveButton.textContent = '✓ נשמר!';
                saveButton.classList.add('success');
                
                setTimeout(() => {{
                    saveButton.textContent = 'שמור הגדרות';
                    saveButton.classList.remove('success');
                }}, 2000);
                
                // Hide settings panel
                setTimeout(() => {{
                    toggleSettings();
                }}, 1000);
            }} else {{
                // Show error
                saveButton.textContent = 'שגיאה - בדוק ערכים';
                setTimeout(() => {{
                    saveButton.textContent = 'שמור הגדרות';
                }}, 2000);
            }}
        }}
        
        function resetTimer() {{
            if (!gameStarted || onBreak) return;
            
            if (animationId) {{
                cancelAnimationFrame(animationId);
            }}
            startTime = null;
            pausedTime = 0;
            progressBar.style.width = '0%';
            
            if (currentSlide < slides.length - 1) {{
                timerState = 'running';
                setTimeout(() => {{
                    updateProgress();
                }}, 50);
            }} else {{
                timerState = 'stopped';
                progressBar.style.width = '100%';
            }}
        }}
        
        function pauseTimer() {{
            if (timerState === 'running') {{
                timerState = 'paused';
                if (animationId) {{
                    cancelAnimationFrame(animationId);
                }}
            }}
        }}
        
        function resumeTimer() {{
            if (timerState === 'paused' && currentSlide < slides.length - 1) {{
                timerState = 'running';
                updateProgress();
            }}
        }}
        
        function toggleTimer() {{
            if (timerState === 'running') {{
                pauseTimer();
            }} else if (timerState === 'paused') {{
                resumeTimer();
            }}
        }}
        
        function updateProgress() {{
            if (timerState !== 'running') return;
            
            const now = Date.now();
            if (!startTime) {{
                startTime = now - pausedTime;
            }}
            
            const elapsed = now - startTime;
            const progress = Math.min(elapsed / SLIDE_DURATION, 1);
            
            progressBar.style.width = (progress * 100) + '%';
            
            if (progress >= 1) {{
                // Show 100% for a brief moment before advancing
                progressBar.style.width = '100%';
                setTimeout(() => {{
                    if (currentSlide < slides.length - 1) {{
                        nextSlide();
                    }} else {{
                        timerState = 'stopped';
                    }}
                }}, 50);
            }} else {{
                animationId = requestAnimationFrame(updateProgress);
            }}
        }}
        
        function nextSlide() {{
            if (currentSlide < slides.length - 1) {{
                currentSlide++;
                showSlide(currentSlide);
                
                // Check if it's time for a break (after showing the slide)
                if (BREAK_INTERVAL > 0 && currentSlide % BREAK_INTERVAL === 0 && currentSlide < slides.length - 1) {{
                    showBreakScreen();
                }}
            }}
        }}
        
        function prevSlide() {{
            if (currentSlide > 0) {{
                currentSlide--;
                showSlide(currentSlide);
            }}
        }}
        
        function manualNavigation() {{
            if (!gameStarted || onBreak) return;
            // Stop timer on manual navigation
            pauseTimer();
            const now = Date.now();
            if (startTime) {{
                pausedTime = now - startTime;
            }}
        }}
        
        // Show first slide on load
        window.addEventListener('load', () => {{
            console.log('Page loaded, found', slides.length, 'slides');
            
            // Make body focusable to receive keyboard events
            document.body.tabIndex = -1;
            document.body.focus();
            
            // Don't start game automatically - wait for user to click play
        }});
        
        // Add keyboard event listener (only one to avoid duplicates)
        document.addEventListener('keydown', (e) => {{
            console.log('Key pressed:', e.key);
            if (e.key === ' ') {{
                e.preventDefault();
                if (!gameStarted) {{
                    startGame();
                }} else if (onBreak) {{
                    hideBreakScreen();
                }} else {{
                    toggleTimer();
                }}
            }} else if (gameStarted && !onBreak) {{
                if (e.key === 'ArrowRight') {{
                    manualNavigation();
                    nextSlide();
                }} else if (e.key === 'ArrowLeft') {{
                    manualNavigation();
                    prevSlide();
                }}
            }}
        }});
        
        // Focus body when clicked to ensure keyboard events work
        document.addEventListener('click', (e) => {{
            document.body.focus();
            
            if (!gameStarted || onBreak) {{
                return; // Let play/continue button handle the click
            }}
            
            const x = e.clientX;
            const width = window.innerWidth;
            manualNavigation();
            if (x < width / 2) {{
                prevSlide();
            }} else {{
                nextSlide();
            }}
        }});
        
        // Play button click handler
        playButton.addEventListener('click', (e) => {{
            e.stopPropagation();
            startGame();
        }});
        
        // Continue button click handler
        continueButton.addEventListener('click', (e) => {{
            e.stopPropagation();
            hideBreakScreen();
        }});
        
        // Settings button click handler
        settingsButton.addEventListener('click', (e) => {{
            e.stopPropagation();
            toggleSettings();
        }});
        
        // Save button click handler
        saveButton.addEventListener('click', (e) => {{
            e.stopPropagation();
            saveSettings();
        }});
        
        // Prevent settings panel clicks from bubbling
        settingsPanel.addEventListener('click', (e) => {{
            e.stopPropagation();
        }});
    </script>
</body>
</html>
    """
    
    with open('presentation.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Generated presentation.html")

if __name__ == '__main__':
    generate_html() 