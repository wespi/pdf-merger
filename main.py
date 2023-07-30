from pathlib import Path
from pypdf import PdfWriter
import PySimpleGUI as sg


def is_valid_path(file_path):
    if file_path and Path(file_path).exists():
        return True
    # sg.popup_error("file path not correct")
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
            sg.Input(key="input_files"),
            sg.FilesBrowse(file_types=(('PDFs', '*.pdf'),)),
        ],
        [
            sg.Text("File Name:", s=15, justification="r"),
            sg.Input(key="name"),
        ],
        [
            sg.Text("Output Folder:", s=15, justification="r"),
            sg.Input(key="output_path"),
            sg.FolderBrowse(),
        ],
        [
            sg.Button("Merge PDFs", button_color="tomato"),
            sg.Button("Reset Inputs"),
            sg.Exit(),
        ],
    ]

    window = sg.Window("PDF Merger", layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event in (sg.WINDOW_CLOSED, "Exit"):
            break
        if event == "Merge PDFs":
            input_files = values["input_files"]
            output_path = values["output_path"]
            file_name = values["name"]

            if input_files and is_valid_path(output_path) and len(file_name) > 0:
                merge_pdfs(
                    files_to_merge=input_files.split(";"),
                    output_path=output_path,
                    file_name=file_name,
                )
                sg.popup("DONE!")
            else:
                sg.popup("Check your Input")
        if event == "Reset Inputs":
            for key, element in window.key_dict.items():
                if isinstance(element, sg.Input):
                    element.update("")
    window.close()


if __name__ == "__main__":
    SETTINGS_PATH = Path.cwd()
    settings = sg.UserSettings(
        path=SETTINGS_PATH, filename="config.ini", use_config_file=True
    )
    theme = settings["GUI"]["theme"]
    font_family = settings["GUI"]["font_family"]
    # font_size = settings["GUI"]["font_size"]
    sg.theme(theme)
    # sg.set_options(font=(font_family, font_size))
    main_window()
