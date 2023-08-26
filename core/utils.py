import os


def check_header(header):
    if header == "504b0304":
        return "JAR"

    return "ELF" if header == "7f454c46" else "UNKNOWN"


def write_file_to_dir(output_dir, filename, content):
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    if output_dir[:-1] != '/':
        output_dir += "/"

    with open(output_dir + filename, 'wb') as f:
        f.write(content)
