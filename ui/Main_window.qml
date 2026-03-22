import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {

    anchors.fill: parent
    color: "#12141A"

    RowLayout {
        anchors.fill: parent
        spacing: 0
        Rectangle {
            Layout.preferredWidth: 300
            Layout.fillHeight: true
            color: "#3B4155"
            ColumnLayout {
                anchors.fill: parent
                anchors.margins: 8
                spacing: 8
                RowLayout {
                    Layout.fillWidth: true
                    Layout.alignment: Qt.AlignTop
                    Layout.preferredHeight: 36
                    spacing: 8
                    Rectangle {
                        width: 30
                        height: 30
                        color: "#3B4155"
                        Column {
                            anchors.centerIn: parent
                            spacing: 8
                            Rectangle {color: "#181818"; width: 30; height: 3}
                            Rectangle {color: "#181818"; width: 30; height: 3}
                            Rectangle {color: "#181818"; width: 30; height: 3}
                        }
                    }

                    Rectangle {
                        Layout.fillWidth: true
                        height: 30
                        radius: 11
                        color: "#D9D9D9"

                        TextInput {
                            anchors {fill: parent; leftMargin: 10; rightMargin: 10}
                            verticalAlignment: TextInput.AlignVCenter
                            color: "#000000"

                            font.pixelSize: 12

                            Text {
                                anchors.fill: parent
                                verticalAlignment: Text.AlignVCenter
                                text: "Поиск..."
                                color: "#000000"
                                opacity: 0.3
                                font.pixelSize: 14
                                visible: parent.text === ""
                            }
                        }
                    }
                }
                ListView {
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                    clip: true
                    model: ListModel {

                    }
                    delegate: Rectangle {
                        width: ListView.view.width
                        height: 50
                        radius: 4
                        color: "#D9D9D9"
                        Column {
                            anchors { left: parent.left; leftMargin: 10; verticalCenter: parent.verticalCenter }
                            Text { text: name;  color: "#000000"; font.pixelSize: 12 }
                            Text { text: iduser;  color: "#000000"; font.pixelSize: 12 }
                        }
                    }
                }
            }


        }
    }
}
