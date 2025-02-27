import pandas as pd
from .models import Prevencion, Group
#import openai
from django.conf import settings
from .constances import SYSTEM_PROMPT

# API_KEY = settings.API_KEY_OPEN_AI
# client = openai.OpenAI(api_key=API_KEY)

def cargar_datos_desde_excel(ruta_archivo, academic_year):
    # Leer el archivo Excel
    
    df = pd.read_excel(ruta_archivo, sheet_name=0)  # Cambia el sheet_name si es necesario
    preventions_list = []
    # Seleccionar las filas a partir de la fila 12 (índice 11 en pandas)
    # Y seleccionar las columnas desde 'A' hasta 'Y'
    df_subset = df.iloc[10:, :25]  # Las columnas A-Y corresponden a los primeros 25 índices (0-24)

    # Iterar sobre las filas del DataFrame filtrado
    for index, row in df_subset.iterrows():
        try:
            # Convertir la fila en un diccionario para facilitar el acceso a los valores
            row_data = row.to_dict()

            # Asignar valores a la instancia de Prevencion
            prevencion = Prevencion(
                numero_de_orden=row_data['Diagnóstico Preventivo por parte del Profesor Guia'],
                nombre_y_apellidos=row_data['Unnamed: 1'],
                grupo=row_data['Unnamed: 2'],
                sexo='M' if row_data['Unnamed: 4'] == 1 else 'F',
                nacionalidad='C' if row_data['Unnamed: 5'] == 1 else 'A' if row_data['Unnamed: 6'] == 1 else 'Otra',
                consumo_social_alcohol=row_data['Unnamed: 8'],
                consumo_riesgoso_alcohol=row_data['Unnamed: 9'],
                consumo_ocasional_cigarro=row_data['Unnamed: 10'],
                consumo_regular_cigarro=row_data['Unnamed: 11'],
                otros_tipos_adicciones_numero=row_data['Unnamed: 12'],
                otros_tipos_adicciones_tipo=row_data['Unnamed: 13'],
                consumo_psicofarmacos_receta=row_data['Unnamed: 14'],
                consumo_psicofarmacos_automedicacion=row_data['Unnamed: 15'],
                vinculo_grupos_sociales_numero=row_data['Unnamed: 16'],
                vinculo_grupos_sociales_tipo=row_data['Unnamed: 17'],
                problemas_personalidad=row_data['Unnamed: 18'],
                problemas_psiquiatricos=row_data['Unnamed: 19'],
                problemas_personales_familiares_sociales_economicos=row_data['Unnamed: 20'],
                problemas_academicos=row_data['Unnamed: 21'],
                problemas_disciplina=row_data['Unnamed: 22'],
                problema_asistencia=row_data['Unnamed: 23'],
                caso_nuevo=row_data['Unnamed: 24']
            )
            
            # Guardar la instancia en la base de datos
            prevencion.save()
            preventions_list.append(prevencion)
            
            
        
        except Exception as e:
            print(f"Error al procesar la fila {index + 11}: {e}")  # +11 para mostrar el número de fila correcto
            continue  # Continúa con la siguiente fila
        
    if preventions_list:
        group_number = preventions_list[0].grupo
        existing_group = Group.objects.filter(
            number=group_number,
            academic_year=academic_year,
        ).first()
        if existing_group:
            group = existing_group
        else:
            group = Group(number=group_number, academic_year=academic_year)
            group.save()
        for prevencion in preventions_list:
            if group.number == prevencion.grupo:
                existing_prevencion = group.prevenciones.filter(
                    nombre_y_apellidos=prevencion.nombre_y_apellidos,
                ).exists()
                if not existing_prevencion:
                    group.prevenciones.add(prevencion)
        group.save()

# class FormatedMessages:
#     """ Class to handle GPT IA messages """

#     def __format_messages(self, messages):
#         formatted_messages = [
#             # {
#             #     "role": "system",
#             #     "content": SYSTEM_PROMPT,
#             # },
#             {
#                 "role": "user",
#                 "content": messages,
#             }
#         ]
#         return formatted_messages

#     def get_formatted_messages(self, messages):
#         return self.__format_messages(messages)

# class GPTResponse:
#     """ Class to handle GPT IA responses """
    
#     def __handle_response(self, response):
#         response_text = response.choices[0].message.content
#         return response_text
    
#     def response_manager(self, prompt):
#         response = client.chat.completions.create(
#             model="gpt-4o",
#             messages=prompt
#         )
#         return self.__handle_response(response)
        