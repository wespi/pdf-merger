from pathlib import Path
from pypdf import PdfWriter
import PySimpleGUI as sg


def is_valid_path(file_path):
    if file_path and Path(file_path).exists():
        return True
    sg.popup_error("file path not correct")
    return False


def merge_pdfs(files_to_merge, output_path, file_name):
    output_path = Path(f"{output_path}")
    merger = PdfWriter()

    for pdf in files_to_merge:
        merger.append(pdf)

    merger.write(output_path / f"{file_name}.pdf")
    merger.close()


def main_window():
    layout = [
        [
            sg.Text("PDFs to Merge:", s=15, justification="r"),
            sg.Input(key="input_files", do_not_clear=False),
            sg.FilesBrowse(),
        ],
        [
            sg.Text("File Name:", s=15, justification="r"),
            sg.Input(key="name", do_not_clear=False),
        ],
        [
            sg.Text("Output Folder:", s=15, justification="r"),
            sg.Input(key="output_path", do_not_clear=False),
            sg.FolderBrowse(),
        ],
        [sg.Button("Merge PDFs", button_color="tomato"), sg.Exit()],
    ]

    window = sg.Window("PDF Merger", layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "Merge PDFs":
            # sg.popup_error("Not yet implemented")
            files_to_merge = values["input_files"].split(";")
            output_path = values["output_path"]
            file_name = values["name"]

            if is_valid_path(output_path):
                merge_pdfs(
                    files_to_merge=files_to_merge,
                    output_path=output_path,
                    file_name=file_name,
                )
    window.close()


if __name__ == "__main__":
    SETTINGS_PATH = Path.cwd()
    settings = sg.UserSettings(
        path=SETTINGS_PATH, filename="config.ini", use_config_file=True
    )
    theme = settings["GUI"]["theme"]
    font_family = settings["GUI"]["font_family"]
    font_size = int(settings["GUI"]["font_size"])
    print(type(font_size))
    sg.theme(theme)
    sg.set_options(font=(font_family, font_size))
    main_window()
