#include <QtGui/QFont>
#include <QtWidgets/QApplication>

int main(int argc, char *argv[]) {
    QGuiApplication qapp(argc, argv);
    qapp.font();
    QFont font;
    printf("Successfully created\n");
}
