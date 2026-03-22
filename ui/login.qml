import QtQuick
import QtQuick.Controls
import QtQuick.Layouts

Rectangle {
    color: "#12141A"
    function showMain() {
        loader.source = "Main_window.qml"
    }
    Rectangle {
        width: 440
        height: 390
        anchors.centerIn: parent
        color: "#3B4155"
        ColumnLayout {
            anchors.left: parent.left
            anchors.right: parent.right
            spacing: 16

            TextField {
                id: login_input
                placeholderText: qsTr("Логин")
                placeholderTextColor: "#000000"
                Layout.fillWidth: true
                Layout.preferredHeight: 50
                height: 51
                opacity: 0.5

                color: "#000000"
                font.pixelSize: 16
                font.family: "Roboto"
                verticalAlignment: Text.AlignVCenter

                Layout.leftMargin: 20
                Layout.rightMargin: 20
                Layout.topMargin: 30

                background: Rectangle {
                    color: "#DCDCDC"
                    border.color: textField.focus ? "blue" : "gray"
                    border.width: 1
                }
            }
            TextField {
                id: name_input
                placeholderText: qsTr("Имя")
                placeholderTextColor: "#000000"
                Layout.fillWidth: true
                Layout.preferredHeight: 50
                height: 51
                opacity: 0.5

                color: "#000000"
                font.pixelSize: 16
                font.family: "Roboto"
                verticalAlignment: Text.AlignVCenter

                Layout.leftMargin: 20
                Layout.rightMargin: 20

                background: Rectangle {
                    color: "#DCDCDC"
                    border.color: textField.focus ? "blue" : "gray"
                    border.width: 1
                }
            }
            TextField {
                id: password_input
                placeholderText: qsTr("Пароль")
                placeholderTextColor: "#000000"
                echoMode: TextInput.Password
                Layout.fillWidth: true
                Layout.preferredHeight: 50
                opacity: 0.5

                color: "#000000"
                font.pixelSize: 16
                font.family: "Roboto"
                verticalAlignment: Text.AlignVCenter

                Layout.leftMargin: 20
                Layout.rightMargin: 20

                background: Rectangle {
                    color: "#DCDCDC"
                    border.color: textField.focus ? "blue" : "gray"
                    border.width: 1
                }
                height: 51
            }
            Button {
                id: log_in_button
                text: qsTr("Войти")
                hoverEnabled: false

                background: Rectangle {
                    color: "#090C15"
                }

                font.pixelSize: 24
                font.family: "Roboto"
                Layout.preferredHeight: 52
                Layout.preferredWidth: 230
                Layout.topMargin: 48
                Layout.alignment: Qt.AlignCenter
            }
            Text {
                id: creat_accaunt
                text: qsTr("Создать аккаут")
                property bool hover: false
                Layout.alignment: Qt.AlignCenter
                font.pixelSize: 16
                font.family: "Roboto"
                color: "#C4C4C4"
                MouseArea {
                    anchors.fill: parent
                    cursorShape: Qt.PointingHandCursor
                    onEntered: parent.hover = true
                    onExited: parent.hover = false
                    onClicked: backend.registration(login_input.text, name_input.text, password_input.text)

                }
            }
        }
    }
}
