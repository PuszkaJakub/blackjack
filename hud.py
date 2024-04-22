class Button:
    def __init__(self, image, position, text, font, color_normal, color_onclick):
        self.image = image
        self.position_x = position[0]
        self.position_y = position[1]
        self.text = text
        self.font = font
        self.color_normal = color_normal
        self.color_onclick = color_onclick
        self.title = self.font.render(text, True, self.color_normal)
        if self.image is None:
            self.image = self.title
        self.rect = self.image.get_rect(center=(self.position_x, self.position_y))
        self.text_rect = self.title.get_rect(center=(self.position_x, self.position_y))

    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.title, self.text_rect)

    def check_input(self, position):
        return (position[0] in range(self.rect.left, self.rect.right)
                and position[1] in range(self.rect.top, self.rect.bottom))

    def change_color(self, position):
        if (position[0] in range(self.rect.left, self.rect.right)
                and position[1] in range(self.rect.top, self.rect.bottom)):
            self.title = self.font.render(self.text, True, self.color_onclick)
        else:
            self.title = self.font.render(self.text, True, self.color_normal)

