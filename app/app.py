from flask import Flask, Response, jsonify, request
import json
from flask_restplus import Api, Resource
from parseLogLine import parseLogLine, parseWholeText
from werkzeug.datastructures import FileStorage
from werkzeug import secure_filename
import re

app = Flask(__name__)
api = Api(app, version='1.0', title='Parse Log', validate=False)

upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True)


@api.route('/upload/')
@api.doc(params={'description': 'upload log file to get a parsed output'})
@api.expect(upload_parser)

class uploadFile(Resource):
	def post(self):
	
		args = upload_parser.parse_args()
		uploaded_file = args['file']
		#print(list(args.keys()))
		if len(list(args.keys()))>0:
			con = uploaded_file.read()
			result = parseWholeText(con)
			return result
		else:
			return{"Please upload proper file"}


@api.route('/')
class LogParse(Resource):
	def get(self):
		return({'Input type':'log file upload'})
		

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
	
