(function() {

  const canvasElement = document.getElementById("c");
  const ctx = canvasElement.getContext("2d");

  const canvasWidth = canvasElement.width = 500;
  const canvasHeight = canvasElement.height = 500;
  const centerX = canvasWidth / 2;
  const centerY = canvasHeight / 2;

  const degreesToRadians = Math.PI / 180;
  const particleCount = 500;

  const particleInstances = [];

  const colorPalette = ["217,65,65", "240,223,223", "255,161,161", "237,126,126", "240,96,137"];

  ctx.strokeStyle = "white";
  ctx.globalAlpha = 0.7;

  function getRandomInteger(min, max) {
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  class SparkleParticle {
    constructor() {
      this.radius = getRandomInteger(2, 12);

      const initialDist = Math.random() * 130 + 1;
      const initialAngle = Math.random() * 360;
      const angleInRadians = initialAngle * degreesToRadians;

      this.x = centerX + initialDist * Math.cos(angleInRadians);
      this.y = centerY + 25 + initialDist * Math.sin(angleInRadians);

      const speedFactor = Math.random();
      this.velocityX = speedFactor * (Math.random() < 0.5 ? -1 : 1);
      this.velocityY = speedFactor * (Math.random() < 0.5 ? -1 : 1);

      this.alpha = Math.random() * 0.8 + 0.1;
      const colorIndex = Math.floor(Math.random() * colorPalette.length);
      this.colorString = `rgba(${colorPalette[colorIndex]}, ${this.alpha})`;
    }

    move() {
        this.x += this.velocityX;
        this.y += this.velocityY;
    }

    reverseDirection() {
        this.velocityX *= -1;
        this.velocityY *= -1;
    }

    draw(context) {
        context.beginPath();
        context.arc(this.x, this.y, this.radius, 0, 2 * Math.PI);
        context.fillStyle = this.colorString;
        context.fill();
    }
  }

  for (let i = 0; i < particleCount; i++) {
    particleInstances.push(new SparkleParticle());
  }

  function defineHeartShape(particleRadius) {
    const heartSize = 100;
    const buffer = particleRadius;
    const effectiveRadius = heartSize - buffer;
    const safeRadius = Math.max(effectiveRadius, 1);

    const topCurveY = 200;
    const bottomPointY = 450;
    const leftCurveX = centerX - heartSize;
    const rightCurveX = centerX + heartSize;

    ctx.beginPath();
    ctx.moveTo(centerX, topCurveY);
    ctx.arc(rightCurveX, topCurveY, safeRadius, Math.PI, Math.PI * 0.23, false);
    ctx.lineTo(centerX, bottomPointY);
    ctx.arc(leftCurveX, topCurveY, safeRadius, Math.PI * 0.77, 0, false);
    ctx.closePath();
  }


  function renderAnimation() {
    ctx.fillStyle = "rgba(0, 0, 0, 0.1)";
    ctx.fillRect(0, 0, canvasWidth, canvasHeight);

    for (let i = 0; i < particleInstances.length; i++) {
      const particle = particleInstances[i];

      defineHeartShape(particle.radius);

      if (ctx.isPointInPath(particle.x, particle.y)) {
        particle.move();
        particle.draw(ctx);
      } else {
        particle.reverseDirection();
        particle.move();
      }
    }

    window.requestAnimationFrame(renderAnimation);
  }

  window.requestAnimationFrame(renderAnimation);

})();