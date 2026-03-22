import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 1280
    height: 620
    title: "Veil"

    function showMain() {
        loader.source = "Main_window.qml"
    }

    Loader {
        id: loader
        anchors.fill: parent
        source: "login.qml"
    }
}