case_response = {}


def set_response(case_id, response):
    case_response[case_id] = response


def get_response(case_id):
    return case_response.get(case_id)