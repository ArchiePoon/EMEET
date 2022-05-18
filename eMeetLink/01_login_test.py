import uiautomation
import os
import subprocess
import time
import pytest

subprocess.Popen("C:\Program Files\eMeetLink\eMeetLink.exe")
time.sleep(5)

# 定位窗口
wc = uiautomation.WindowControl(searchDepth=1, Name="eMeetLink")


class Test_emeetlink_login:
    def test_emeetlin_login(self):
        # 设置为顶层
        # wc.SetTopmost(True)
        sub = wc.GroupControl(searchDepth=1, AutomationId="eMeetLinkClass.centralWidget")

        widget_menu_bar = sub.GroupControl(searchDepth=1, AutomationId="eMeetLinkClass.centralWidget.widget_menu_bar")

        btn_personal = widget_menu_bar.RadioButtonControl(searchDepth=1,
                                                          AutomationId="eMeetLinkClass.centralWidget.widget_menu_bar.btn_personal")

        btn_personal.Click()
        time.sleep(1)

        wc.RadioButtonControl(searchDepth=15, Name="手机号登录").Click()

        time.sleep(1)
        # 输入手机号

        account = '13590237702'
        wc.EditControl(searchDepth=19,
                       AutomationId="eMeetLinkClass.centralWidget.widget.widget_client.mainStackedWidget.page_personal.stackedWidget.page_personal_login.widget.stackedWidgetLogin.page_login.stackedWidget.page_use_password.widget_11.stackedWidget_2.page_4.widget_4.widget_7.lineEditPhone",
                       ClassName="QLineEdit").SendKeys(account)

        wc.EditControl(searchDepth=19,
                       AutomationId="eMeetLinkClass.centralWidget.widget.widget_client.mainStackedWidget.page_personal.stackedWidget.page_personal_login.widget.stackedWidgetLogin.page_login.stackedWidget.page_use_password.widget_11.stackedWidget_2.page_4.widget_4.widget_edit_4.lineEditPhonePW",
                       ClassName="QLineEdit").SendKeys('Pwq123123')
        time.sleep(1)
        wc.ButtonControl(searchDepth=18,
                         AutomationId="eMeetLinkClass.centralWidget.widget.widget_client.mainStackedWidget.page_personal.stackedWidget.page_personal_login.widget.stackedWidgetLogin.page_login.stackedWidget.page_use_password.widget_11.stackedWidget_2.page_4.widget_4.btnPhoneLogin",
                         ClassName="QPushButton").Click()
        time.sleep(8)

        btn_personal.Click()

        label_account = wc.TextControl(searchDepth=13,
                                       AutomationId="eMeetLinkClass.centralWidget.widget.widget_client.mainStackedWidget.page_personal.stackedWidget.page_personal.stackedWidget_2.page_info.widget_info_1.widget_info_1_b.label_account",
                                       ClassName="QLabel")

        assert '13590237702' in str(label_account)
        print('测试通过，账号%s登录成功' % (account))

    def test_cloes_windows(self):
        wc.ButtonControl(searchDepth=5,
                         AutomationId="eMeetLinkClass.centralWidget.widget.widget_title_bar.btnQuitApp",
                         ClassName="QPushButton").Click()


if __name__ == '__main__':
    pytest.main(["./01_login_test.py"])
# a = Test_emeetlink_login()
# a.test_emeetlin_login()
# time.sleep(1)
# a.cloes_windows_test()
