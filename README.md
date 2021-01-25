API for connecting to bots in Dialogflow

Using Flask an API was built to allow an external application to connect to Dialogflow only sending the following parameters in JSON format:

An HTTP POST is sent to the URL http / https: // url-o-ip / dialogflow

{"project_id": ID of the project corresponding to the bot, "session_id": ID of the session, "text": Text to send to detect the intent, "lan": Language}

The API will respond with a JSON with the following structure:

{"action": The action of the detected intent, "response": Bot response in text, "parameters": Parameters extracted by the intent (if applicable)}
