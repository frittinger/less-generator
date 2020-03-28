# stores data in a local file
import os


def save_data_locally(project_name, data):
    file_name = os.path.join(project_name, ".data")
    file_object = open(file_name, 'w')
    file_object.write("# generated automatically")
    for key, value in data.items():
        file_object.write("\n" + key + " = " + value)

    file_object.close()
