{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "a85349e3-ce0d-4103-9abb-b30cba16e3fd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#pip install pytesseract pillow"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "5603cfeb-3e3f-4303-898d-b9015c2d4486",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pytesseract\n",
    "from PIL import Image\n",
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "5be15246-2251-41eb-906b-6b194c3412a0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'244020028 = BRETON NICASIO DIEGO ALEJANDRO\\n244020007 | CARREON ROSALES MARGARITA\\n244020022 + CHAVEZ MARTINEZ JESUS OSIEL\\n244020001 | CONTRERAS RAMOS OSCAR ALBERTO\\n244020003 ~ DELA GUERRA GUERRERO TANIA ESTEFANNY\\n244020018 DIAZ BRIONES BRISA\\n\\n244020026 DIAZ CRISTOBAL LUIS FERNANDO\\n244020021 | DURAN FLORES VALERIA ALEJANDRA\\n244020020 ELIZALDE PEREZ ALINA\\n\\n244020014 GARCIA MOTA ALINE VIOLETA\\n\\n244020002 GUTIERREZ TAPIA ANDREA ITZEL\\n244020025 = HERNANDEZ RAMIREZ JOSE MIGUEL\\n244020019 | HERNANDEZ RAMIREZ JUAN DANIEL\\n244020027 + JUAREZ CUNA LEONARDO\\n\\n244020004 = LOPEZ HERNANDEZ RUTH\\n\\n244020013 = LOPEZ ORTEGA CRISTIAN\\n\\n244020024 = LORENZO LIRA KATHYA\\n\\n244020009 | LUNA AMBROSIO KEVIN YAEL\\n\\n244020010 | MANZANO RAMIREZ DIEGO EMILIO\\n244020016 | MATIAS DIONISIO JOSSELINE\\n\\n244020012 = PANTOJA HERNANDEZ DANIELA SARAHY\\n244020030 PEREZ ROCHA KENIA LIZETH\\n\\n244020006 RIVERA VALENCIA CLAUDIA YADIRA\\n244020011 RODRIGUEZ DE PABLO LILIA XIMENA\\n244020005 SANCHEZ BARBOSA FRIDA MABEL.\\n244020017 = SANCHEZ MUNOZ VALERIA\\n\\n244020008 | SANTOS TORRES JUAN ALBERTO\\n244020023 SIERRA MENDOZA VALENTIN\\n\\n244020015 VALENCIA ESPINO JETXIA JOCABHET\\n244020029 VALLE SOSA ANDREA PAOLA\\n'"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Ruta de la imagen subida\n",
    "image_path = \"/Users/stam/Documents/Documentos - MacBook Air de Eduardo/GitHub/extracting_tables_from_IMAGE/lista_1A11.png\"\n",
    "\n",
    "# Extraer texto de la imagen usando pytesseract\n",
    "image = Image.open(image_path)\n",
    "text = pytesseract.image_to_string(image)\n",
    "\n",
    "# Mostrar el texto extraído (para referencia)\n",
    "text"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "6453e1d8-d785-4426-86e6-3fded7b52a0c",
   "metadata": {},
   "outputs": [],
   "source": [
    "matricula = \"\\n244020028\\n244020007\\n244020022\\n244020001\\n244020003\\n244020018\\n244020026\\n244020021\\n244020020\\n244020014\\n244020002\\n244020025\\n244020019\\n244020027\\n244020004\\n244020013\\n244020024\\n244020009\\n244020010\\n244020016\\n244020012\\n244020030\\n244020006\\n244020011\\n244020005\\n244020017\\n244020008\\n244020023\\n244020015\\n244020029\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "bd33a28f-42a5-4732-9721-416294156c11",
   "metadata": {},
   "outputs": [],
   "source": [
    "nombre = \"\\nBRETON NICASIO DIEGO ALEJANDRO\\nCARREON ROSALES MARGARITA\\nCHAVEZ MARTINEZ JESUS OSIEL\\nCONTRERAS RAMOS OSCAR ALBERTO\\nDE LA GUERRA GUERRERO TANIA ESTEFANNY\\nDIAZ BRIONES BRISA\\n\\nDIAZ CRISTOBAL LUIS FERNANDO\\nDURAN FLORES VALERIA ALEJANDRA\\nELIZALDE PEREZ ALINA\\n\\nGARCIA MOTA ALINE VIOLETA\\nGUTIERREZ TAPIA ANDREA ITZEL\\nHERNANDEZ RAMIREZ JOSE MIGUEL\\nHERNANDEZ RAMIREZ JUAN DANIEL\\nJUAREZ CUNA LEONARDO\\n\\nLOPEZ HERNANDEZ RUTH\\n\\nLOPEZ ORTEGA CRISTIAN\\nLORENZO LIRA KATHYA\\n\\nLUNA AMBROSIO KEVIN YAEL\\nMANZANO RAMIREZ DIEGO EMILIO\\nMATIAS DIONISIO JOSSELINE\\nPANTOJA HERNANDEZ DANIELA SARAHY\\nPEREZ ROCHA KENIA LIZETH\\n\\nRIVERA VALENCIA CLAUDIA YADIRA\\nRODRIGUEZ DE PABLO LILIA XIMENA\\nSANCHEZ BARBOSA FRIDA MABEL\\nSANCHEZ MUNOZ VALERIA\\n\\nSANTOS TORRES JUAN ALBERTO\\nSIERRA MENDOZA VALENTIN\\nVALENCIA ESPINO JETXIA JOCABHET\\nVALLE SOSA ANDREA PAOLA\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "85297f1f-9ff0-4a62-80d3-77b5ecf86cfb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Matrícula\n",
      "0   244020028\n",
      "1   244020007\n",
      "2   244020022\n",
      "3   244020001\n",
      "4   244020003\n",
      "5   244020018\n",
      "6   244020026\n",
      "7   244020021\n",
      "8   244020020\n",
      "9   244020014\n",
      "10  244020002\n",
      "11  244020025\n",
      "12  244020019\n",
      "13  244020027\n",
      "14  244020004\n",
      "15  244020013\n",
      "16  244020024\n",
      "17  244020009\n",
      "18  244020010\n",
      "19  244020016\n",
      "20  244020012\n",
      "21  244020030\n",
      "22  244020006\n",
      "23  244020011\n",
      "24  244020005\n",
      "25  244020017\n",
      "26  244020008\n",
      "27  244020023\n",
      "28  244020015\n",
      "29  244020029\n"
     ]
    }
   ],
   "source": [
    "# Dividir el texto por líneas y luego por espacios para estructurarlo\n",
    "lines = matricula.strip().split(\"\\n\")\n",
    "data = [line.split(maxsplit=2) for line in lines]\n",
    "# Crear un DataFrame\n",
    "df_matricula = pd.DataFrame(data, columns=[\"Matrícula\"])\n",
    "# Mostrar el DataFrame\n",
    "print(df_matricula)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "4e699d90-2139-40d5-a960-32c103cf52a3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                          Nombre Completo\n",
      "0          BRETON NICASIO DIEGO ALEJANDRO\n",
      "1               CARREON ROSALES MARGARITA\n",
      "2             CHAVEZ MARTINEZ JESUS OSIEL\n",
      "3           CONTRERAS RAMOS OSCAR ALBERTO\n",
      "4   DE LA GUERRA GUERRERO TANIA ESTEFANNY\n",
      "5                      DIAZ BRIONES BRISA\n",
      "6            DIAZ CRISTOBAL LUIS FERNANDO\n",
      "7          DURAN FLORES VALERIA ALEJANDRA\n",
      "8                    ELIZALDE PEREZ ALINA\n",
      "9               GARCIA MOTA ALINE VIOLETA\n",
      "10           GUTIERREZ TAPIA ANDREA ITZEL\n",
      "11          HERNANDEZ RAMIREZ JOSE MIGUEL\n",
      "12          HERNANDEZ RAMIREZ JUAN DANIEL\n",
      "13                   JUAREZ CUNA LEONARDO\n",
      "14                   LOPEZ HERNANDEZ RUTH\n",
      "15                  LOPEZ ORTEGA CRISTIAN\n",
      "16                    LORENZO LIRA KATHYA\n",
      "17               LUNA AMBROSIO KEVIN YAEL\n",
      "18           MANZANO RAMIREZ DIEGO EMILIO\n",
      "19              MATIAS DIONISIO JOSSELINE\n",
      "20       PANTOJA HERNANDEZ DANIELA SARAHY\n",
      "21               PEREZ ROCHA KENIA LIZETH\n",
      "22         RIVERA VALENCIA CLAUDIA YADIRA\n",
      "23        RODRIGUEZ DE PABLO LILIA XIMENA\n",
      "24            SANCHEZ BARBOSA FRIDA MABEL\n",
      "25                  SANCHEZ MUNOZ VALERIA\n",
      "26             SANTOS TORRES JUAN ALBERTO\n",
      "27                SIERRA MENDOZA VALENTIN\n",
      "28        VALENCIA ESPINO JETXIA JOCABHET\n",
      "29                VALLE SOSA ANDREA PAOLA\n"
     ]
    }
   ],
   "source": [
    "# Separar los nombres utilizando '\\n' y filtrar líneas vacías\n",
    "nombres_list = [line.strip() for line in nombre.split('\\n') if line.strip()]\n",
    "# Crear el DataFrame\n",
    "df_nombres = pd.DataFrame(nombres_list, columns=['Nombre Completo'])\n",
    "# Mostrar el DataFrame\n",
    "print(df_nombres)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "4b9e6be1-18db-4c59-972d-614647c050d1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "    Matrícula                        Nombre Completo\n",
      "0   244020028         BRETON NICASIO DIEGO ALEJANDRO\n",
      "1   244020007              CARREON ROSALES MARGARITA\n",
      "2   244020022            CHAVEZ MARTINEZ JESUS OSIEL\n",
      "3   244020001          CONTRERAS RAMOS OSCAR ALBERTO\n",
      "4   244020003  DE LA GUERRA GUERRERO TANIA ESTEFANNY\n",
      "5   244020018                     DIAZ BRIONES BRISA\n",
      "6   244020026           DIAZ CRISTOBAL LUIS FERNANDO\n",
      "7   244020021         DURAN FLORES VALERIA ALEJANDRA\n",
      "8   244020020                   ELIZALDE PEREZ ALINA\n",
      "9   244020014              GARCIA MOTA ALINE VIOLETA\n",
      "10  244020002           GUTIERREZ TAPIA ANDREA ITZEL\n",
      "11  244020025          HERNANDEZ RAMIREZ JOSE MIGUEL\n",
      "12  244020019          HERNANDEZ RAMIREZ JUAN DANIEL\n",
      "13  244020027                   JUAREZ CUNA LEONARDO\n",
      "14  244020004                   LOPEZ HERNANDEZ RUTH\n",
      "15  244020013                  LOPEZ ORTEGA CRISTIAN\n",
      "16  244020024                    LORENZO LIRA KATHYA\n",
      "17  244020009               LUNA AMBROSIO KEVIN YAEL\n",
      "18  244020010           MANZANO RAMIREZ DIEGO EMILIO\n",
      "19  244020016              MATIAS DIONISIO JOSSELINE\n",
      "20  244020012       PANTOJA HERNANDEZ DANIELA SARAHY\n",
      "21  244020030               PEREZ ROCHA KENIA LIZETH\n",
      "22  244020006         RIVERA VALENCIA CLAUDIA YADIRA\n",
      "23  244020011        RODRIGUEZ DE PABLO LILIA XIMENA\n",
      "24  244020005            SANCHEZ BARBOSA FRIDA MABEL\n",
      "25  244020017                  SANCHEZ MUNOZ VALERIA\n",
      "26  244020008             SANTOS TORRES JUAN ALBERTO\n",
      "27  244020023                SIERRA MENDOZA VALENTIN\n",
      "28  244020015        VALENCIA ESPINO JETXIA JOCABHET\n",
      "29  244020029                VALLE SOSA ANDREA PAOLA\n"
     ]
    }
   ],
   "source": [
    "df = pd.concat([df_matricula, df_nombres], axis=1)\n",
    "# Mostrar el DataFrame resultante\n",
    "print(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "900f9226-473c-40fe-bdf4-096f3bcf262f",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
