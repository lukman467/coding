import tkinter as tk
import math
import time
import random

LYRICS = [
    "But you should know that I die slow",
    "Running through the halls of your haunted home",
    "And the toughest part is that we both know",
    "What happened to you",
    "Why you're out on your own",
    "Merry Christmas, please don't call",
    "Merry Christmas, I'm not yours at all",
    "Merry Christmas, please don't call me",
]

DELAYS = [
    0.3,
    4.0,
    9.0,
    13.0,
    15.0,
    17.5,
    22.0,
    26.5,
]

X_POSITIONS = [
    400,
    800,
    430,
    800,
    450,
    700,
    350,
    800,
]

Y_POSITIONS = [
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
    1100,
]

KARAOKE_SPEEDS = [
    5,
    4,
    3,
    4,
    4,
    4,
    4,
    4,
]

BOX_COLORS = [
    "#FF6B6B",
    "#4ECDC4",
    "#0984E3",
    "#A29BFE",
    "#FD79A8",
    "#00CEC9",
    "#E17055",
    "#6C5CE7",
]

TRANSPARENT_COLOR = "#010101"

PARTICLE_COLORS = ["#FFB6C1", "#FFC0CB", "#DC143C", "#FFF0F5", "#FF69B4", "#FF1493", "#FF6B6B"]

def darken(hex_color, factor=0.4):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return f"#{int(r*factor):02x}{int(g*factor):02x}{int(b*factor):02x}"

class HeartParticle:
    _unit_pts = None

    def __init__(self, canvas, screen_w, screen_h):
        self.canvas = canvas
        self.screen_h = screen_h
        
        self.size = random.randint(10, 25)
        self.w = self.size
        self.h = self.size * 0.9
        
        self.x = random.randint(0, screen_w)
        self.y = float(screen_h + 20)
        
        self.dy = random.uniform(1.5, 4.0)
        self.dx = random.uniform(-1.0, 1.0)
        
        self.color = random.choice(PARTICLE_COLORS)
        self.gone = False
        
        if HeartParticle._unit_pts is None:
            HeartParticle._unit_pts = self._gen_heart_points()
            
        self.poly = self._draw_heart(self.x, self.y, fill=self.color, outline="")
        self.canvas.tag_lower(self.poly)

    def _gen_heart_points(self):
        pts = []
        for i in range(20):
            t = 2 * math.pi * i / 20
            x = 16 * math.sin(t) ** 3
            y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            pts.append((x / 17.0, y / 17.0))
        return pts

    def _draw_heart(self, ox, oy, **kwargs):
        cx = ox + self.w / 2
        cy = oy + self.h / 2
        sx = self.w / 2
        sy = self.h / 2
        flat = []
        for (hx, hy) in self._unit_pts:
            flat.append(cx + hx * sx)
            flat.append(cy + hy * sy)
        return self.canvas.create_polygon(flat, smooth=True, **kwargs)

    def update(self):
        if self.gone: return
        
        ax = random.uniform(-0.1, 0.1)
        self.dx += ax
        self.dx = max(-1.5, min(1.5, self.dx))
        
        self.x += self.dx
        self.y -= self.dy
        
        self.canvas.move(self.poly, self.dx, -self.dy)
        
        if self.y + self.h < -10:
            self.gone = True
            self.canvas.delete(self.poly)

class FloatingHeart:
    HEART_POINTS = 80
    UNIFORM_W = 400
    UNIFORM_H = 360

    def __init__(self, canvas, text, color, screen_w, screen_h, manual_x=None, manual_y=None, type_speed=5):
        self.canvas = canvas
        self.color = color
        self.gone = False
        self.screen_h = screen_h

        self.font = ("Segoe UI", 18, "bold")
        self.full_text = text
        self.shown_chars = 0
        self.char_timer = 0
        self.char_interval = type_speed
        self.karaoke_started = False

        self.heart_w = self.UNIFORM_W
        self.heart_h = self.UNIFORM_H

        if manual_x is not None:
            self.x = manual_x
        else:
            self.x = (screen_w - self.heart_w) / 2
            
        if manual_y is not None:
            self.y = float(manual_y)
        else:
            self.y = float(screen_h + 20)
            
        self.speed = 3.0
        self.text_offset_y = self.heart_h * 0.03
        self._unit_pts = self._gen_heart_points()

        self.shadow = self._draw_heart(
            self.x + 5, self.y + 5, fill=darken(color, 0.3), outline=""
        )
        self.rect = self._draw_heart(
            self.x, self.y, fill=color, outline=""
        )
        self.label = canvas.create_text(
            self.x + self.heart_w / 2,
            self.y + self.heart_h / 2 + self.text_offset_y,
            text="", font=self.font, fill="#FFFFFF", anchor="center",
            justify="center",
            width=self.heart_w * 0.55,
        )

    def _gen_heart_points(self):
        pts = []
        for i in range(self.HEART_POINTS):
            t = 2 * math.pi * i / self.HEART_POINTS
            x = 16 * math.sin(t) ** 3
            y = -(13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            pts.append((x / 17.0, y / 17.0))
        return pts

    def _draw_heart(self, ox, oy, **kwargs):
        cx = ox + self.heart_w / 2
        cy = oy + self.heart_h / 2
        sx = self.heart_w / 2
        sy = self.heart_h / 2
        flat = []
        for (hx, hy) in self._unit_pts:
            flat.append(cx + hx * sx)
            flat.append(cy + hy * sy)
        return self.canvas.create_polygon(flat, smooth=True, **kwargs)

    def _move_all(self):
        self.canvas.delete(self.shadow)
        self.canvas.delete(self.rect)

        self.shadow = self._draw_heart(
            self.x + 5, self.y + 5, fill=darken(self.color, 0.3), outline=""
        )
        self.rect = self._draw_heart(
            self.x, self.y, fill=self.color, outline=""
        )
        self.canvas.itemconfigure(
            self.label, text=self.full_text[:self.shown_chars]
        )
        self.canvas.tag_raise(self.label)
        self.canvas.coords(
            self.label,
            self.x + self.heart_w / 2,
            self.y + self.heart_h / 2 + self.text_offset_y,
        )

    def update(self):
        if self.gone:
            return

        if not self.karaoke_started:
            if self.y < self.screen_h - self.heart_h * 0.3:
                self.karaoke_started = True

        if self.karaoke_started and self.shown_chars < len(self.full_text):
            self.char_timer += 1
            if self.char_timer >= self.char_interval:
                self.char_timer = 0
                self.shown_chars += 1

        self.y -= self.speed
        if self.y + self.heart_h < -10:
            self.gone = True
            self.canvas.delete(self.shadow)
            self.canvas.delete(self.rect)
            self.canvas.delete(self.label)
            return
        self._move_all()


class FloatingLyricsOverlay:
    FPS = 60

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Apocalypse Lyrics")

        self.root.overrideredirect(True)
        self.root.wm_attributes('-topmost', True)
        self.root.wm_attributes('-transparentcolor', TRANSPARENT_COLOR)

        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry(f"{sw}x{sh}+0+0")

        self.canvas = tk.Canvas(
            self.root, width=sw, height=sh,
            bg=TRANSPARENT_COLOR, highlightthickness=0
        )
        self.canvas.pack()

        self.sw = sw
        self.sh = sh
        self.boxes = []
        self.particles = []
        self.spawned = [False] * len(LYRICS)
        self.start_time = time.time()

        self.root.bind('<Escape>', lambda e: self.root.destroy())

        self._animate()
        self.root.mainloop()

    def _animate(self):
        elapsed = time.time() - self.start_time

        for i in range(len(LYRICS)):
            if not self.spawned[i] and elapsed >= DELAYS[i]:
                manual_x = X_POSITIONS[i] if i < len(X_POSITIONS) else None
                manual_y = Y_POSITIONS[i] if i < len(Y_POSITIONS) else None
                t_speed = KARAOKE_SPEEDS[i] if i < len(KARAOKE_SPEEDS) else 5
                
                box = FloatingHeart(
                    self.canvas, LYRICS[i], BOX_COLORS[i % len(BOX_COLORS)],
                    self.sw, self.sh, manual_x, manual_y, t_speed
                )
                self.boxes.append(box)
                self.spawned[i] = True

        if random.random() < 0.15 and len(self.particles) < 60:
            self.particles.append(HeartParticle(self.canvas, self.sw, self.sh))

        for box in self.boxes:
            box.update()
            
        for p in self.particles:
            p.update()
        self.particles = [p for p in self.particles if not p.gone]

        if all(self.spawned) and all(b.gone for b in self.boxes):
            self.root.destroy()
            return

        self.root.after(1000 // self.FPS, self._animate)


if __name__ == "__main__":
    FloatingLyricsOverlay()
