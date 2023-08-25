import pygame

# Fensterabmessungen in Pixeln
WINDOW_WIDTH = 960
WINDOW_HEIGHT = 540

# Schriftgröße
FONT_SIZE = 30

# Initialisierung von Pygame
pygame.init()

# Erzeugen eines Fensters
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Wer wird Gillionär")

# Schriftart festlegen
font = pygame.font.Font(None, FONT_SIZE)

# Hintergrundbild laden
background_image = pygame.image.load("logo.jpg")

# Menüoptionen und Auswahl initialisieren
menu_options = ["Neues Spiel", "Optionen", "Credits", "Ende"]
selected_option = 0
sound_enabled = True

# Funktion zum Umschalten des Sounds
def toggle_sound():
    global sound_enabled
    sound_enabled = not sound_enabled

# Hauptschleife des Menüs
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                selected_option = (selected_option - 1) % len(menu_options)
            elif event.key == pygame.K_DOWN:
                selected_option = (selected_option + 1) % len(menu_options)
            elif event.key == pygame.K_RETURN:
                if selected_option == 0:
                    # Hier wird die Funktion für "Neues Spiel" aufgerufen
                    import main
                    main.main()
                    print("Neues Spiel starten")
                elif selected_option == 1:
                    # Hier wird das Optionen-Menü aufgerufen
                    options_running = True
                    while options_running:
                        for option_event in pygame.event.get():
                            if option_event.type == pygame.KEYDOWN:
                                if option_event.key == pygame.K_RETURN:
                                    options_running = False  # Optionen-Menü beenden
                                    print("Optionen schließen")
                                    break
                                elif option_event.key == pygame.K_SPACE:
                                    toggle_sound()  # Soundstatus umkehren
                                    sound_text = "Sound aktiviert: Leertaste"
                                    
                            elif option_event.type == pygame.QUIT:
                                options_running = False  # Optionen-Menü beenden

                        # Zeichnen des Optionen-Menüs hier
                        screen.fill((255, 255, 255))
                        sound_text = "Sound: " + ("Aktiviert" if sound_enabled else "Deaktiviert")
                        sound_color = (0, 255, 0) if sound_enabled else (255, 0, 0)
                        text = font.render(sound_text, True, sound_color)
                        screen.blit(text, (10, 10))
                        back_text = font.render("Zurück (Enter)", True, (0, 0, 0))
                        screen.blit(back_text, (10, 50))
                        pygame.display.flip()

                elif selected_option == 2:
                    # Hier werden die Credits angezeigt
                    print("Credits anzeigen")
                elif selected_option == 3:
                    running = False  # Programm beenden

    # Hintergrund zeichnen
    screen.fill((255, 255, 255))

    # Bild auf die Fenstergröße skalieren
    fit_image = pygame.transform.scale(background_image, (WINDOW_WIDTH, WINDOW_HEIGHT))
    screen.blit(fit_image, (0, 0))

    # Menüoptionen zeichnen
    for i, option in enumerate(menu_options):
        color = (0, 0, 0)
        if i == selected_option:
            color = (255, 0, 0)
        text = font.render(option, True, color)
        screen.blit(text, (10, 180 + i * 50))

    pygame.display.flip()

# Pygame beenden
pygame.quit()
