import aiohttp
import asyncio #pip install aiohttp para realizar peticiones asincronas, es como el fetch

async def obtener_usuario():
    url = 'https://jsonplaceholder.typicode.com/users/1'
    
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            # Verificar si la petición fue exitosa
            if response.status == 200:
                usuario = await response.json()  # Convertir la respuesta JSON en un diccionario
                print(usuario)
            else:
                print(f"Error al obtener usuario: {response.status}")

# Crear un bucle de eventos para ejecutar la función asíncrona
async def main():
    await obtener_usuario()

# Ejecutar el bucle de eventos
asyncio.run(main())#esto ejecuta las funciones en general


#estrucutra general
# Función asincrónica para obtener datos desde una API
# async def obtener_datos():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.example.com/data') as respuesta:
#             datos = await respuesta.json()  # Parsear el JSON
#             print(datos)

# # Llamar la función asincrónica
# asyncio.run(obtener_datos())
