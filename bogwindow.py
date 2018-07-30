import pyglet

window = pyglet.window.Window()

output = 'Bog World'

label = pyglet.text.Label(output,
    font_name='Times New Roman',
    font_size=36,
    x=window.width//2, y=window.height//2,
    anchor_x='center', anchor_y='center')

document = pyglet.text.decode_text('Hello, world.')
layout = pyglet.text.layout.TextLayout(document, 80, 80)

@window.event
def on_draw():
    window.clear()
    layout.draw()

event_loop = pyglet.app.EventLoop()

@event_loop.event
def on_window_close(window):
    event_loop.exit()
    return pyglet.event.EVENT_HANDLED

pyglet.app.run()
