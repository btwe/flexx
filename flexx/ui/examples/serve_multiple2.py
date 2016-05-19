"""
Import apps from other example modules, and host these as widgets in a
single app.
"""

from flexx import app, ui

from flexx.ui.examples.drawing import Drawing
from flexx.ui.examples.circles import Circles
from flexx.ui.examples.twente import Twente


class MultiApp(ui.DockPanel):
    def init(self):
        Drawing(title='Drawing')
        Circles(title='Circles')
        Twente(title='Twente')


if __name__ == '__main__':
    # This example is setup as a desktop app
    app.launch(MultiApp)
    app.run()
