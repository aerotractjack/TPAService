from flasgger import swag_from

template = {
    "swagger": "2.0",
    "info": {
        "title": "TPA Estimate Service API Documentation",
        "description": "API documentation for the Aerotract LabelService tool",
        "version": "1.0.0"
    }
}

swag_submit_tpa = swag_from({
    'responses': {
        200: {
                "description": "Successfully submitted operation",
                "schema": {
                    "type": "object",
                    "properties": {
                        "tpa_rd_plot": {
                            "type": "string",
                            "description": "Path to the TPA RD plot"
                        },
                        "tpa_report": {
                            "type": "string",
                            "description": "Path to the TPA report"
                        }
                    }
                }
            },
        500: {
            'description': 'Failed to submit operation',
            'schema': {
                'type': 'string',
            }
        }
    },
    'parameters': [
        {
            'name': 'client_id',
            'description': 'Client ID of data to process',
            'example': '10007',
            'in': 'body',
            'required': True,
            'type': 'string'
        },{
            'name': 'project_id',
            'description': 'Project ID of data to process',
            'example': '101036',
            'in': 'body',
            'required': True,
            'type': 'string'
        },{
            'name': 'stand_id',
            'description': 'Stand ID of data to process',
            'example': '103',
            'in': 'body',
            'required': True,
            'type': 'string'
        },
        {
            'name': 'desired_confidence',
            'description': 'Desired confidence level of TPA estimate',
            'example': 0.95,
            'in': 'body',
            'required': False,
            'type': 'number',
            'format': 'float'
        },
    ]
})