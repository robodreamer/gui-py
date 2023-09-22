from datetime import datetime
from nicegui import ui
from nicegui.events import ValueChangeEventArguments

dark = ui.dark_mode()

class Demo:
    def __init__(self):
        self.position_sensitivity = 1
        self.rotation_sensitivity = 1
        self.recording = False
        self.start_time = None
        self.elapsed_time = None

    def show(self, event: ValueChangeEventArguments):
        name = type(event.sender).__name__
        ui.notify(f"{name}: {event.value}")

    def start_recording(self):
        self.recording = True
        self.start_time = datetime.now()

    def pause_recording(self):
        self.recording = False
        self.elapsed_time = datetime.now() - self.start_time

    def stop_recording(self):
        self.recording = False
        self.elapsed_time = datetime.now() - self.start_time
        ui.notify(f"Recording stopped. Elapsed time: {self.elapsed_time}")


demo = Demo()

with ui.header().classes(replace="row items-center") as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon="menu").props(
        "flat color=white"
    )
    with ui.tabs() as tabs:
        ui.tab("Teleop Settings")
        ui.tab("Robot Status")
        ui.tab("UI Settings")

with ui.footer(value=False) as footer:
    ui.label("Footer")

with ui.left_drawer().classes("bg-blue-100") as left_drawer:
    ui.label("Side menu")

with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
    ui.button(on_click=footer.toggle, icon="contact_support").props("fab")

with ui.tab_panels(tabs, value="Teleop Settings").classes("w-full"):
    with ui.tab_panel("Teleop Settings"):
        ui.label("Selected axes for teleop")
        with ui.row():
            ui.button("Position Only", on_click=lambda: ui.notify("Position Only"))
            ui.button("Rotation Only", on_click=lambda: ui.notify("Rotation Only"))
            ui.button("Both", on_click=lambda: ui.notify("Both"))
        # with ui.row():

        ui.label('position sensitivity')
        slider_pos = ui.slider(min=0, max=100, value=50).bind_value(
            demo, "position_sensitivity"
        )
        ui.label().bind_text_from(slider_pos, "value")

        ui.label('rotation sensitivity')
        slider_rot = ui.slider(min=0, max=100, value=50).bind_value(
            demo, "rotation_sensitivity"
        )
        ui.label().bind_text_from(slider_rot, "value")

        ui.label('gripper max force [N]')
        slider_rot = ui.slider(min=0, max=50, value=25)
        ui.label().bind_text_from(slider_rot, "value")

        with ui.row():
            ui.button("Start Recording", on_click=demo.start_recording)
            ui.button("Pause Recording", on_click=demo.pause_recording)
            ui.button("Stop Recording", on_click=demo.stop_recording)
        ui.label(f"Start Time for Record: {demo.start_time}").bind_visibility_from(
            demo, "recording"
        )
        with ui.row():
            switch = ui.switch("switch me")
            ui.label("Switch!").bind_visibility_from(switch, "value")
    with ui.tab_panel("Robot Status"):
        ui.label("Joint Positions")
        ui.label('A1')
        slider_pos = ui.slider(min=0, max=1, step=0.1, value=0.5)
        ui.label().bind_text_from(slider_pos, "value")
        ui.label('A2')
        slider_pos = ui.slider(min=0, max=1, step=0.1, value=0.5)
        ui.label().bind_text_from(slider_pos, "value")
        ui.label('A3')
        slider_pos = ui.slider(min=0, max=1, step=0.1, value=0.5)
        ui.label().bind_text_from(slider_pos, "value")
        ui.label('A4')
        slider_pos = ui.slider(min=0, max=1, step=0.1, value=0.5)
        ui.label().bind_text_from(slider_pos, "value")
        ui.label('A5')
        slider_pos = ui.slider(min=0, max=1, step=0.1, value=0.5)
        ui.label().bind_text_from(slider_pos, "value")
        ui.label('A6')
        slider_pos = ui.slider(min=0, max=1, step=0.1, value=0.5)
        ui.label().bind_text_from(slider_pos, "value")
        ui.label('A7')
        slider_pos = ui.slider(min=0, max=1, step=0.1, value=0.5)
        ui.label().bind_text_from(slider_pos, "value")
    with ui.tab_panel("UI Settings"):
        ui.label('Switch mode:')
        ui.button('Dark', on_click=dark.enable)
        ui.button('Light', on_click=dark.disable)



ui.run()
