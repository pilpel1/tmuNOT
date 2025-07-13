import os
import random
import glob

# Configuration
SLIDE_DURATION = 4  # seconds per slide

def generate_html():
    # Get all images: jpg, jpeg, png
    image_dir = 'images'
    images = [os.path.join(image_dir, f).replace('\\', '/') for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)  # Randomize order
    print(f"Found {len(images)} images")
    
    slides = []
    for img in images:
        color = random.choice(['red', 'green'])
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
    </style>
  </head>
  <body>
      <div class="progress-container">
          <div class="progress-bar" id="progressBar"></div>
      </div>
      {''.join(slides)}
    
    <script>
        const SLIDE_DURATION = {int(SLIDE_DURATION * 1000)}; // milliseconds
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        const progressBar = document.getElementById('progressBar');
        
        // Timer state
        let timerState = 'running'; // 'running', 'paused', 'stopped'
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
            resetTimer();
        }}
        
        function resetTimer() {{
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
            }}
        }}
        
        function prevSlide() {{
            if (currentSlide > 0) {{
                currentSlide--;
                showSlide(currentSlide);
            }}
        }}
        
        function manualNavigation() {{
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
            
            if (slides.length > 0) {{
                showSlide(0);
            }}
        }});
        
        // Add keyboard event listener (only one to avoid duplicates)
        document.addEventListener('keydown', (e) => {{
            console.log('Key pressed:', e.key);
            if (e.key === 'ArrowRight') {{
                manualNavigation();
                nextSlide();
            }} else if (e.key === 'ArrowLeft') {{
                manualNavigation();
                prevSlide();
            }} else if (e.key === ' ') {{
                e.preventDefault();
                toggleTimer();
            }}
        }});
        
        // Focus body when clicked to ensure keyboard events work
        document.addEventListener('click', (e) => {{
            document.body.focus();
            const x = e.clientX;
            const width = window.innerWidth;
            manualNavigation();
            if (x < width / 2) {{
                prevSlide();
            }} else {{
                nextSlide();
            }}
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