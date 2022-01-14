from flask_restful import Api, Resource, reqparse

class ApiHandler(Resource):
    def get(self):
        return {
            'resultStatus': 'SUCCESS',
            'message': ''
        }


    def post(self):
        print(self)
        parser = reqparse.RequestParser()
        parser.add_argument('type', type=str)
        parser.add_argument('message', type=str)

        args = parser.parse_args()

        print(args)

        request_type = args['type']
        request_json = args['message']

        ret_status = request_type
        ret_msg = request_json

        if ret_msg:
            message = 'Your Message Requested: {}'.format(ret_msg)
        else:
            message = 'No Msg'

        final_ret = {"status": "Success", "message": message}

        return final_ret