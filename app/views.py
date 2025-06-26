from django.shortcuts import render
import requests


def green_api(request):
    context = {}
    if request.method == "POST":
        
        api_url = "https://1103.api.green-api.com"
        id_instance = request.POST.get("id_instance")
        api_token_instance = request.POST.get("api_token_instance")
        context["id_instance"] = id_instance
        context["api_token_instance"] = api_token_instance

        if request.POST.get("action") == "get_settings":
            url = f"{api_url}/waInstance{id_instance}/getSettings/{api_token_instance}"
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.status_code)
            context["response"] = response.json()
            return render(request, "home.html", context)

        elif request.POST.get("action") == "get_state_instance":
            url = f"{api_url}/waInstance{id_instance}/getStateInstance/{api_token_instance}"
            payload = {}
            headers = {}
            response = requests.request("GET", url, headers=headers, data=payload)
            print(response.status_code)
            context["response"] = response.json()
            return render(request, "home.html", context)

        elif request.POST.get("action") == "send_message":
            url = f"{api_url}/waInstance{id_instance}/sendMessage/{api_token_instance}"
            suffix = request.POST.get("suffix_sendMessage")
            chat_id = request.POST.get("other_id_sendMessage")
            message = request.POST.get("message_text_sendMessage")
            payload = {"chatId": f"{chat_id}{suffix}", "message": message}
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, json=payload, headers=headers)
            context["response"] = response.json()
            print(response.status_code)
            return render(request, "home.html", context)

        elif request.POST.get("action") == "send_file_by_url":
            url = (
                f"{api_url}/waInstance{id_instance}/sendFileByUrl/{api_token_instance}"
            )
            suffix = request.POST.get("suffix_sendFileByUrl")
            chat_id = request.POST.get("other_id_sendFileByUrl")
            url_file = request.POST.get("message_text_sendFileByUrl")
            file_name = request.POST.get("file_name_sendFileByUrl")
            payload = {
                "chatId": f"{chat_id}{suffix}",
                "urlFile": url_file,
                "fileName": file_name,
            }
            headers = {"Content-Type": "application/json"}
            response = requests.post(url, json=payload, headers=headers)
            context["response"] = response.json()
            print(response.status_code)
            print(response.json())
            print(response.text)
            return render(request, "home.html", context)

    return render(request, "home.html")
