import os
import random
import glob

def generate_html():
    # Get all images: jpg, jpeg, png
    image_dir = 'images'
    images = [os.path.join(image_dir, f).replace('\\', '/') for f in os.listdir(image_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    images.sort()  # Sort alphabetically
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
<html lang="en">
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
    </style>
</head>
<body>
    {''.join(slides)}
    
    <script>
        let currentSlide = 0;
        const slides = document.querySelectorAll('.slide');
        
        function showSlide(n) {{
            console.log('Showing slide:', n, 'of', slides.length);
            slides.forEach((slide, index) => {{
                slide.classList.remove('active');
                if (index === n) {{
                    slide.classList.add('active');
                }}
            }});
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
                nextSlide();
            }} else if (e.key === 'ArrowLeft') {{
                prevSlide();
            }}
        }});
        
        // Focus body when clicked to ensure keyboard events work
        document.addEventListener('click', (e) => {{
            document.body.focus();
            const x = e.clientX;
            const width = window.innerWidth;
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