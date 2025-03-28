import aiohttp
import asyncio

# Función asincrónica para obtener datos desde una API
# async def obtener_datos():
#     async with aiohttp.ClientSession() as session:
#         async with session.get('https://api.example.com/data') as respuesta:
#             datos = await respuesta.json()  # Parsear el JSON
#             print(datos)

# # Llamar la función asincrónica
# asyncio.run(obtener_datos())

#get
URL = 'http://localhost:3000/api/rol/'
async def obtener_roles():
    async with aiohttp.ClientSession() as session: # tipo como prisma para primero entablar conexion con el cliente
        async with session.get(URL) as response:
            if response.status == 200:
                roles = await response.json()  # Convertir la respuesta JSON en un diccionario
                print(roles)
            else:
                print(f"Error al obtener roles: {response.status}")
#post


#json para el body
#enviar cabeceras
async def crear_rol():
    payload = {'nombre': "EXPLOTADOR"}
    headers = {'Content-Type': "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.post(URL, json = payload, headers = headers) as response:
            if response.status == 200:
                rol = await response.json()
                print(rol)
            else:
                print(f"hubo un error..{response.status}")

#put
async def update_rol():
    payload = {'nombre': "explorador"}
    headers = {'Content-Type': "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.put(f"{URL}/5",json = payload, headers = headers) as response:
            if response.status == 200:
                rol = await response.json()
                print(rol)
            else:
                print(f"hubo un error..{response.status}")
            
#obtener rol
async def get_rol():
    #payload = {'nombre': "explorador"}
    headers = {'Content-Type': "application/json"}
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{URL}/5") as response:
            if response.status == 200:
                rol = await response.json()
                print(rol)
            else:
                print(f"hubo un error..{response.status}")

#eliminar rol

async def delete_rol():
    async with aiohttp.ClientSession() as session:
        async with session.delete(f"{URL}/5") as response:
            if response.status == 200:
                rol = await response.json()
                print(rol)
            else:
                print(f"hubo un error..{await response.json()}")
asyncio.run(obtener_roles())