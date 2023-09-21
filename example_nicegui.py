# from nicegui import ui
# from nicegui.events import ValueChangeEventArguments


# class Demo:
#     def __init__(self):
#         self.number = 1


# def show(event: ValueChangeEventArguments):
#     name = type(event.sender).__name__
#     ui.notify(f"{name}: {event.value}")


# ui.button("Button", on_click=lambda: ui.notify("Click"))
# with ui.row():
#     ui.checkbox("Checkbox", on_change=show)
#     ui.switch("Switch", on_change=show)
# ui.radio(["A", "B", "C"], value="A", on_change=show).props("inline")

# # with ui.row():
# #     ui.input("Text input", on_change=show)
# #     ui.select(["One", "Two"], value="One", on_change=show)
# # ui.link("And many more...", "/documentation").classes("mt-8")

# demo = Demo()
# v = ui.checkbox("visible", value=True)
# with ui.column().bind_visibility_from(v, "value"):
#     ui.slider(min=1, max=3).bind_value(demo, "number")
#     ui.toggle({1: "A", 2: "B", 3: "C"}).bind_value(demo, "number")
#     ui.number().bind_value(demo, "number")

# ui.run()


from datetime import datetime
from nicegui import ui
from nicegui.events import ValueChangeEventArguments


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

ui.label("Teleop Helper Menu")
with ui.row():
    ui.button("Position Only", on_click=lambda: ui.notify("Position Only"))
    ui.button("Rotation Only", on_click=lambda: ui.notify("Rotation Only"))
    ui.button("Both", on_click=lambda: ui.notify("Both"))
with ui.row():
    slider_pos = ui.slider(min=0, max=100, value=50).bind_value(
        demo, "position_sensitivity"
    )
    ui.label().bind_text_from(slider_pos, "value")
    slider_rot = ui.slider(min=0, max=100, value=50).bind_value(
        demo, "rotation_sensitivity"
    )
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

ui.run()
