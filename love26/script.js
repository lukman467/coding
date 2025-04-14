const bodyElement = document.body;
const canvasElement = document.getElementsByTagName('canvas')[0];
const ctx = canvasElement.getContext('2d');

window.requestAnimFrame = (function() {
    return window.requestAnimationFrame ||
           window.webkitRequestAnimationFrame ||
           function(callback) {
               window.setTimeout(callback, 1000 / 60);
           };
})();

let mouseX = 0;
let mouseY = 0;

bodyElement.addEventListener('mousemove', function(event) {
    mouseX = event.pageX;
    mouseY = event.pageY;
});

bodyElement.addEventListener('click', function(event) {
    particles.forEach(particle => {
        particle.x = mouseX;
        particle.y = mouseY;
    });
});

const canvasWidth = window.innerWidth;
const canvasHeight = window.innerHeight;
const particleSizeFactor = Math.floor((canvasWidth * canvasHeight) / 29000);
const numParticles = 900;
const particles = [];

canvasElement.width = canvasWidth;
canvasElement.height = canvasHeight;

function initializeParticles() {
    for (let i = 0; i < numParticles; i++) {
        const particle = {
            x: canvasWidth / 2,
            y: canvasHeight / 2,
            angleControlA: Math.random() * 100000,
            angleControlB: 0,
            previousHeartState: 0,
            opacity: 0.1,
        };
        particle.angleControlB = particle.angleControlA;
        particles.push(particle);
    }
}

let heartPixelData = null;

function captureHeartShape() {
    ctx.fillStyle = "rgba(0, 0, 0, 1)";
    ctx.font = (canvasWidth * 0.8) + "px sans-serif";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText('♥', canvasWidth / 2, canvasHeight / 2);

    try {
        heartPixelData = ctx.getImageData(0, 0, canvasWidth, canvasHeight).data;
    } catch (e) {
        console.error("Could not get image data:", e);
        return;
    }

    ctx.fillStyle = "rgba(0, 0, 0, 1)";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);
}

function render() {
    if (!heartPixelData) return;

    ctx.fillStyle = "rgba(0, 0, 0, 0.01)";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    particles.forEach(particle => {
        particle.angleControlA += Math.random() > 0.5 ? -1 : 1;
        particle.angleControlB -= (particle.angleControlB - particle.angleControlA) * 0.05;

        const angle = particle.angleControlB * 8;
        const radianAngle = angle * Math.PI / 180;
        particle.x += Math.cos(radianAngle);
        particle.y += Math.sin(radianAngle);

        const px = Math.floor(particle.x);
        const py = Math.floor(particle.y);

        let currentHeartValue = 0;
        if (px >= 0 && px < canvasWidth && py >= 0 && py < canvasHeight) {
            const pixelIndex = (px + (py * canvasWidth)) * 4;
            currentHeartValue = heartPixelData[pixelIndex + 3];
        }

        const isInHeart = currentHeartValue > 0;

        if ((isInHeart && !particle.previousHeartState) || (!isInHeart && particle.previousHeartState)) {
            particle.opacity = 0.05;
        }

        particle.previousHeartState = isInHeart;

        if (isInHeart) {
            particle.opacity += particle.opacity < 0.8 ? 0.03 : 0;
            ctx.fillStyle = `rgba(255, 0, 0, ${particle.opacity})`;
        } else {
            particle.opacity += particle.opacity < 0.3 ? 0.01 : 0;
            ctx.fillStyle = `rgba(255, 255, 255, ${particle.opacity})`;
        }

        const wrapBuffer = particleSizeFactor;
        if (particle.x > canvasWidth + wrapBuffer) particle.x = -wrapBuffer;
        if (particle.x < -wrapBuffer) particle.x = canvasWidth + wrapBuffer;
        if (particle.y > canvasHeight + wrapBuffer) particle.y = -wrapBuffer;
        if (particle.y < -wrapBuffer) particle.y = canvasHeight + wrapBuffer;

        const deltaX = particle.x - canvasWidth / 2;
        const deltaY = particle.y - canvasHeight / 2;
        const distance = Math.sqrt(deltaX * deltaX + deltaY * deltaY);
        const fontSizeBase = particleSizeFactor;
        const dynamicFontSize = (distance < fontSizeBase * (fontSizeBase / 4) ? Math.floor(distance / (fontSizeBase / 4)) || 1 : fontSizeBase);
        const finalFontSize = Math.max(1, dynamicFontSize);
        ctx.font = finalFontSize + 'px Arial';

        ctx.fillText('❤', Math.floor(particle.x), Math.floor(particle.y));
    });
}

(function animationLoop() {
    requestAnimFrame(animationLoop);
    render();
})();

initializeParticles();
captureHeartShape();