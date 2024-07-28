import re
import zipfile
from io import BytesIO
import os
from django.core.files.uploadedfile import SimpleUploadedFile
from ..crw.models import SalarioMinimo
import json
import pandas as pd
from ..core.models import TransactionalFile


def create_zip_file(files: dict, nombre_achivo: str):
    # Open StringIO to grab in-memory ZIP contents
    temp_file = BytesIO()
    # The zip compressor
    zf = zipfile.ZipFile(temp_file, "w")
    for file in files:
        # Calculate path for file in zip
        fdir, fname = os.path.split(files[file].path)
        # zip_path = os.path.join(zip_subdir, fname)
        zip_path = fname
        # Add file, at correct path
        zf.write(files[file].path, zip_path)

    # Must close zip for all contents to be written
    zf.close()
    temp_file.seek(0)
    zip_file = temp_file.read()
    zip_file = SimpleUploadedFile.from_dict({
        'content': zip_file,
        'filename': '{name}.zip'.format(name=nombre_achivo),
        'content-type': 'application/x-zip-compressed'})
    return zip_file


def camel_to_snake(name):
    name = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', name).lower()


def decamelize_dict(dictionary: dict) -> dict:
    keys_change: list = []
    for key in dictionary:
        new_key = camel_to_snake(key)
        keys_change.append([key, new_key])
    for key_pair in keys_change:
        dictionary[key_pair[1]] = dictionary.pop(key_pair[0])
    return dictionary


def get_smml(year: int, valor: float) -> float:
    try:
        salario_minimo = SalarioMinimo.objects.get(year=year).salario
        return float('{:.2f}'.format(valor / salario_minimo))
    except SalarioMinimo.DoesNotExist:
        try:
            salario_minimo = SalarioMinimo.objects.get(year=year - 1).salario
            return float('{:.2f}'.format(valor / salario_minimo))
        except SalarioMinimo.DoesNotExist:
            return None


def lista_concatenada(lista: list[str]):
    if len(lista) == 1:
        return lista[0]
    return ', '.join(lista[:-1]) + ' y ' + lista[-1]


def first_name(nombre: str) -> str:
    nombre_requeridor: str = nombre.strip().split(' ')[0]
    return nombre_requeridor.capitalize()


def select_fields(arguments: dict, editable_fields: list[str]) -> dict:
    args = decamelize_dict(json.loads(json.dumps(arguments)))
    new_dict = {}
    for key in args:
        if key in editable_fields:
            new_dict[key] = args[key]
    return new_dict


def generar_excel_from_dataframe(df: pd.DataFrame, name_file: str, name_sheet: str):
    temp_file = BytesIO()
    writer = pd.ExcelWriter(temp_file, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=name_sheet, index=False)
    writer.save()
    writer.close()
    temp_file.seek(0)
    workbook = temp_file.read()
    file_ = SimpleUploadedFile.from_dict({
        'content': workbook,
        'filename': '{name}.xlsx'.format(name=name_file),
        'content-type': 'application/vnd.ms-excel'})
    file = TransactionalFile.objects.create(file=file_, name=name_file)
    return file.file
