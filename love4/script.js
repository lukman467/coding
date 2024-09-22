var settings = {
    particles: {
        length: 500, // Number of particles
        duration: 2, // Particle duration in seconds
        velocity: 100, // Particle velocity in pixels per second
        effect: -0.75, // Particle effect (0 = no effect, -1 = reverse, 1 = normal)
        size: 30, // Particle size in pixels
    },
};

(function(){var b=0;var c=["ms","moz","webkit","o"];for(var a=0;a<c.length&&!window.requestAnimationFrame;++a){window.requestAnimationFrame=window[c[a]+"RequestAnimationFrame"];window.cancelAnimationFrame=window[c[a]+"CancelAnimationFrame"]||window[c[a]+"CancelRequestAnimationFrame"]}if(!window.requestAnimationFrame){window.requestAnimationFrame=function(h,e){var d=new Date().getTime();var f=Math.max(0,16-(d-b));var g=window.setTimeout(function(){h(d+f)},f);b=d+f;return g}}if(!window.cancelAnimationFrame){window.cancelAnimationFrame=function(d){clearTimeout(d)}}}()); // Polyfill for requestAnimationFrame

var Point = (function() { // Point class
    function Point(x, y) { // Constructor
        this.x = (typeof x !== 'undefined') ? x : 0;
        this.y = (typeof y !== 'undefined') ? y : 0;
    }   
    Point.prototype.clone = function() { // Clone point
        return new Point(this.x, this.y);
    };
    Point.prototype.length = function(length) { // Get or set length
        if (typeof length == 'undefined')
        return Math.sqrt(this.x * this.x + this.y * this.y);
        this.normalize();
        this.x *= length;
        this.y *= length;
        return this;
    };
    Point.prototype.normalize = function() { // Normalize point
        var length = this.length();
        this.x /= length;
        this.y /= length;
        return this;
    };

    return Point;
})();

var Particle = (function() { // Particle class
    function Particle() {
        this.position = new Point();
        this.velocity = new Point();
        this.acceleration = new Point();
        this.age = 0;
    }
    Particle.prototype.initialize = function(x, y, dx, dy) { // Initialize particle
        this.position.x = x;
        this.position.y = y;
        this.velocity.x = dx;
        this.velocity.y = dy;
        this.acceleration.x = dx * settings.particles.effect;
        this.acceleration.y = dy * settings.particles.effect;
        this.age = 0;
    };
    Particle.prototype.update = function(deltaTime) { // Update particle
        this.position.x += this.velocity.x * deltaTime;
        this.position.y += this.velocity.y * deltaTime;
        this.velocity.x += this.acceleration.x * deltaTime;
        this.velocity.y += this.acceleration.y * deltaTime;
        this.age += deltaTime;
    };
    Particle.prototype.draw = function(context, image) { // Draw particle
        function ease(t) { // Ease function
        return (--t) * t * t + 1;
        }
        var size = image.width * ease(this.age / settings.particles.duration);
        context.globalAlpha = 1 - this.age / settings.particles.duration;
        context.drawImage(image, this.position.x - size / 2, this.position.y - size / 2, size, size);
    };

    return Particle;
})();

var ParticlePool = (function() { // Particle pool class
    var particles, firstActive = 0, firstFree = 0, duration = settings.particles.duration;

    function ParticlePool(length) { // Constructor
        particles = new Array(length);
        for (var i = 0; i < particles.length; i++)
        particles[i] = new Particle();
    }
    ParticlePool.prototype.add = function(x, y, dx, dy) { // Add particle
        particles[firstFree].initialize(x, y, dx, dy);
        firstFree++;

        if (firstFree == particles.length) { // Reset pool
            firstFree = 0;
        }
        if (firstActive == firstFree) { // Reset pool
            firstActive++;
        }
        if (firstActive == particles.length) { // Reset pool
            firstActive = 0;
        }
    };
    ParticlePool.prototype.update = function(deltaTime) { // Update particles
        var i;
        
        if (firstActive < firstFree) { // Update particles
            for (i = firstActive; i < firstFree; i++) { // Update particles
                particles[i].update(deltaTime);
            }
        }
        if (firstFree < firstActive) { // Update particles
            for (i = firstActive; i < particles.length; i++) { // Update particles
                particles[i].update(deltaTime);
            }
            for (i = 0; i < firstFree; i++) { // Update particles
                particles[i].update(deltaTime);
            }
        }
        while (particles[firstActive].age >= duration && firstActive != firstFree) { // Remove old particles
            firstActive++;
            if (firstActive == particles.length) { // Reset pool
                firstActive = 0;
            }
        }
    };
    ParticlePool.prototype.draw = function(context, image) { // Draw particles
        if (firstActive < firstFree) { // Draw particles
            for (i = firstActive; i < firstFree; i++) { // Draw particles
                particles[i].draw(context, image);
            }
        }
        if (firstFree < firstActive) { // Draw particles
            for (i = firstActive; i < particles.length; i++) { // Draw particles
                particles[i].draw(context, image);
            }
            for (i = 0; i < firstFree; i++) { // Draw particles
                particles[i].draw(context, image);
            }
        }
    };

    return ParticlePool;
})();

(function(canvas) { // Main function
    var context = canvas.getContext('2d'), particles = new ParticlePool(settings.particles.length), particleRate = settings.particles.length / settings.particles.duration, time;

    function pointOnHeart(t) { // Get point on heart
        return new Point(
            160 * Math.pow(Math.sin(t), 3),
            130 * Math.cos(t) - 50 * Math.cos(2 * t) - 20 * Math.cos(3 * t) - 10 * Math.cos(4 * t) + 25
        );
    }

    var image = (function() { // Create particle image
        var canvas  = document.createElement('canvas'), context = canvas.getContext('2d');
        canvas.width  = settings.particles.size;
        canvas.height = settings.particles.size;

        function to(t) { // Convert t to radians 
            var point = pointOnHeart(t);
            point.x = settings.particles.size / 2 + point.x * settings.particles.size / 350;
            point.y = settings.particles.size / 2 - point.y * settings.particles.size / 350;
        
            return point;
        }

        context.beginPath();
        var t = -Math.PI;
        var point = to(t);
        context.moveTo(point.x, point.y);

        while (t < Math.PI) { // Draw heart
            t += 0.01;
            point = to(t);
            context.lineTo(point.x, point.y);
        }

        context.closePath();
        context.fillStyle = '#ea80b0';
        context.fill();
        var image = new Image();
        image.src = canvas.toDataURL();

        return image;
    })();

    function render() { // Render function
        requestAnimationFrame(render);
        var newTime = new Date().getTime() / 1000, deltaTime = newTime - (time || newTime);
        time = newTime;
        context.clearRect(0, 0, canvas.width, canvas.height);
        var amount = particleRate * deltaTime;

        for (var i = 0; i < amount; i++) { // Add particles
            var pos = pointOnHeart(Math.PI - 2 * Math.PI * Math.random());
            var dir = pos.clone().length(settings.particles.velocity);
            particles.add(canvas.width / 2 + pos.x, canvas.height / 2 - pos.y, dir.x, -dir.y);
        }
        
        particles.update(deltaTime);
        particles.draw(context, image);
    }

    function onResize() { // Resize function
        canvas.width  = canvas.clientWidth;
        canvas.height = canvas.clientHeight;
    }

    window.onresize = onResize;
    
    setTimeout(function() { // Start
        onResize();
        render();
    }, 10);
})
(document.getElementById('pinkboard')); // Get canvas element