import tcod

# from actions import EscapeAction, MovementAction
from engine import Engine
from input_handlers import EventHandler
from entity import Entity

def main():
    # screen_width = 60
    # screen_height = 15
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    
    # player_x = int(screen_width / 2)
    # player_y = int(screen_height / 2)

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    engine = Engine( entities       =   entities, 
                     event_handler  =   event_handler,
                     player         =   player )

    with tcod.context.new(
        tileset     =   tileset,
        title       =   "Halllaaaaa",
        vsync       =   True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:
            engine.render(console = root_console, context = context)
            events = tcod.event.wait()
            engine.handle_events(events)

            # ------------------------------------------------------------------
            # root_console.clear()
            # # root_console.print(x=player_x, y=player_y, string="@", fg=(255, 255, 0))
            # root_console.print(
            #     x   =   player.x, 
            #     y   =   player.y, 
            #     string  =   player.char, 
            #     fg      =   player.color)
            # # print(root_console)

            # context.present(root_console)

            # for event in tcod.event.wait():
            #     # if event.type == "QUIT":
            #     #     raise SystemExit()
                
            #     action = event_handler.dispatch(event)

            #     if action is None:
            #         continue

            #     if isinstance(action, MovementAction):
            #         player_x += actionh
                


if __name__ == "__main__":
    main()