API para conexion a bots en Dialogflow

Utilziando Flask se construyo un API para permitir que una aplicacion externa se conecte a Dialogflow solo enviando los 
siguientes parametros en formato JSON:

Se envia un HTTP POST a la URL http/https://url-o-ip/dialogflow

{
    "project_id": ID del proyecto correspondiente al bot,
    "session_id": ID de la sesion,
    "text": Texto a enviar para detectar el intent,
    "lan": Lenguaje
}

El API respondera con un JSON con la siguiene estructura:

{
    "action": La accion del intent detectado, 
    "response": Respuesta del bot en texto, 
    "parameters": Parametros extraidos por el intent (si aplica)
}