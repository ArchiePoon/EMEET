import uiautomation
import subprocess
import time
import pytest
import uiautomation as auto
import datetime

subprocess.Popen("C:\Program Files\eMeetLink\eMeetLink.exe")
time.sleep(4)
auto.uiautomation.DEBUG_SEARCH_TIME = True

nowtime = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
windows_control = uiautomation.WindowControl(searchDepth=1, Name="eMeetLink")
#设置为顶层
# windows_control.SetTopmost(True)
class Test_PersonInfo:
    def test_EditPersonName(self):
        windows_control.RadioButtonControl(searchDepth=4,AutomationId="eMeetLinkClass.centralWidget.widget_menu_bar.btn_personal",ClassName="QPushButton").Click()

        windows_control.ButtonControl(searchDepth=14,ClassName="QPushButton",AutomationId="eMeetLinkClass.centralWidget.widget.widget_client.mainStackedWidget.page_personal.stackedWidget.page_personal.stackedWidget_2.page_info.widget_0.widget_.widget_nickname.btnChangeNick").Click()
#清除个人信息中用户名称
        windows_control.EditControl(searchDepth=6,ClassName="QLineEdit",AutomationId="eMeetLinkClass.centralWidget.widget.widget_client.mainStackedWidget.page_personal.stackedWidget.page_personal.stackedWidget_2.page_info.EMUpdateUserNicknameDlg.widget.widget_input.widget_2.lineEditNickname").SendKeys("Back")
        time.sleep(3)
        windows_control.EditControl(searchDepth=6, ClassName="QLineEdit",
                                    AutomationId="eMeetLinkClass.centralWidget.widget.widget_client.mainStackedWidget.page_personal.stackedWidget.page_personal.stackedWidget_2.page_info.EMUpdateUserNicknameDlg.widget.widget_input.widget_2.lineEditNickname").SendKeys(
            "咕咕鸡+%s"%nowtime)
        windows_control.ButtonControl(searchDepth=5, ClassName="QPushButton",
                                      AutomationId="eMeetLinkClass.centralWidget.widget.widget_client.mainStackedWidget.page_personal.stackedWidget.page_personal.stackedWidget_2.page_info.EMUpdateUserNicknameDlg.widget.widget_btn.btn_confirm").Click()

#
# if __name__ == '__main__':
#     pytest.main(["./02_EditPersonInfo_test.py"])
Test_PersonInfo().test_EditPersonName()