from flask import Flask, request, jsonify
from flask_executor import Executor
from flasgger import Swagger
import sys
from docs import template, swag_submit_tpa
from TPACalc import TPAReport, integration

app = Flask(__name__)
executor = Executor(app)
swagger = Swagger(app, template=template)

def log(msg):
    print(msg)
    sys.stdout.flush()

@app.route("/tpa", methods=['POST'])
@swag_submit_tpa
def tpa():
    '''
    API endpoint to submit TPA calculation requests for validated data
    '''
    contents = request.get_json()
    contents = {k.lower(): v for k,v in contents.items()}
    try:
        # TPAReport(**contents)
        executor.submit(TPAReport, **contents)
        paths = integration.get_tpa_paths(
            contents['client_id'], contents['project_id'], contents['stand_id']
        )
        log(contents)
        log("==============")
        return jsonify(paths)
    except Exception as e:
        print(e)
        sys.stdout.flush()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=7113, host="0.0.0.0")