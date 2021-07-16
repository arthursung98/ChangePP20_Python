import config
import requests
import json

bearerToken = config.bearerToken

# Create authentification credentials with Twitter token
def bearerAuth(r) :
    r.headers["Authorization"] = f"Bearer {bearerToken}"
    r.headers["User-Agent"] = "v2UserLookupPython"
    
    return r

# GET URL : get userID from username
def userIDURL(name) :
    username = "usernames={}".format(name)
    user_fields = "user.fields=id"
    url = "https://api.twitter.com/2/users/by?{}&{}".format(username, user_fields)

    return url

# Twitter API Request : Get userID from username
def userIDRequest(url) :
    response = requests.request("GET", url, auth=bearerAuth,)

    if(response.status_code != 200) :
        raise Exception("Error sending userID Request !")

    return response.json()

def main() :
    username = "elonmusk"
    username2 = "kanyewest"
    url = userIDURL(username)
    json_response = userIDRequest(url)
    
    x = json.dumps(json_response)
    print(x)

if __name__ == "__main__":
    main()