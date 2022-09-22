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
            
        for key, value in kwargs.items():
            for ind_dict in USERS:
                if type(kwargs[key]) == str:
                    if kwargs[key] == ind_dict[key] or kwargs[key].lower() in ind_dict[key].lower():
                        if ind_dict not in output_list:
                            output_list.append(ind_dict) 
                    
                elif type(kwargs[key]) == int:
                    if ind_dict[key] in range(kwargs[key]-1, kwargs[key]+2):
                        if ind_dict not in output_list:
                            output_list.append(ind_dict) 

    return output_list