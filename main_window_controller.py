from gui import MainWindow


class MainWindowController:

    def __init__(self, main_window: MainWindow):
        self._main_window = main_window
        from main_frame_controller import MainFrameController
        self._main_frame_controller = MainFrameController(self._main_window.main_frame)
        self._main_window.on_load_event.add(self._on_load)
        self._main_window.on_close_event.add(self.on_close)

    def _on_load(self):
        self._main_frame_controller.load_from_file()

    def on_close(self):
        self._main_frame_controller.save_to_file()
        self._main_window.destroy()