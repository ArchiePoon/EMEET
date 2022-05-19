import uiautomation

windows_control = uiautomation.WindowControl(searchDepth=1, Name="eMeetLink")

class Test_cloes_windows:
    def test_cloes_windows(self):
        windows_control.ButtonControl(searchDepth=5,
                         AutomationId="eMeetLinkClass.centralWidget.widget.widget_title_bar.btnQuitApp",
                         ClassName="QPushButton").Click()