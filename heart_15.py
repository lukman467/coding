from __future__ import annotations

import math
import random
import sys
from dataclasses import dataclass
import pygame


@dataclass(frozen=True)
class Config:
    width: int = 1900
    height: int = 1000
    fps: int = 120
    bg_color: tuple[int, int, int] = (15, 0, 0)
    caption: str = "I love you <3"

    scale: int = 20
    y_offset: int = -45

    n_outline: int = 160
    n_fill: int = 130
    n_floating: int = 1000

    outline_gap: int = 22
    fill_gap: int = 30

    frames_per_step: float = 0.5
    fill_delay_offset: int = 10
    center_delay: int = 40
    fade_speed_min: int = 25
    fade_speed_rand: int = 10

    heart_words: tuple[str, ...] = ("i love you", "I LOVE YOU", "love you")
    center_text: str = " I Love you"
    float_words: tuple[str, ...] = ("love", "♥", "love you", "❤")

    colors: tuple[tuple[int, int, int], ...] = (
        (255, 20, 20),
        (220, 20, 60),
        (255, 0, 0),
        (178, 34, 34),
        (255, 60, 60),
    )

    @property
    def center(self) -> tuple[float, float]:
        return self.width / 2, self.height / 2


CFG = Config()


def heart_parametric(t: float) -> tuple[float, float]:
    x = 16.0 * math.sin(t) ** 3
    y = 13.0 * math.cos(t) - 5.0 * math.cos(2 * t) - 2.0 * math.cos(3 * t) - math.cos(4 * t)
    return x, -y


def heart_to_screen(hx: float, hy: float) -> tuple[float, float]:
    sx = hx * CFG.scale + CFG.center[0]
    sy = hy * CFG.scale + CFG.center[1] + CFG.y_offset
    return sx, sy


class HeartParticle:
    __slots__ = (
        "x", "y", "order", "kind", "word", "color",
        "alpha", "flicker", "font", "delay", "size_mult",
    )

    def __init__(self, x: float, y: float, order: int, kind: str) -> None:
        self.x = x
        self.y = y
        self.order = order
        self.kind = kind
        self.word: str = random.choice(CFG.heart_words)
        self.color = random.choice(CFG.colors)
        self.alpha = 0
        self.flicker = random.uniform(0, math.tau)
        self.font: pygame.font.Font | None = None
        self.delay = 0
        self.size_mult = random.uniform(0.85, 1.15)


class FloatingParticle:
    __slots__ = (
        "x", "y", "word", "color", "size",
        "alpha", "max_alpha", "vx", "vy",
        "sway_speed", "sway_amount", "phase",
        "fading_in", "life", "max_life",
    )

    def __init__(self) -> None:
        self._randomize(scatter_y=True)

    def _randomize(self, scatter_y: bool = False) -> None:
        self.x = random.uniform(50, CFG.width - 50)
        self.y = random.uniform(0, CFG.height) if scatter_y else CFG.height + random.uniform(20, 100)
        self.word = random.choice(CFG.float_words)
        self.color = random.choice(CFG.colors)
        self.size = random.randint(10, 18)
        self.alpha = 0
        self.max_alpha = random.randint(40, 120)
        self.vx = random.uniform(-0.3, 0.3)
        self.vy = random.uniform(-0.4, -1.2)
        self.sway_speed = random.uniform(0.01, 0.04)
        self.sway_amount = random.uniform(0.3, 1.0)
        self.phase = random.uniform(0, math.tau)
        self.fading_in = True
        self.life = 0
        self.max_life = random.randint(300, 700)

    def update(self, frame: int) -> None:
        self.life += 1
        self.x += self.vx + math.sin(frame * self.sway_speed + self.phase) * self.sway_amount
        self.y += self.vy

        if self.fading_in:
            self.alpha = min(self.max_alpha, self.alpha + 3)
            if self.alpha >= self.max_alpha:
                self.fading_in = False

        if self.life > self.max_life - 60:
            self.alpha = max(0, self.alpha - 3)

        off_screen = self.y < -50 or self.x < -50 or self.x > CFG.width + 50
        if off_screen or (self.alpha <= 0 and self.life > 60):
            self._randomize(scatter_y=False)


def _too_close(sx: float, sy: float, placed: list[tuple[float, float]], gap: float) -> bool:
    return any(math.hypot(sx - px, sy - py) < gap for px, py in placed)


def generate_outline(n: int = CFG.n_outline, gap: int = CFG.outline_gap) -> list[HeartParticle]:
    particles: list[HeartParticle] = []
    placed: list[tuple[float, float]] = []

    for i in range(n):
        t = (i / n) * math.tau
        sx, sy = heart_to_screen(*heart_parametric(t))
        if _too_close(sx, sy, placed, gap):
            continue
        placed.append((sx, sy))
        particles.append(HeartParticle(sx, sy, order=i, kind="outline"))

    return particles


def generate_fill(n: int = CFG.n_fill, gap: int = CFG.fill_gap) -> list[HeartParticle]:
    particles: list[HeartParticle] = []
    placed: list[tuple[float, float]] = []
    max_attempts = n * 80

    for _ in range(max_attempts):
        if len(particles) >= n:
            break
        t = random.uniform(0, math.tau)
        r = random.uniform(0.0, 0.86)
        hx, hy = heart_parametric(t)
        sx, sy = heart_to_screen(hx * r, hy * r)

        if _too_close(sx, sy, placed, gap):
            continue

        placed.append((sx, sy))
        particles.append(HeartParticle(sx, sy, order=random.randint(0, 50), kind="fill"))

    return particles


class Renderer:
    def __init__(self) -> None:
        self.glow_layer = pygame.Surface((CFG.width, CFG.height), pygame.SRCALPHA)
        self.text_layer = pygame.Surface((CFG.width, CFG.height), pygame.SRCALPHA)

    @staticmethod
    def _render_text(font: pygame.font.Font, word: str, color: tuple, size_mult: float) -> pygame.Surface:
        if size_mult != 1.0:
            scaled = pygame.font.Font(None, int(font.get_height() * size_mult))
            return scaled.render(word, True, color)
        return font.render(word, True, color)

    def draw_glow_text(
        self, font: pygame.font.Font, word: str, color: tuple,
        x: float, y: float, alpha: int, size_mult: float = 1.0,
    ) -> None:
        if alpha <= 0:
            return

        txt = self._render_text(font, word, color, size_mult)
        txt.set_alpha(alpha)
        center = (x, y)

        if alpha > 10:
            for scale_factor, divisor in ((2.4, 7), (1.6, 3)):
                glow = pygame.transform.smoothscale(
                    txt,
                    (int(txt.get_width() * scale_factor), int(txt.get_height() * scale_factor)),
                )
                glow.set_alpha(max(0, alpha // divisor))
                self.glow_layer.blit(glow, glow.get_rect(center=center))

        self.text_layer.blit(txt, txt.get_rect(center=center))

    def begin_frame(self) -> None:
        self.glow_layer.fill((0, 0, 0, 0))
        self.text_layer.fill((0, 0, 0, 0))

    def composite(self, target: pygame.Surface) -> None:
        target.blit(self.glow_layer, (0, 0))
        target.blit(self.text_layer, (0, 0))


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((CFG.width, CFG.height), pygame.DOUBLEBUF)
    pygame.display.set_caption(CFG.caption)
    clock = pygame.time.Clock()

    font_outline = pygame.font.SysFont("arial", 20, bold=True)
    font_fill = pygame.font.SysFont("arial", 17, bold=True)
    font_center = pygame.font.SysFont("georgia", 54, bold=True)
    float_fonts = {sz: pygame.font.SysFont("arial", sz) for sz in range(10, 19)}

    background = pygame.Surface((CFG.width, CFG.height))
    background.fill(CFG.bg_color)

    outline = generate_outline()
    fill = generate_fill()

    outline_span = max(p.order for p in outline) if outline else 0
    fill_start = int(outline_span * CFG.frames_per_step) + CFG.fill_delay_offset
    center_start = fill_start + CFG.center_delay

    for p in outline:
        p.delay = int(p.order * CFG.frames_per_step)
        p.font = font_outline

    for p in fill:
        p.delay = fill_start + p.order
        p.font = font_fill

    heart_particles = outline + fill
    floating = [FloatingParticle() for _ in range(CFG.n_floating)]
    renderer = Renderer()

    frame = 0
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        frame += 1
        screen.blit(background, (0, 0))
        renderer.begin_frame()

        for fp in floating:
            fp.update(frame)
            if fp.alpha > 0:
                surf = float_fonts[fp.size].render(fp.word, True, fp.color)
                surf.set_alpha(fp.alpha)
                renderer.text_layer.blit(surf, surf.get_rect(center=(fp.x, fp.y)))

        for p in heart_particles:
            if frame > p.delay and p.alpha < 255:
                p.alpha = min(255, p.alpha + CFG.fade_speed_min + random.randint(0, CFG.fade_speed_rand))

            flicker = 0.75 + 0.25 * math.sin(frame * 0.04 + p.flicker) if p.alpha >= 255 else 1.0
            alpha = int(p.alpha * flicker)

            if alpha > 0:
                renderer.draw_glow_text(p.font, p.word, p.color, p.x, p.y, alpha, p.size_mult)

        renderer.composite(screen)

        if frame > center_start:
            progress = min(1.0, (frame - center_start) / 30.0)
            center_alpha = int(255 * (1 - math.exp(-progress * 8)))
            pulse = 1.0 + 0.025 * math.sin(frame * 0.05)

            center_surf = font_center.render(CFG.center_text, True, (255, 200, 200))
            w = int(center_surf.get_width() * pulse)
            h = int(center_surf.get_height() * pulse)

            if w > 0 and h > 0:
                center_surf = pygame.transform.smoothscale(center_surf, (w, h))

            center_surf.set_alpha(center_alpha)

            if center_alpha > 10:
                glow = pygame.transform.smoothscale(
                    center_surf,
                    (int(center_surf.get_width() * 1.4), int(center_surf.get_height() * 1.4)),
                )
                glow.set_alpha(center_alpha // 5)
                screen.blit(glow, glow.get_rect(center=CFG.center))

            screen.blit(center_surf, center_surf.get_rect(center=CFG.center))

        pygame.display.flip()
        clock.tick(CFG.fps)

    pygame.quit()


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        import traceback
        traceback.print_exc()
        sys.exit(1)