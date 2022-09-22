from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(**kwargs):

    output_list = []
    
    if len(kwargs) < 1:
        return USERS

    elif len(kwargs) >= 1:

        #converts id input from string to int
        if "id" in kwargs:
            kwargs.update({"id": str(kwargs["id"])})

        for ind_dict in USERS:
            if kwargs.items() <= ind_dict.items():
                if ind_dict not in output_list:
                    output_list.append(ind_dict)
            else:
                for key, value in kwargs.items():
                    if type(value) == int:
                        if ind_dict[key] in range(value-1, value+2):
                            if ind_dict not in output_list:
                                output_list.append(ind_dict)
                    else: 
                        if ind_dict[key] == value or value.lower() in ind_dict[key].lower():
                            if ind_dict not in output_list:
                                output_list.append(ind_dict)

    return output_list