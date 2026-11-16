pragma ComponentBehavior: Bound
import QtQuick
import qs.Ui
import "../lib/kit" as V

Item {
    id: root
    property var bar: null
    property string moduleName: "yourname.hello"
    property var settings: ({})
    property bool opened: false
    implicitWidth: button.implicitWidth
    implicitHeight: bar ? bar.barSize : 40

    function open() {
        opened = true
        if (bar) bar.requestPopout(root)
    }
    function close() {
        opened = false
        if (bar) bar.releasePopout(root)
    }
    function toggle() { if (opened) close(); else open() }
    function closeForPopoutSwitch() { close() }

    V.Theme { id: theme; bar: root.bar }
    WidgetButton {
        id: button
        anchors.fill: parent
        bar: root.bar
        text: "Hello"
        tooltipText: "Open Hello Velunori"
        onPressed: function(buttonCode) { if (buttonCode === Qt.LeftButton) root.toggle() }
    }
    V.Panel {
        bar: root.bar
        anchorItem: button
        owner: root
        open: root.opened
        contentWidth: fittedContentWidth(300)
        contentHeight: fittedContentHeight(content.implicitHeight)
        focusTarget: keys
        PanelKeyCatcher {
            id: keys
            anchors.fill: parent
            onCloseRequested: root.close()
            onTabRequested: function(direction) {
                if (root.bar) root.bar.switchPanelFrom(root, direction)
            }
            Column {
                id: content
                width: parent.width
                spacing: theme.spacing
                Text {
                    width: parent.width
                    text: "Hello from Velunori Library."
                    color: theme.text
                    font.family: theme.fontFamily
                    font.pixelSize: 16
                    wrapMode: Text.WordWrap
                }
                V.Button {
                    text: "Close"
                    bar: root.bar
                    onClicked: root.close()
                }
            }
        }
    }
}
