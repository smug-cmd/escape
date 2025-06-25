import pygame
import sys

def load_task():
    try:
        with open("task.txt", "r", encoding="utf-8") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "No task set."

def main():
    pygame.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Daily Task")
    
    # Load font (optional: use a pixel or matrix font for more hacker effect)
    font = pygame.font.SysFont("Consolas", 48)
    big_font = pygame.font.SysFont("Consolas", 72, bold=True)
    GREEN = (0, 255, 0)
    BLACK = (0, 0, 0)

    task_text = load_task()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        screen.fill(BLACK)
        title = big_font.render("Today's Task:", True, GREEN)
        task_lines = task_text.split("\n")
        screen.blit(title, (100, 100))
        
        for i, line in enumerate(task_lines):
            text_surface = font.render(line, True, GREEN)
            screen.blit(text_surface, (120, 200 + i * 60))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()