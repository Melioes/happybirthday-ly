import re

with open('D:/happybirthday/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Video Tags for 100% mobile compatibility
html = re.sub(
    r'<video id=\"hero-video\"[^>]*>',
    '<video id=\"hero-video\" class=\"section-video\" preload=\"auto\" autoplay loop muted playsinline=\"true\" webkit-playsinline=\"true\" x5-playsinline=\"true\" x5-video-player-type=\"h5-page\" x5-video-player-fullscreen=\"true\">',
    html
)
html = re.sub(
    r'<video class=\"section-video story-video\"[^>]*>',
    '<video class=\"section-video story-video\" preload=\"auto\" autoplay loop muted playsinline=\"true\" webkit-playsinline=\"true\" x5-playsinline=\"true\" x5-video-player-type=\"h5-page\" x5-video-player-fullscreen=\"true\">',
    html
)
html = re.sub(
    r'<video class=\"finale-video\"[^>]*>',
    '<video class=\"finale-video\" preload=\"auto\" autoplay loop muted playsinline=\"true\" webkit-playsinline=\"true\" x5-playsinline=\"true\" x5-video-player-type=\"h5-page\" x5-video-player-fullscreen=\"true\">',
    html
)

# 2. Update style block: add pop-char 3D styling and mobile-friendly hero tint
new_styles = '''
        /* 3D 梦幻高质感文字特效 */
        .pop-char {
            display: inline-block;
            color: #fffcee;
            text-shadow: 
                0 1px 0 #ffd166,
                0 2px 0 #f4a261,
                0 3px 0 #e76f51,
                0 4px 0 #d64045,
                0 5px 12px rgba(0, 0, 0, 0.7),
                0 0 20px rgba(255, 215, 0, 0.9),
                0 0 45px rgba(255, 107, 129, 0.6);
            transform-origin: center bottom;
        }
        .bless-char {
            display: inline-block;
            transform-origin: center bottom;
        }
        .hero-section .video-shade {
            background: radial-gradient(circle at 50% 50%, rgba(0, 220, 130, 0.22) 0%, rgba(2, 6, 23, 0.75) 100%) !important;
        }
'''
if '.pop-char {' not in html:
    html = html.replace('</style>', new_styles + '\n    </style>')

# 3. Replace #cake-blessing block with new structure
new_blessing = '''        <div id="cake-blessing" style="position: absolute; top: 8%; left: 0; width: 100%; text-align: center; z-index: 30; pointer-events: none; padding: 0 10px; opacity: 0; transition: opacity 0.5s ease;">
            <div class="pop-title" style="font-family: 'Fredoka One', 'Arial Black', sans-serif; font-size: clamp(2.4rem, 8vw, 4.5rem); font-weight: 900; line-height: 1.15;">
                <div class="pop-word" style="display: inline-block; margin-right: 12px;">HAPPY</div>
                <div class="pop-word" style="display: inline-block;">BIRTHDAY</div>
            </div>
            <div class="pop-blessing" style="font-size: clamp(1.2rem, 3.8vw, 1.8rem); color: #ffffff; font-weight: 600; letter-spacing: 3px; margin-top: 14px; text-shadow: 0 0 10px #00e5ff, 0 0 25px rgba(0, 229, 255, 0.7);">
                岁岁常欢愉 ✨
            </div>
            <div class="pop-recipient" style="font-size: clamp(1.1rem, 3.2vw, 1.5rem); color: #00f5d4; font-weight: 700; letter-spacing: 2px; margin-top: 10px; text-shadow: 0 0 15px rgba(0, 245, 212, 0.8);">
                To: 梁研 🎂
            </div>
        </div>'''

html = re.sub(r'<div id=\"cake-blessing\".*?</div>\s*</div>', new_blessing, html, flags=re.DOTALL)

# 4. Update the entire script block with proper mobile video handling, centered cake coordinates, and 3D popping text
script_pattern = r'<script>.*?</script>'
new_script = '''<script>
    // 1. 全局移动端视频强制播放保障
    function playAllVideos() {
        document.querySelectorAll('video').forEach(v => {
            v.muted = true;
            v.setAttribute('muted', '');
            v.setAttribute('playsinline', 'true');
            v.setAttribute('webkit-playsinline', 'true');
            v.setAttribute('x5-playsinline', 'true');
            v.setAttribute('x5-video-player-type', 'h5-page');
            const p = v.play();
            if (p && p.catch) p.catch(() => {});
        });
    }
    document.addEventListener('DOMContentLoaded', playAllVideos);
    window.addEventListener('load', playAllVideos);
    ['touchstart', 'click', 'scroll'].forEach(evt => {
        window.addEventListener(evt, playAllVideos, { once: true, passive: true });
    });
    document.addEventListener('WeixinJSBridgeReady', playAllVideos, false);

    // 2. 滚动 reveal
    const observer = new IntersectionObserver((e) => { 
        e.forEach(en => { if(en.isIntersecting) en.target.classList.add('revealed'); }); 
    }, { threshold: 0.15 });
    document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

    // 3. 召唤蛋糕交互与 3D 逐字蹦出动效
    const summonBtn = document.getElementById('summon-cake-btn');
    const cakeContainer = document.getElementById('cake-canvas-container');
    const balloonContainer = document.getElementById('balloon-container');
    const cakeBlessing = document.getElementById('cake-blessing');
    let cakeInitialized = false;

    summonBtn.addEventListener('click', () => {
        gsap.to(document.getElementById('finale-text'), { 
            opacity: 0, 
            duration: 0.8, 
            onComplete: () => document.getElementById('finale-text').style.display = 'none' 
        });

        // 升起气球
        createBalloons();

        // 启动 3D 逐字蹦出文字特效
        trigger3DPoppingText();

        // 加载 3D 粒子蛋糕并从底部升起旋转
        setTimeout(() => {
            cakeContainer.classList.add('active');
            if(!cakeInitialized) { 
                initParticleCake(); 
                cakeInitialized = true; 
            }
        }, 300);
    });

    function trigger3DPoppingText() {
        cakeBlessing.style.opacity = '1';
        
        // 分割 HAPPY BIRTHDAY
        document.querySelectorAll('.pop-word').forEach(word => {
            const letters = word.innerText.split('');
            word.innerHTML = '';
            letters.forEach(l => {
                const s = document.createElement('span');
                s.className = 'pop-char';
                s.innerText = l;
                word.appendChild(s);
            });
        });

        // 分割祝福语
        const blessEl = document.querySelector('.pop-blessing');
        const blessText = blessEl.innerText.split('');
        blessEl.innerHTML = '';
        blessText.forEach(c => {
            const s = document.createElement('span');
            s.className = 'bless-char';
            s.innerText = c;
            blessEl.appendChild(s);
        });

        // 1. HAPPY BIRTHDAY 3D 翻转弹跳蹦出
        gsap.fromTo('.pop-char', 
            { scale: 0, rotationY: -110, rotationX: 45, y: -40, opacity: 0 },
            { scale: 1, rotationY: 0, rotationX: 0, y: 0, opacity: 1, duration: 0.6, stagger: 0.06, ease: "back.out(2.5)", delay: 0.4 }
        );

        // 2. 祝福文字逐字弹跳蹦出
        gsap.fromTo('.bless-char', 
            { scale: 0, y: 20, opacity: 0 },
            { scale: 1, y: 0, opacity: 1, duration: 0.5, stagger: 0.05, ease: "back.out(2.2)", delay: 1.4 }
        );

        // 3. 寿星名字高光浮现
        gsap.fromTo('.pop-recipient', 
            { scale: 0.4, y: 20, opacity: 0 },
            { scale: 1, y: 0, opacity: 1, duration: 0.8, ease: "elastic.out(1, 0.5)", delay: 2.1 }
        );
    }

    function createBalloons() {
        const colors = [
            { bg: 'radial-gradient(circle at 30% 30%, #fff, #ff6b81)', tip: '#ff6b81' },
            { bg: 'radial-gradient(circle at 30% 30%, #fff, #00e5ff)', tip: '#00e5ff' },
            { bg: 'radial-gradient(circle at 30% 30%, #fff, #f7d070)', tip: '#f7d070' },
            { bg: 'radial-gradient(circle at 30% 30%, #fff, #a29bfe)', tip: '#a29bfe' }
        ];
        
        for(let i=0; i<25; i++) {
            const b = document.createElement('div');
            b.className = 'balloon';
            const c = colors[Math.floor(Math.random() * colors.length)];
            b.style.background = c.bg;
            b.style.left = (Math.random() * 88 + 6) + '%';
            
            const startY = window.innerHeight + 100 + Math.random() * 150;
            const endY = -280 - Math.random() * 200;
            const duration = 4.5 + Math.random() * 3.5;
            
            balloonContainer.appendChild(b);
            
            gsap.fromTo(b, 
                { y: startY, x: 0 }, 
                { y: endY, x: (Math.random()-0.5)*180, duration: duration, ease: "power1.inOut", 
                  onComplete: () => b.remove() }
            );
        }
    }

    function initParticleCake() {
        const scene = new THREE.Scene();
        const isMobile = window.innerWidth < 768;
        
        // 手机端拉远相机距离，确保蛋糕整体完全居中可见
        const camZ = isMobile ? 27 : 21;
        const camera = new THREE.PerspectiveCamera(45, window.innerWidth / window.innerHeight, 0.1, 100);
        camera.position.set(0, 3.5, camZ);
        camera.lookAt(0, 0.2, 0);

        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
        renderer.setSize(window.innerWidth, window.innerHeight);
        renderer.setClearColor(0x000000, 0); 
        cakeContainer.appendChild(renderer.domElement);

        const cakeGroup = new THREE.Group();
        scene.add(cakeGroup);
        
        // 蛋糕从屏幕下方深处以 3D 旋转姿态升上正中央
        cakeGroup.position.set(0, -14, 0);
        gsap.to(cakeGroup.position, { y: -0.8, duration: 3.2, ease: "back.out(1.15)" });
        gsap.fromTo(cakeGroup.rotation, { y: -Math.PI * 0.8 }, { y: 0, duration: 3.2, ease: "power2.out" });

        // 3D 粒子蛋糕生成（以 y=0 为垂直几何中心，确保不被切底）
        const particleCount = 15000;
        const geometry = new THREE.BufferGeometry();
        const positions = new Float32Array(particleCount * 3);
        const colors = new Float32Array(particleCount * 3);
        
        const colorCyan = new THREE.Color(0x00e5ff);
        const colorGold = new THREE.Color(0xf7d070);
        const colorPink = new THREE.Color(0xff6b81);

        for (let i = 0; i < particleCount; i++) {
            const tier = Math.random();
            let r, y, h;
            if (tier < 0.5) { 
                // 底层基座：y 从 -2.6 到 -0.6
                h = 2.0; r = 4.8; y = -2.6 + Math.random() * h;
            } else if (tier < 0.8) { 
                // 中层蛋糕：y 从 -0.6 到 +1.2
                h = 1.8; r = 3.4; y = -0.6 + Math.random() * h;
            } else { 
                // 顶层蛋糕：y 从 +1.2 到 +2.6
                h = 1.4; r = 2.1; y = 1.2 + Math.random() * h;
            }
            
            const theta = Math.random() * Math.PI * 2;
            const radius = Math.random() > 0.15 ? r : r * Math.sqrt(Math.random());
            
            positions[i * 3] = Math.cos(theta) * radius;
            positions[i * 3 + 1] = y;
            positions[i * 3 + 2] = Math.sin(theta) * radius;
            
            const mixColor = [colorCyan, colorGold, colorPink][Math.floor(Math.random() * 3)];
            colors[i * 3] = mixColor.r;
            colors[i * 3 + 1] = mixColor.g;
            colors[i * 3 + 2] = mixColor.b;
        }
        
        geometry.setAttribute('position', new THREE.BufferAttribute(positions, 3));
        geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));

        // 粒子发光贴图
        const pCanvas = document.createElement('canvas');
        pCanvas.width = 32; pCanvas.height = 32;
        const ctx = pCanvas.getContext('2d');
        const grad = ctx.createRadialGradient(16, 16, 0, 16, 16, 16);
        grad.addColorStop(0, 'rgba(255,255,255,1)');
        grad.addColorStop(0.25, 'rgba(255,255,255,0.85)');
        grad.addColorStop(1, 'rgba(255,255,255,0)');
        ctx.fillStyle = grad; ctx.fillRect(0,0,32,32);
        const particleTexture = new THREE.CanvasTexture(pCanvas);

        const material = new THREE.PointsMaterial({
            size: isMobile ? 0.22 : 0.18,
            map: particleTexture,
            vertexColors: true,
            transparent: true,
            opacity: 0.85,
            blending: THREE.AdditiveBlending,
            depthWrite: false
        });

        const particles = new THREE.Points(geometry, material);
        cakeGroup.add(particles);

        // 顶层蜡烛与烛光火焰
        const flames = [], flameLights = [];
        for(let i=0; i<5; i++) {
            const angle = (i / 5) * Math.PI * 2;
            const cx = Math.cos(angle) * 1.3;
            const cz = Math.sin(angle) * 1.3;
            
            const glow = new THREE.Sprite(new THREE.SpriteMaterial({ 
                map: particleTexture, 
                color: 0xffaa00, 
                transparent: true, 
                blending: THREE.AdditiveBlending 
            }));
            glow.position.set(cx, 3.4, cz);
            glow.scale.set(1.8, 1.8, 1.8);
            cakeGroup.add(glow); 
            flames.push(glow);

            const light = new THREE.PointLight(0xffaa00, 2, 8);
            light.position.set(cx, 3.4, cz);
            cakeGroup.add(light); 
            flameLights.push(light);
        }

        // 初始粒子聚合入场动画
        const positionsAttr = geometry.attributes.position;
        const targetPositions = new Float32Array(positionsAttr.array);
        
        for(let i=0; i<particleCount*3; i++) {
            positionsAttr.array[i] += (Math.random() - 0.5) * 18;
        }
        
        gsap.to(positionsAttr.array, {
            endArray: targetPositions,
            duration: 2.8,
            ease: "power2.out",
            onUpdate: () => positionsAttr.needsUpdate = true,
            onComplete: () => {
                cakeContainer.addEventListener('click', blowCandles);
            }
        });

        let isBlown = false;
        function blowCandles() {
            if(isBlown) return;
            isBlown = true;
            
            flames.forEach((f, i) => {
                setTimeout(() => {
                    gsap.to(f.scale, { x: 0, y: 0, z: 0, duration: 0.3 });
                    gsap.to(flameLights[i], { intensity: 0, duration: 0.3 });
                    if(i === flames.length - 1) {
                        celebrateFireworks();
                    }
                }, i * 140);
            });
        }

        function celebrateFireworks() {
            const end = Date.now() + 5000;
            (function frame() {
                confetti({ particleCount: 8, angle: 60, spread: 80, origin: { x: 0, y: 0.7 }, colors: ['#00e5ff', '#f7d070', '#ffffff', '#ff6b81'] });
                confetti({ particleCount: 8, angle: 120, spread: 80, origin: { x: 1, y: 0.7 }, colors: ['#00e5ff', '#f7d070', '#ffffff', '#ff6b81'] });
                if (Date.now() < end) requestAnimationFrame(frame);
            }());
        }

        const clock = new THREE.Clock();
        function animate() {
            requestAnimationFrame(animate);
            const time = clock.getElapsedTime();
            cakeGroup.rotation.y = time * 0.15;
            
            // 粒子呼吸光效
            material.size = (isMobile ? 0.22 : 0.18) + Math.sin(time * 2.5) * 0.03;

            if(!isBlown) {
                flames.forEach((f, i) => {
                    const flicker = Math.sin(time * 16 + i) * 0.1;
                    f.scale.set(1.8 + flicker, 2.2 + flicker*2, 1.8 + flicker);
                });
            }
            renderer.render(scene, camera);
        }
        animate();

        window.addEventListener('resize', () => {
            const newIsMobile = window.innerWidth < 768;
            camera.aspect = window.innerWidth / window.innerHeight;
            camera.position.z = newIsMobile ? 27 : 21;
            camera.updateProjectionMatrix();
            renderer.setSize(window.innerWidth, window.innerHeight);
        });
    }
</script>'''

html = re.sub(script_pattern, new_script, html, flags=re.DOTALL)

with open('D:/happybirthday/index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Successfully rewritten index.html')
