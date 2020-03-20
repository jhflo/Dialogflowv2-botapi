
class nlpprocess:

    def __init__(self, data):
        self.data = data

    def displaydata(self):
        print(self.data)

    def processdata(self):
        import dialogflow_v2 as dialogflow
        from google.oauth2 import service_account
        from protobuf_to_dict import protobuf_to_dict
        credentials = service_account.Credentials.from_service_account_file('C:\\RESPALDO\\RESPALDO\\Infraestructura\\ColombinaBot\\{}.json'.format(self.data["project_id"]))
        session_client = dialogflow.SessionsClient(credentials=credentials)
        session = session_client.session_path(self.data["project_id"], self.data["session_id"])
        text_input = dialogflow.types.TextInput(text=self.data["text"], language_code=self.data["lan"])
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        action = response.query_result.action
        text_resp = response.query_result.fulfillment_text
        parameters = protobuf_to_dict(response.query_result.parameters)
        intent = response.query_result.intent.display_name
        return {"action":action, "intent":intent, "response":text_resp, "parameters":parameters}





