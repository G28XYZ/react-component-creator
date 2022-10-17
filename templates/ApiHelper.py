def ApiHelper(name):
    nameCapitalize = name.capitalize()
    return f"""
import {{ Inject, Service }} from "typedi";

import {{ RequestFactory }} from "../../../../Core/react/service/api/RequestFactory";
import {{ RequestMethod }} from "../../../../Core/react/service/api";
// import * as Urls from "./urls";

/** Сервис api, инкапсулирующий запросы к серверу **/
@Service("{nameCapitalize}Api")
export class {nameCapitalize}Api {{
  @Inject("RequestFactory")
  private requestFactory: RequestFactory;
}}
"""

# export default {
#     dhcpServer: cgi_rest_service_url ? cgi_rest_service_url + 'dhcp_server' : '/services/dhcp_server'
# }