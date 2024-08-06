import azure.functions as func
import logging

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="http_trigger_fa_parse_and_transpose")
@app.blob_input(
    arg_name="excel_table_file",
    path="input/{blob_name}",
    connection = "BLOB_STORAGE",
    data_type="binary"
)
def http_trigger_fa_parse_and_transpose(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            input_path = req_body.get("input_path")
            input_file = req_body.get("input_file")
            output_path = req_body.get("output_path")

        if None in {input_path, input_file, output_path}:
            _result =
            return func.HttpResponse(
                "Please pass input_path, input_file and output_path in the request body",
                status_code=400
            )
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )