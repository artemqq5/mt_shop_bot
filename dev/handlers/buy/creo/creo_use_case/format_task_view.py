def check_view_order(order_params: dict[str, str]) -> str:
    formated_order = ""

    for param in order_params:
        if param != 'general':
            formated_order += f"<b>{param}:</b> {order_params[param]}\n"
        else:
            for param_general in order_params[param]:
                formated_order += f"<b>{param_general}:</b> {order_params[param][param_general]}\n"

    return formated_order
